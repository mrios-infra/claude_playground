"""
Project Euler Problem 25: 1000-digit Fibonacci number

The Fibonacci sequence is defined by the recurrence relation:
    F(n) = F(n-1) + F(n-2), where F(1) = 1 and F(2) = 1.

So the sequence starts: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

QUESTION: What is the index (position) of the FIRST Fibonacci number
          that has 1000 digits?

For example, the first Fibonacci number with 3 digits is F(12) = 144,
so for "3 digits" the answer would be 12.
"""


def first_fibonacci_index_with_digits(num_digits: int) -> int:
    # We want the first Fibonacci number that has `num_digits` digits.
    # A number has at least `num_digits` digits when it is >= 10^(num_digits - 1).
    # Example: a 3-digit number is anything >= 100, and 100 == 10^(3-1).
    # So we set a "threshold" and stop as soon as a Fibonacci number reaches it.
    threshold = 10 ** (num_digits - 1)

    # `a` holds F(n-1) and `b` holds F(n). We start at F(1)=1 and F(2)=1,
    # so `b` currently represents F(2), which is why `index` starts at 2.
    a, b = 1, 1
    index = 2

    # Keep generating the next Fibonacci number until `b` is big enough.
    # Each loop iteration moves one step forward in the sequence:
    #   new previous = old current
    #   new current  = old previous + old current
    while b < threshold:
        a, b = b, a + b   # advance to the next Fibonacci number
        index += 1        # and bump the position counter

    # When the loop ends, `b` is the first Fibonacci number with enough digits,
    # and `index` is its position in the sequence -- exactly what we want.
    return index


# This block only runs when you execute the file directly (e.g. `python3 problem_025.py`).
# It would NOT run if another file imported this one as a module.
if __name__ == "__main__":
    answer = first_fibonacci_index_with_digits(1000)
    print(answer)  # Expected output: 4782
