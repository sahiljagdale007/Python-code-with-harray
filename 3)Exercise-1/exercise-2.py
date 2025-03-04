#Create a python progrma capable of greeting you with Good Morning,Good Afternoon
# and Good Evening. Your program should use time module to get the current hour.
# Here is a sample progrma and documentation link for you:


import datetime

def greet():
  """Greets the user based on the current time."""

  current_hour = datetime.datetime.now().hour

  if current_hour < 12:
    greeting = "Good morning!"
  elif current_hour < 18:
    greeting = "Good afternoon!"
  else:
    greeting = "Good evening!"

  print(greeting)

if __name__ == "__main__":
  greet()