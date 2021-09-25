import time
import random

name = input("Hello what help do  you want: ")

time.sleep(2)
if "help" in name:
    print("ok i shall help!")
else:
    print("I'm sorry to hear that!")

time.sleep(2)

feeling = input("are u happy with help?: ")

time.sleep(2)
if "yes" in feeling:
    print("ok ,have a nice day!")
else:
    print("I'm sorry to hear that!")

time.sleep(2)
exit = input("can i leave now?:")

if "yes" in exit:
 print("ok , thanks")
 
else:
    print("ok we shall meet again.")
