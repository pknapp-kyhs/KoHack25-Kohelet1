import appInterface as home
import familyUploads as upload
import accountPage as account



# Prompt user for account creation or login
while True:
  accountChoice = input("Do you want to (1) Create an account or (2) Log in? ")
  if accountChoice == "1":
    account.create_account()
    break
  elif accountChoice == "2":
    account.login()
    break
  else:
    print("Invalid choice. Please enter 1 or 2.")






appRunning = True


while appRunning:
  openToAppTKINTER = input("Open the app in a graphical interface? (Y/N): ") #user is prompted to user tkinter graphical interface for the family tree feature or to use the console text-input system for the file upload and search feature
  if openToAppTKINTER.upper() in ["Y","YE","YES"]:
      home.tkinterWin() 

  elif openToAppTKINTER.upper() in ["N","NO"]:
    consoleVersionRunning = True
    while consoleVersionRunning:
      textBasedAppInput = input("What would you like to do? (1) Upload documents, (2) Quit \n{to view/edit the family tree, return to tkinter (type return to return)")
      if str(textBasedAppInput) == "1":
        upload.upload_family_document()
      elif str(textBasedAppInput) == "2": 
        appRunning = False
      elif str(textBasedAppInput) == "return":
        consoleVersionRunning = False
        
      else:
        print("Please enter a valid option")
          

     
  

