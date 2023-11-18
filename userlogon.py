import pathlib

authed = False
snumber = input("Student number: ")
password = input("Password: ")

def parseCreds(snumber, password):
   local = "virtualenv/virtualserver/accounts/"
   if pathlib.Path(local + snumber).exists():
      print("Broker found account")
      if pathlib.Path(local + snumber + "/password.txt").exists():
         if open(local + snumber + "/password.txt", "r").readline() == password:
            if pathlib.Path(local + snumber + "/locked.txt").exists():
               if open(local + snumber + "/locked.txt", "r").readline() == "False":
                  if pathlib.Path(local + snumber + "/displayname.txt").exists():
                     print(f"Welcome, {open(local + snumber + "/displayname.txt", "r").readline()}!")
                     authed = True
                  else: 
                     print("Welcome, User!"); authed = True
               else: print("Account locked. Contact your administrator for more information")
         else: print("Invalid password")   
   else: 
      print("Account not found in registry")
      
parseCreds(snumber, password)
