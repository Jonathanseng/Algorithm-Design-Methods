def brute_force(x):
  """Finds the largest number in a list of numbers using brute force."""
  largest = x[0]
  for i in range(1, len(x)):
    if x[i] > largest:
      largest = x[i]
  return largest


if __name__ == "__main__":
  x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  largest = brute_force(x)
  print("The largest number in the list is", largest)

# This code first defines a function called brute_force(). This function takes a list of numbers as input and returns the largest number in the list. The function works by iterating through the list of numbers and keeping track of the largest number seen so far. The largest number is the last number in the list that is greater than or equal to all the previous numbers.

#The code then defines a variable called x and assigns it a list of numbers. The code then calls the brute_force() function and prints the result.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as brute_force.py, you can run it by typing the following command into the command line:
