import subprocess
import sys


def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    if action == '--c':
        subprocess.call(['python3', 'dmp_create.py'])
    elif action == '--d':
        subprocess.call(['python3', 'dmp_delete.py'])
    else: #action == '':
        print("there is no action in the command ,excepted --c for create or --d for delete")


if __name__ == '__main__':
    main()
