import sys
import os
import subprocess

def main():
    cmds = ["echo", "exit", "type", "pwd"]
    paths = os.environ.get("PATH", "").split(os.pathsep)
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command == "exit":
            break
        elif command.split()[0] == "echo":
            print(" ".join(command.split()[1:]))
        elif command.split()[0] == "type":
            arg = command.split()[1]
            if arg in cmds:
                print(f"{arg} is a shell builtin")
            elif is_valid_command(arg, paths):
                print(f"{arg} is {os.path.abspath(get_command_path(arg, paths))}")
            else:
                print(f"{arg}: not found")
        elif is_valid_command(command.split()[0], paths):
            subprocess.run(command.split())
        elif command == "pwd":
            print(os.getcwd())
        else:
            print(f"{command}: command not found")
    
def is_valid_command(cmd: str, paths: list) -> bool:
    for path in paths:
        full_path = os.path.join(path, cmd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return True
    return False

def get_command_path(cmd: str, paths: list) -> str:
    for path in paths:
        full_path = os.path.join(path, cmd)
        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path
    return ""


if __name__ == "__main__":
    main()
