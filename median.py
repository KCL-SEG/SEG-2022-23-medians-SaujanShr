"""Median calculator."""

from math import floor

def get_median(numbers):
    n = len(numbers)
    numbers = sorted(numbers)
    return numbers[floor((n-1)/2)] if n%2==1 else \
          (numbers[floor((n/2)-1)] + numbers[floor(n/2)])/2

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(get_median(numbers))