import hashlib
import json

def create_account():
  """
  Creates a new account with username and password validation.
  """
  while True:
    username = input("Enter desired username: ")
    password = input("Enter desired password (at least 8 characters, including numbers): ")
    if len(password) < 8 or not any(char.isdigit() for char in password):
      print("Password must be at least 8 characters long and contain at least one number.")
      continue

    confirm_password = input("Confirm password: ")
    if password != confirm_password:
      print("Passwords do not match. Please try again.")
      continue

    # Hash the password twice for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    hashed_password = hashlib.sha256(hashed_password.encode()).hexdigest()

    try:
      # Load existing accounts from file
      with open("accounts.json", "r") as f:
        accounts = json.load(f)
    except FileNotFoundError:
      accounts = {}

    if username in accounts:
      print("Username already exists. Choose another one.")
    else:
      # Add new account to dictionary
      accounts[username] = hashed_password
      # Save updated accounts to file
      with open("accounts.json", "w") as f:
        json.dump(accounts, f)
      print("Account created successfully!")
      break

def login():
  
 # Logs into an existing account with username and password validation.
  
  while True:
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Hash the password twice for security
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    hashed_password = hashlib.sha256(hashed_password.encode()).hexdigest()

    try:
      # Load existing accounts from file
      with open("accounts.json", "r") as f:
        accounts = json.load(f)
    except FileNotFoundError:
      print("No accounts found. Please create an account first.")
      return

    if username in accounts and accounts[username] == hashed_password:
      print("Login successful!")
      return True
    else:
      print("Invalid username or password. Please try again.")