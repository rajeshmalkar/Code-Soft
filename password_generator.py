import random
import string
def mypassword(length):
  charactors = string.ascii_letters + string.digits 
  # Generate a random password of the given length
  password = ''.join(random.choice(charactors) 
  for i in range(length))
  return password
def main():
  # Ask the user for the desired length of the password
  length = int(input("Enter the desired length of the password: "))
  # Generates a password of the specified length
  password = mypassword(length)
  print("Your password is:", password)
if __name__ == "__main__":
  main()