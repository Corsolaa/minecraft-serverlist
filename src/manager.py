import subprocess
import yaml

CONFIG_PATH = "config/servers.yaml"


class ServerManager:
    def __init__(self):
        self.servers = self.load_config()

    def load_config(self):
        with open(CONFIG_PATH, "r") as file:
            return yaml.safe_load(file)["servers"]

    def start_server(self, server_name):
        if server_name in self.servers:
            script_path = self.servers[server_name]["path"]
            subprocess.Popen(["bash", script_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✅ {server_name} started.")
        else:
            print(f"❌ Server '{server_name}' not found.")

    def stop_server(self, server_name):
        if self.is_running(server_name):
            subprocess.run(["screen", "-S", server_name, "-X", "quit"])
            print(f"🛑 {server_name} stopped.")
        else:
            print(f"⚠️ {server_name} is not running.")

    def restart_server(self, server_name):
        self.stop_server(server_name)
        self.start_server(server_name)
        print(f"🔄 {server_name} restarted.")

    def is_running(self, server_name):
        result = subprocess.run(["screen", "-ls"], capture_output=True, text=True)
        return server_name in result.stdout

    def list_servers(self):
        print("📋 Server List:")
        for server in self.servers.keys():
            status = "🟢 Running" if self.is_running(server) else "🔴 Stopped"
            print(f" - {server}: {status}")


if __name__ == "__main__":
    manager = ServerManager()
    manager.list_servers()
