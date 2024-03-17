def main(user):
  """
  Main function that runs the program.

  Args:
    user: The user object.
  """

  # Get the user's input.
  input = raw_input("Enter a number: ")

  # Convert the input to an integer.
  number = int(input)

  # Check if the number is even or odd.
  if number % 2 == 0:
    print("The number is even.")
  else:
    print("The number is odd.")
