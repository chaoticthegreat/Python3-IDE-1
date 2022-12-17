import os
try:
  import readchar
except:
  os.system("pip3 install readchar")
  import readchar
from readchar import key
username = os.environ["REPL_OWNER"]
os.system("mkdir users/" + username)
os.system("clear")
def load():
  print("All Files In Your Directory: ")
  print(*os.listdir('users/'+username), sep = "\n")
  while True:
    try:
      with open("users/"+username+"/"+input("Type in the name of the file (Don't add the .py)").replace(".py","")+".py", 'r') as read:
        alllines = read.readlines()
      for i in range(len(alllines)):
        alllines[i] = alllines[i].replace("\n","")
    except:print("No file named like that!");pass
    return alllines
def install(args):
  print("Press [CTRL-C] at any time to stop package installion")
  success = []
  for arguma in args:
    try:
      os.system("pip3 install "+arguma)
      print(arguma+" has been installed succesfully")
      success.append(arguma)
    except KeyboardInterrupt:
      input("Package installion stopped... Press [ENTER TO GO BACK TO EDIT MODE]")
      return
    except:
      try:
        input(arguma+" could not be installed...Press [ENTER] to continue package installion")
      except KeyboardInterrupt:
        input("Package installion stopped... Press [ENTER TO GO BACK TO EDIT MODE]")
        return
  print(*success, sep = ", ")
  input("Have been all installed\nPress [ENTER] to go back")
  os.system("clear")
def run(coder):
  os.system("clear")
  print("Running...")
  x = coder.splitlines()
  for line in x:
    with open("tempory.py","a") as appender:
      appender.write(line+"\n")
  try:
    os.system("python3 tempory.py")
    os.system("rm tempory.py")
  except:
    os.system("rm tempory.py")
  input("Code Excution has finished ")
  os.system("clear")
def save(filepath, text):
  with open(filepath,"a") as writer:
    writer.truncate(0)
    for line in text.splitlines():
      writer.write(line+"\n")
