import pathlib
import os

local = "virtualenv/virtualserver"; loop = True

def ngen(offset):
   if pathlib.Path(local + "/ngencache.txt").exists():
      file0 = open(local + "/ngencache.txt", "r")
      curncache = int(file0.readline())
      file0a = open(local + "/ngencache.txt", "w");  file0a.write(str(curncache + 1))
      file0.close(); file0a.close()
      return str(curncache + 1 + offset)
   
while True and loop:
   cmd = input("vdi.admin>$ ")
   if cmd.find("reset") != -1:
      username = cmd.split()[1]
      if pathlib.Path(local + "/accounts/" + username).exists():
         if pathlib.Path(local + "/accounts/" + username + "/password.txt").exists():
            newpassword = input("Enter a new password: ")
            file5 = open(local + "/accounts/" + username + "/password.txt", "w").write(newpassword); 
            print(f"New password successfully reset on '{username}'")
         else: print(f"password attribute couldn't be found in '{username}'")
      else: print(f"User '{username}' couldn't be found")      

   elif cmd.find("netstat") != -1:
      if cmd.find("-a") != -1:
         file1, file2 = open(local + "/powerState.txt", "r"), open(local + "/status.txt", "r")
         file9 = open(local + "/ngencache.txt", "r")
         print(f"Network debug stats\n > Network state: {file1.readline()}\n > Server response: {file2.readline()}\n > ngencache: {file9.readline()}")
         file1.close(); file2.close(); file9.close()

   elif cmd.find("lock") != -1 and cmd.find("unlock") == -1:
      username = cmd.split()[1]
      if pathlib.Path(local + "/accounts/" + username).exists():
         if pathlib.Path(local + "/accounts/" + username + "/locked.txt").exists():
            if pathlib.Path(local + "/accounts/" + username + "/displayname.txt").exists():
               file3 = open(local + "/accounts/" + username + "/locked.txt", "w+")
               file4 = open(local + "/accounts/" + username + "/displayname.txt", "r")
               file3.write("True")
               print(f"Account '{username}' ({file4.readline()}) has been locked"); file4.close(); file3.close()
            else: 
               open(local + "/accounts/" + username + "/locked.txt", "w").write("True")
               print(f"Account {username} has been locked")
         else: print(f"locked attribute not found on '{username}'")
      else: 
         print(f"Account '{username}' couldn't be found")

   elif cmd.find("unlock") != -1:
      username = cmd.split()[1]
      if pathlib.Path(local + "/accounts/" + username).exists():
         if pathlib.Path(local + "/accounts/" + username + "/locked.txt").exists():
            if pathlib.Path(local + "/accounts/" + username + "/displayname.txt").exists():
               file3 = open(local + "/accounts/" + username + "/locked.txt", "w+")
               file4 = open(local + "/accounts/" + username + "/displayname.txt", "r")
               file3.write("False")
               print(f"Account '{username}' ({file4.readline()}) has been unlocked")
            else: 
               open(local + "/accounts/" + username + "/locked.txt", "w").write("False")
               print(f"Account {username} has been unlocked")
         else: print(f"locked attribute not found on '{username}'")
      else: 
         print(f"Account '{username}' couldn't be found")

   elif cmd.find("accountmgr") != -1:
      mode = input("Would you like to edit, create new or remove a user?: ")
      if mode == "edit":
         user = input("Which user would you like to edit details for?: ")
         if pathlib.Path(local + "/accounts/" + user).exists():
            selAttr = input(f"What detail would you like to edit on '{user}'?: ")
            if selAttr == "name" or selAttr == "Name" or selAttr == "username" or selAttr == "username" or selAttr == "displayname" or selAttr == "Displayname":
               if pathlib.Path(local + "/accounts/" + user + "/displayname.txt").exists():
                  newname = input(f"What would you like to change user '{user}' displayname to?: ")
                  namechangefile = open(local + "/accounts/" + user + "/displayname.txt", "w+")
                  namechangefile.write(str(newname)); namechangefile.close()
                  print(f"Successfully changed atrtibute '{selAttr}' on user '{user}' to \"{newname}\"")
         else: print(f"User '{user}' couldn't be found")
      elif mode == "create" or mode == "create new":
         displayname, password, snum = "", "", ngen(0)
         displayname = input("What is your name: ")
         password = input("Set a password that you'll remember: ")
         os.makedirs(local + "/accounts/" + snum, exist_ok=True)
         crpass = open(local + "/accounts/" + snum + "/password.txt", "w")
         crpass.write(password); crpass.close()
         crname = open(local + "/accounts/" + snum + "/displayname.txt", "w")
         crname.write(displayname); crname.close()
         crlock = open(local + "/accounts/" + snum + "/locked.txt", "w")
         crlock.write("False"); crlock.close()
         print(f"Successfully created account '{snum}' ")

      elif mode == "remove":
         username = input("Which user would you like to delete: ")
         if pathlib.Path(local + "/accounts/" + username).exists():
            confirm = input(f"Are you sure you would like to remove '{username}'? (Y/N): ")
            if confirm == "Y" or confirm == "y":
               if pathlib.Path(local + "/accounts/" + username + "/password.txt").exists():
                  os.remove(local + "/accounts/" + username + "/password.txt")
               if pathlib.Path(local + "/accounts/" + username + "/displayname.txt").exists():
                  os.remove(local + "/accounts/" + username + "/displayname.txt")
               if pathlib.Path(local + "/accounts/" + username + "/locked.txt").exists():
                  os.remove(local + "/accounts/" + username + "/locked.txt")
               os.rmdir(local + "/accounts/" + username)
               print(f"User '{username}' has been deleted")
            elif confirm == "n" or confirm == "N":
               print("Cancelled operation successfully")
            else: print(f"Invalid entry '{confirm}' is not a valid response")
         else: print(f"'{username}' couldn't be found")

   elif cmd.find("whois") != -1:
      username = cmd.split()[1]
      if pathlib.Path(local + "/accounts/" + username).exists():
         if pathlib.Path(local + "/accounts/" + username + "/displayname.txt").exists():
            file7 = open(local + "/accounts/" + username + "/displayname.txt", "r")
            print(f"Name: {file7.readline()}"); file7.close()
         else: print(f"Name: Name attribute not found on '{username}'")
         if pathlib.Path(local + "/accounts/" + username + "/locked.txt").exists():
            file8 = open(local + "/accounts/" + username + "/locked.txt", "r")
            print(f"Locked: {file8.readline()}" ); file8.close()
         else: print(f"Locked: Locked attribute not found on '{username}'")
      else: print(f"'{username}' couldn't be found")

   elif cmd.find("help") != -1 or cmd.find("Help") != -1:
      print("For more detailed guidance and usage, visit the online documentation.")
      print(f"1) accountmgr - manage accounts\n   1a) create - creates a new user\n   1b) edit - edits a users attributes\n   1c) remove - deletes a user")
      print(f"2) help - displays this guidance list\n3) lock <studentnumber> - lock accounts and prevent them from being logged onto")
      print(f"4) netstat <-?>\n   <-a> - displays all network stats")
      print(f"5) reset <studentnumber> - resets a students password")
      print(f"6) unlock <studentnumber> - unlocks a students account to allow the user to log on again")
      print(f"7) whois <studentnumber> - displays details about a user to identify them")
   
   elif cmd.find("exit") != -1 or cmd.find("Exit") != -1or cmd.find("quit") != -1:
      loop = False
      print("Successfully exited adminveiw.py")
      
   else: print(f"Command '{cmd}' is not a valid command.\nUse 'help' for a list of valid commands")
