import subprocess
import sys

def start_services():
    subprocess.run(["docker-compose", "up", "-d"], check=True)

def stop_services():
    subprocess.run(["docker-compose", "down"], check=True)

def open_terminal():
    container_id = subprocess.run(["docker-compose", "ps", "-q", "ls-cli-dev"], check=True, text=True, capture_output=True).stdout.strip()
    subprocess.run(["docker", "exec", "-it", container_id, "/bin/bash"], check=True)

if len(sys.argv) != 3 or sys.argv[1] != "dev":
    print(f"Usage: {sys.argv[0]} dev {{start|stop|terminal}}")
    sys.exit(1)

command = sys.argv[2]

if command == "start":
    start_services()
elif command == "stop":
    stop_services()
elif command == "terminal":
    open_terminal()
else:
    print(f"Invalid command. Usage: {sys.argv[0]} dev {{start|stop|terminal}}")
    sys.exit(1)