def editor(code:list,path):
  for i in range(len(code)):
    split = []
    for char in code[i]:
      split.append(char)
    code[i] = split
  print(len(code))
  try:
    code[len(code)-1].append("|")
  except IndexError:
    code = [["|"]]
  while True:
    print("\033c", end= "")
    print('''
New File         Save            Run          Install Packages        Load File
[CTRL-H]       [CTRL-S]       [CTRL-D]         [CTRL-P]               [CTRL-L]
_______________________________________________________________________________\n\n''')
    for i in range(len(code)):
      total = ""
      for b in range(len(code[i])):
        total+=code[i][b]
      try:
        posi = code[i].index("|")
        line = i
      except:
        pass
      if "#" in total:
        total = total.replace("#","\033[32m#")
      if "print" in total:
        total=total.replace("print","\033[93mprint")
      total=total.replace("input","\033[93minput\033[0m")
      total=total.replace("while","\033[1;34mwhile")
      total=total.replace("if","\033[1;34mif")
      total=total.replace("for","\033[1;34mfor")
      total=total.replace("import","\033[1;34mimport")
      total=total.replace("def","\033[1;34mdef\033[93m")
      total=total.replace("@","\033[1;34m@")
      total=total.replace('\"','\033[0;33m\"')
      total=total.replace('\'','\033[0;33m\'')
      total=total.replace("(","\033[0m(")
      total=total.replace(")","\033[0m)")
      total=total.replace("return","\033[1;34mreturn")
      total=total.replace("[","\033[0m[")
      total=total.replace("{","\033[0m{")
      total=total.replace("}","\033[0m}")
      total=total.replace(",","\033[0m,")
    print(total,"\033[0m")
    keys = readchar.readkey()
    if keys == key.UP:
      if line-1 != -1:
        code[line].remove(code[line][posi])
        if posi > len(code[line-1]) or posi == len(code[line]):
          posi = len(code[line-1])
        code[line-1].insert(posi,"|")
    elif keys == key.DOWN:
      if line+1 < len(code):
        code[line].remove(code[line][posi])
        if posi > len(code[line+1]) or posi == len(code[line]):
          posi = len(code[line+1])
        code[line+1].insert(posi,"|")
    elif keys == key.LEFT:
        code[line].remove(code[line][posi])
        if posi-1 < 0:
          try:
            code[line-1].insert(len(code[line-1]),"|")
          except:
            pass
          continue
        code[line].insert(posi-1,"|")
    elif keys == key.RIGHT:
        code[line].remove(code[line][posi])
        if posi+1 > len(code[line]):
          try:
            print(code)
            code[line+1].insert(0,"|")
            continue
          except:
            code[line].insert(len(code[line]),"|")
            continue

        code[line].insert(posi+1,"|")
    elif keys == key.BACKSPACE:
      if len(code[line]) == 1:
        if len(code) != 1:
          del code[line]
          code[line-1].insert(len(code[line-1]),"|")
        else:
          pass
      else:
        if posi > 0:
          del code[line][posi-1]
    elif keys == key.ENTER:
      delcount = 0
      alldeleted = []
      for i in range(posi,len(code[line])):
        alldeleted.append(code[line][i-delcount])
        del code[line][i-delcount]
        delcount+=1
      code.insert(line+1,alldeleted)
    elif keys == '\x08':
      code = [["|"]]
    elif keys == '\x13':
      j = input("What filename do you want to save this code into [q to cancel]:\n")
      if j == "q":
        continue
      thecode = ""
      for i in range(len(code)):
        for b in range(len(code[i])):
          thecode+=code[i][b]
        thecode+="\n"
      save("users/"+username+"/"+j.replace(".py","")+".py",thecode.replace("|",""))
    elif keys == '\x04':
      thecode = ""
      newcode = code.copy()
      for i in range(len(newcode)):
        if "#" not in newcode[i]:
          for b in range(len(newcode[i])):
            thecode+=newcode[i][b]
          thecode+="\n"
      print(thecode)
      input()
      run(thecode.replace("|","").replace("\033[0;33m","").replace("\033[0m",""))
    elif keys == "\x10":
      install(input("Type all the packages you want to install seperated by spaces or commas:\n").replace(","," ").split())
    elif keys == "\x0c":
     code= load()
     for i in range(len(code)):
      split = []
     for char in code[i]:
      split.append(char)
     code[i] = split
     try:
        code[len(code)-1].append("|")
     except IndexError:
      code = [["|"]]
    elif keys == "(":
      del code[line][posi]
      code[line].insert(posi,keys)
      code[line].insert(posi+1,"|")
      code[line].insert(posi+2,")")
    elif keys == '\"' or keys == "\'":
      del code[line][posi]
      code[line].insert(posi,keys)
      code[line].insert(posi+1,"|")
      code[line].insert(posi+2,keys)
    else:
      del code[line][posi]
      code[line].insert(posi,keys)
      code[line].insert(posi+1,"|")
while True:
  choice = input("Pick the number of the choice:\n1. Open a file\n2. Make a new file\n")
  if choice == "1":
    print("All Files In Your Directory: ")
    print(*os.listdir('users/'+username), sep = "\n")
    while True:
      try:
        with open("users/"+username+"/"+input("Type in the name of the file (Don't add the .py)").replace(".py","")+".py", 'r') as read:
          alllines = read.readlines()
        for i in range(len(alllines)):
          alllines[i] = alllines[i].replace("\n","")
      except:print("No file named like that!");pass
      editor(alllines,"fg")
      break
    break
  elif choice == '2':
    x=input("Type in the name of the file (Don't add the .py)")
    with open("users/"+username+"/"+x.replace(".py","")+".py", 'a') as a:
      pass
    with open("users/"+username+"/"+x.replace(".py","")+".py", 'r') as read:
      alllines = read.readlines()
    for i in range(len(alllines)):
      alllines[i] = alllines[i].replace("\n","")
    editor(alllines,"fg")
    break
  else:
    continue