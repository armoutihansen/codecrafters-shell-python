import sys
import os

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
            else:
                for path in paths:
                    full_path = os.path.join(path, arg)
                    if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                        print(f"{arg} is {os.path.abspath(full_path)}")
                        break
                else:
                    print(f"{arg}: not found")
        else:
            print(f"{command}: command not found")
    

if __name__ == "__main__":
    main()
