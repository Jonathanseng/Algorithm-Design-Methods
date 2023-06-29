def sliding_window(data, window_size):
  """
  Performs window sliding on the given data with the given window size.

  Args:
    data: The data to perform window sliding on.
    window_size: The size of the window.

  Returns:
    A list of the windows of data.
  """

  windows = []
  start = 0
  end = window_size
  while end <= len(data):
    windows.append(data[start:end])
    start += 1
    end += 1

  return windows


if __name__ == "__main__":
  data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  window_size = 3

  windows = sliding_window(data, window_size)

  print(windows)

# This code will first create a list of windows, each of which is the size of the window_size. The code then iterates through the data, adding each window to the list of windows. The code starts by setting the start pointer to 0 and the end pointer to the window_size. The code then checks if the end pointer is less than or equal to the length of the data. If it is, the code adds the data from the start pointer to the end pointer to the list of windows. The code then increments the start pointer and the end pointer by 1. The code repeats this process until the end pointer is greater than the length of the data.

#The code then prints the list of windows.

#To run this code, you can save it as a Python file and then run it from the command line. For example, if you save the code as sliding_window.py, you can run it by typing the following command into the command line:
