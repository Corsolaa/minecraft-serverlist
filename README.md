# 🎮 Minecraft Server Manager

A simple Python-based server manager to start, stop, restart, and monitor multiple Minecraft servers.

---

## ⚙️ Setup

### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 2️⃣ Configure Servers
Edit `servers.yaml` to define your servers:

```yaml
servers:
  server1:
    path: "./servers/server1.sh"
  server2:
    path: "./servers/server2.sh"
```

### 3️⃣ Make `.sh` Scripts Executable
Run this command:
```bash
chmod +x servers/*.sh
```

Example `server1.sh`:
```bash
#!/bin/bash
screen -dmS server1 bash -c "java -Xmx2G -Xms2G -jar minecraft_server.jar nogui >> logs/server1.log 2>&1"
```

### 4️⃣ Create Log Directory
```bash
mkdir -p logs
```

---

## 🚀 Usage

Run the script:
```bash
python run.py
```

### Available Options:
1️⃣ List Servers  
2️⃣ Start Server  
3️⃣ Stop Server  
4️⃣ Restart Server  
5️⃣ Exit  

You can also check logs:
```bash
tail -f logs/server1.log
```

---

## 🔧 Features
✔️ Start & Stop Minecraft servers  
✔️ Restart servers  
✔️ Track running status  
✔️ Log output to files  

---

## 🛠 Troubleshooting
### "Server not found" error?
Ensure the server name in `servers.yaml` matches exactly.

### Logs not updating?
Check if the log folder exists and the `.sh` script correctly appends output.

---

## 🐜 License
MIT License. Free to use and modify. 🚀