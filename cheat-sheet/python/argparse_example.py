#!/usr/bin/env python3
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("required", help="required positional arg")
    parser.add_argument("optional", nargs='?', default="some default", help="optional positional arg")
    parser.add_argument("-v", "--verbose", action="store_true", help="be verbose")
    parser.add_argument("-n", "--number", type=int, help="a number")
    parser.add_argument("-c", "--condiment", choices=["ketchup", "mustard", "none"], help="anything else?")
    parser.add_argument("-1", "--required", required=True, type=str, help="required flag with string value")
    parser.add_argument("-2", "--optional", type=str, help="optional flag with string value")
    parser.add_argument("-a", "--const", type=int, nargs = "?", const = 99, help="optional with optional value; -a or -a999")

    # this call will exit the program, if the syntax fails...
    try:
        args = parser.parse_args()
    except:
        print()
        print("To run without errors, try:")
        print("{} aaa -1 bbb".format(parser.prog))
        sys.exit(0)


    args = parser.parse_args()

    print("Required value is: " + args.required)
    print("Optional value is: " + args.optional)
    if args.number != None:
        print("Number is " + str(args.number))
    if args.condiment != None and args.condiment != "none":
        print("Your condiment is " + args.condiment)
    if args.verbose:
        print("I am being verbose.")

    print("Optional 'a' flag value is {}".format(args.const))


if __name__ == "__main__":
    main()