

def try_again():
    e = input(" Type 'l' to log in or 'q' to quit: ")
    if e == "l":
        log_in()
    elif e == "q":
        return

    else:
        print("Try again!")
        try_again()

def sign_up():
    print("Sign up")
    username=input("Enter username: ")
    password=input("Enter password: ")
    a=username
    a=a.lower()
    while a[-1] == " ":
        a = a.replace(" ", "")

    b=password
    fw=open('sample.txt','a')
    fw.write(a+"\n")
    fw.write(b+"\n\n")
    fw.close()
    e=input("You successfully signed up! Type 'l' to log in or 'q' to quit: ")
    if e=="l":
        log_in()
    elif e=="q":
        return

    else:
        print("Try again!")
        try_again()



def log_in():
    print("Log in")
    username=input("Enter username: ")
    password=input("Enter password: ")
    a=username
    a=a.lower()
    while a[-1]==" ":
        a=a.replace(" ","")

    b=password
    fr=open('sample.txt','r')
    text=fr.read()
    fr.close()






    if a not in text and b not in text:
        d=input("Incorrect username or password! Type 'r' to try again or 's' to sign up: ")

        if d=="r":
            log_in()
        elif d=="s":
            sign_up()
        else:
            print("Try again!")
            start()

    elif a not in text or b not in text:
        print("Try again!")
        start()
    elif a[0]==" " :
        print("Try again!")
        try_again()


    elif a in text and b in text:
        print("Successfully logged in!")



def start():
    print("Do you want to sign up or log in?")
    c=input("Type 'l' to log in or 's' to sign up: ")
    if c=="l":
        log_in()
    elif c=="s":
        sign_up()
    else:
        print("Try again!")
        start()

start()




