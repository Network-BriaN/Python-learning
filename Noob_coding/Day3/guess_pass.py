import time
secret = "Cisco!23"
count = 1
user = "Safal"
while count <= 3:
    user_pass = str(input("enter pass : "))
    if user_pass not in secret:
        time.sleep(1)
        print("ACCESS DENIED!, try again")
        count +=1
        if count == 4:
            print("Sorry we could not verify user. Try again after 30 min or call "+str.upper(user))
    elif secret in user_pass:
        time.sleep(3)
        print("ACCESS GRANTED. Welcome "+str(user))
        count = 4
