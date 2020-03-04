#!/usr/bin/env python3
try:
 grade = input("Please let me know how smart or dumb you really are. Please enter your last test score and be honest)



if grade >= 90:
    print("Looks like you are actually pretty smart! " + "You got a " + str(grade) + "," + " WHICH IS AN A." + " Not bad HotShot!!!")

elif grade >= 80:
    print("Looks like you are relatively smart. " + "You got a " + str(grade) + "," + " Which happens to be a B")

elif grade >= 70:
    print("Looks like you are of average American intelligence, yay. " + "You got a " + str(grade) + "," + " Which happens to be a C")

elif grade >= 60:
    print("Looks like you are hanging on by a thread sonny!!!! Whippersnappers like you are what's ruining the country!!! " + "You got a " + str(grade) + "," + " Which is a D")

elif grade <= 59:
    print("Looks like you are about as smart as a box of crackerjacks!!!! " + "You got a " + str(grade) + "," + "WHICH IS AN F")

else:
    print("PLEASE ENTER A VALID INTEGER or FLOAT!!!!!!!")


