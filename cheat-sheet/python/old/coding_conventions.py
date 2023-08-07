#!/usr/bin/env python

# lists, trailing commas
my_list = [
    1, 2, 3,
    4, 5, 6,
]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

# indentation, snake casing
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one, var_two, var_three, var_four)

# doc strings
def this_function_has_fleas():
    """It doesn't really have fleas."""
    print("fleas")

def this_function_also_has_fleas():
    """Here is a summary line.
    
    And some other lines, after a blank line.
    It doesn't really have fleas.
    """
    print("fleas")

# linebreak before operator.  I don't like this, but it's in PEP8
income = (gross_wages
    + taxable_interest
    + (dividends - qualified_dividends))

# use compact whitespace
spam(ham[1], {eggs: 2})

########

def main():
    long_function_name(1, 22, 333, 4444)

if __name__ == "__main__":
    main()

