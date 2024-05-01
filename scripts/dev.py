#!/usr/bin/env python3

import subprocess
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} {{up|down|shell|exec <command>}}")
    sys.exit(1)

command = sys.argv[1]

if command == "up":
    subprocess.run(["docker-compose", "up", "-d"], check=True)
elif command == "down":
    subprocess.run(["docker-compose", "down"], check=True)
elif command == "shell":
    container_id = subprocess.run(["docker-compose", "ps", "-q", "ls-cli-dev"], check=True, text=True, capture_output=True).stdout.strip()
    subprocess.run(["docker", "exec", "-it", container_id, "/bin/bash"], check=True)
elif command == "exec":
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} exec <command>")
        sys.exit(1)
    exec_command = sys.argv[2:]
    container_id = subprocess.run(["docker-compose", "ps", "-q", "ls-cli-dev"], check=True, text=True, capture_output=True).stdout.strip()
    result = subprocess.run(["docker", "exec", container_id] + exec_command, check=True, text=True, capture_output=True)
    print(result.stdout)
else:
    print(f"Invalid command. Usage: {sys.argv[0]} {{up|down|shell|exec <command>}}")
    sys.exit(1)