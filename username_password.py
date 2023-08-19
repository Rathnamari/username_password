user= "rathna"
pas="tkk"
j=3
while j>0:
    username = input("enter the username: ")
    if user == username:
      password = input("enter the password: ")
      if password==pas:
        print("successfully login")
        break
      else:
        j = j-1
        if j == 2:
          print("invalid password 2 times only left")
        else:
            if j == 1:
              print("invalid password once more")
            else:
              print("account blocked")
    else:
      j = j-1
      if j == 2:
        print("invalid username two chance more")
      else:
          if j==1:
            print ("invalid username once more")
          else:
            print("invalid account blocked ")
