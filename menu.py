import os 

os.system("tput setaf 1")

os.system("figlet -kcf small Red Script")

os.system("tput setaf 3")
os.system("echo -e '\t\tA Linux Based Script To Make Admin Work-Life Easy'")

os.system("espeak-ng -a 1000 -g 0.01 'Welcome to Red Script' && tput setaf 07")

#----------------------------------------------------

print("""\n\nHow would you like to run command Sir
\nlocally or Remotly :""", end=" ")
os.system("""espeak-ng -a 1000 -g 0.01 'How would you like to run command Sir locally or Remotly'""")
rol=input()

#--------------------------------------------------


os.system("tput setaf 2")

print("""\n\nHere is the list of Menu 
pick one whichever you like Sir..! \n\n """)

os.system("""espeak-ng -a 1000 -g 0.01 'Here is the list of Menu pick one whichever you like Sir ' """)

os.system("tput setaf 07")
#----------------------------------------------------

print("""
press 1: For date command
press 2: For cal command
press 3: To change background colour
press 4: To change text/font colour
press 5: To create new user 
press 6: To find Ip-address of website
press 7: To reboot the system
press 8: To boot the system
press 9: To Exit""")

#-----------------------------------------------------

os.system("tput setaf 02")
print("\n\nPut the no. you desire Sir : ",  end="")
os.system("espeak-ng -a 1000 -g 0.01 'Put the Number you desire Sir' ")
os.system("tput setaf 07")
num=input()


if int(num) == 1 :
    os.system("date")
elif int(num) == 2 :
    os.system("cal")
elif int(num) == 3 :
    print(""""\n\n avaliable colour : red, blue, green, yellow
            Give name of colour :""" , end="")
    colour=input()

    if colour == red :
        os.system("tput setab 01")
    elif colour == blue :
        os.system("tput setab 04")
    elif colour == green :
        os.system("tput setab 02")
    elif colour == yellow :
        os.system("tput setab 03")
        print("\n\nBackground colour now changed")
    else :
        print("\n\nInput Error")

elif int(num) == 5 :
    print("\n\nGive name to new user : " , end=" ")
    usr_name=input()
    os.system("useradd " + usr_name)
    print("\n\nGive user a password : ", end="")
    os.system("passwd " + usr_name)

elif int(num) == 6 :
    print("\n\nType website name here to know ip-address : ", end="")
    webs=input()
    os.system("nslookup " + webs)

elif int(num) == 7 :
    print("\n\nSystem Reboot Start Now..!")
    os.system("sleep 1")
    os.system("init 6")

elif int(num) == 8 :
    print("\n\nThank you for using me\n\n")
    os.system("sleep 2")
    os.system("clear")
    exit()

else :
    print("\n\nInput Error")

