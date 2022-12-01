#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv) - 1
    arg_total = 0
    for i in range(arg_count):
        arg_total += int(sys.argv[i + 1])
    print("{}".format(arg_total))
