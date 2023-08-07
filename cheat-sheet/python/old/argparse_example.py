#!/usr/bin/env python
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("required", help="required positional arg")
    parser.add_argument("optional", nargs='?', default="some default", help="optional positional arg")
    parser.add_argument("-v", "--verbose", action="store_true", help="be verbose")
    parser.add_argument("-n", "--number", type=int, help="a number")
    parser.add_argument("-c", "--condiment", choices=["ketchup", "mustard", "none"], help="anything else?")
    parser.add_argument("-1", "--required", required=True, type=str, help="required flag with string value")
    parser.add_argument("-2", "--optional", type=str, help="optional flag with string value")

    # this call will exit the program, if the syntax fails...
    args = parser.parse_args()

    print "Required value is: " + args.required
    print "Optional value is: " + args.optional
    if args.number != None:
        print "Number is " + str(args.number)
    if args.condiment != None and args.condiment != "none":
        print "Your condiment is " + args.condiment
    if args.verbose:
        print "I am being verbose."


if __name__ == "__main__":
    main()