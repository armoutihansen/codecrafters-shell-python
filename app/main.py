import sys
import os
import subprocess

def main():
    cmds = ["echo", "exit", "type", "pwd", "cd"]
    paths = os.environ.get("PATH", "").split(os.pathsep)
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        parts = command.split()

        if not parts:
            continue

        if parts[0] == "exit":
            break
        elif parts[0] == "echo":
            print(" ".join(parts[1:]))
        elif parts[0] == "type":
            if len(parts) < 2:
                continue
            arg = parts[1]
            if arg in cmds:
                print(f"{arg} is a shell builtin")
            elif is_valid_command(arg, paths):
                print(f"{arg} is {os.path.abspath(get_command_path(arg, paths))}")
            else:
                print(f"{arg}: not found")
        elif parts[0] == "pwd":
            print(os.getcwd())
        elif parts[0] == "cd":
            target = parts[1] if len(parts) > 1 else os.path.expanduser("~")
            target = os.path.expanduser(target)
            try:
                os.chdir(target)
            except FileNotFoundError:
                print(f"cd: {target}: No such file or directory")
        elif is_valid_command(parts[0], paths):
            subprocess.run(parts)
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
