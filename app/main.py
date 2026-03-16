import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    cmds = ["echo", "exit", "type"]
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command == "exit":
            break
        elif command.split()[0] == "echo":
            print(" ".join(command.split()[1:]))
        elif command.split()[0] == "type":
            if command.split()[1] in cmds:
                print(f"{command.split()[1]} is a shell builtin")
            else:
                print(f"{command.split()[1]}: not found")
        else:
            print(f"{command}: command not found")
    

if __name__ == "__main__":
    main()
