print("This is a line of python code because I want to learn this in preparation for AWS.")
print("This is a second line of code to repeat my previous intent.")
print("Affirmation of the intent set, to make it thrice said.")

challenge2 = 9

if challenge2 < 10:
    print("challenge2 is definitely less than 10")
elif challenge2 >= 10:
    print("challenge2 is definitely greater than or equal to 10")
else:
    print("python formatting is weird.")

challenge3 = 21

if challenge3 <= 10:
    print("challenge3 is le 10")
elif challenge3 > 10 and challenge3 <= 25:
    print("challenge3 is gt 10 but le 25")
    
challenge41 = 43
challenge42 = 11

challenge40 = challenge41 % challenge42 
print(challenge40)


challenge51 = 67
challenge52 = 17
challenge50 = 67 // 17
print(challenge50)

age = 4
if age == 0:
    print("This is just a baby because their age is ")
elif age >= 1 and age < 3:
    print("This is a toddler because they are young!")
elif age >=3 and age < 9:
    print("Okay I am running out of things to print in this case")
else:
    print("I am done with this exercise now can I move on to the next chapter")