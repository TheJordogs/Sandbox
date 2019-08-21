"""  Jordan Rose  """

import getpass

password = input("Please enter a password\n"
                 "Must be at least 6 characters")
while len(password) < 6:
    password = input("Password must be at least 6 characters")

getpass.getpass()

print(password)