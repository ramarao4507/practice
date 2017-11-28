num = int(input("enter number for even/odd :"))

if num%2 > 0:
    print "entered number is odd :" + str(num)
else:
    print "entered number is even :" + str(num)


#If the number is a multiple of 4, print out a different message.

num1 = int(input("enter number for analuysis :"))


#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
if num1%4 == 0:
    print "entered number is multiple of 4 :" + str(num1)
elif num1%2 == 0:
    print "entered number is even :" + str(num1)
else:
    print "entered number is odd :" + str(num1)
  
