from functools import reduce
from operator import mul

def tuple_product(tup):
  """
  Calculates the product of all numbers in a given tuple.

  Args:
    tup: The input tuple containing numbers.

  Returns:
    The product of all numbers in the tuple.
  """
  if not tup:
    return 1  # Handle empty tuple
  return reduce(mul, tup)

# Example usage
my_tuple = (2, 3, 4, 5)
product = tuple_product(my_tuple)
print("Product of numbers in the tuple:", product)  # Output: 120