import sys
import os
import subprocess

def main():
    cmds = ["echo", "exit", "type"]
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
            result = subprocess.run(command.split())
            print(result.stdout.decode())
            # print(f"Program was passed with {len(command.split())} args (including the program name).")
            # print(f"Arg #0 (program name): {command.split()[0]}")
            # for i, arg in enumerate(command.split()[1:], start=1):
            #     print(f"Arg #{i}: {arg}")
            # print(f"Program Signature: {status}")
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
