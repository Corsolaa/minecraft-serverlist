from src.manager import ServerManager

def main():
    manager = ServerManager()

    while True:
        print("\n🎮 Minecraft Server Manager 🎮")
        print("1️⃣ List Servers")
        print("2️⃣ Start Server")
        print("3️⃣ Stop Server")
        print("4️⃣ Restart Server")
        print("5️⃣ Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.list_servers()
        elif choice == "2":
            server = input("Enter server name: ")
            manager.start_server(server)
        elif choice == "3":
            server = input("Enter server name: ")
            manager.stop_server(server)
        elif choice == "4":
            server = input("Enter server name: ")
            manager.restart_server(server)
        elif choice == "5":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid option, try again.")

if __name__ == "__main__":
    main()
