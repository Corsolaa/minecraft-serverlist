import os
import subprocess
import time

import yaml

CONFIG_PATH = "servers.yaml"


class ServerManager:
    def __init__(self):
        self.servers = self.load_config()

    def load_config(self):
        with open(CONFIG_PATH, "r") as file:
            return yaml.safe_load(file)["servers"]

    def start_server(self, server_name):
        if server_name in self.servers:
            script_path = self.servers[server_name]["path"]

            # Create the log file when the server starts
            log_file = f"logs/{server_name}.log"
            if not os.path.exists(log_file):
                open(log_file, 'w').close()  # Create an empty log file if it doesn't exist

            # Start the server and redirect stdout and stderr to the log file
            with open(log_file, 'a') as log:
                subprocess.Popen(["bash", script_path], stdout=log, stderr=log)

            print(f"\n✅ {server_name} started.")
        else:
            print(f"\n❌ Server '{server_name}' not found.")

    def stop_server(self, server_name):
        if self.is_running(server_name):
            subprocess.run(["screen", "-S", server_name, "-X", "stuff", "stop\n"])
            print(f"🛑 {server_name} is stopping. Please wait...")

            log_file = f"logs/{server_name}.log"
            stop_message = "ThreadedAnvilChunkStorage: All dimensions are saved"

            while True:
                with open(log_file, 'r') as log:
                    log_content = log.readlines()
                    if any(stop_message in line for line in log_content):
                        print(f"✅ {server_name} has stopped gracefully.")
                        break
                time.sleep(2)

            subprocess.run(["screen", "-S", server_name, "-X", "quit"])
            print(f"✅ {server_name} session terminated.")
        else:
            print(f"⚠️ {server_name} is not running.")

    def restart_server(self, server_name):
        self.stop_server(server_name)
        self.start_server(server_name)
        print(f"\n🔄 {server_name} restarted.")

    def is_running(self, server_name):
        result = subprocess.run(["screen", "-ls"], capture_output=True, text=True)
        return server_name in result.stdout

    def list_servers(self):
        print("\n📋 Server List:")
        for server in self.servers.keys():
            status = "🟢 Running" if self.is_running(server) else "🔴 Stopped"
            print(f" - {status}: {server}")


if __name__ == "__main__":
    manager = ServerManager()
    manager.list_servers()
