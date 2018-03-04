import sys


OUTPUT_FILENAME = '09_libraries_command_line_arguments.txt'


def write_input_into_file():

    with open(OUTPUT_FILENAME, 'w') as f:

        while True:

            line = input('| ')
            if line == '':
                break

            f.write(line)
            f.write('\n')


def read_file_into_stdout():

    with open(OUTPUT_FILENAME) as f:

        for line in f:
            print(line, end='')


# pt: print to
def ptstderr(*args, **argd):
    print(*args, file=sys.stderr, **argd)


def main():

    if len(sys.argv) < 2:
        ptstderr("Need a command: write or read")
        sys.exit(1)

    command = sys.argv[1]
    try:

        if command == 'write':
            print('Enter blank line to exit.')
            write_input_into_file()

        elif command == 'read':
            read_file_into_stdout()

        else:
            ptstderr('No such command:', command)
            sys.exit(1)

    except IOError as e:
        ptstderr('Error:', e)
        sys.exit(1)


if __name__ == '__main__':
    main()
