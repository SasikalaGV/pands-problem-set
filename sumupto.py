#Sasikala Varatharajan - G00376470
#Program to calculate sum of numbers from 1 to the number entered

#Get input from User
n=int(input("Please enter a positive integer "))

#Create an empty intergar called Sum and set initialize it to zero
sum = 0

if n > 0:
    #Create a For loop and add all numbers starting from 1 upto the number entered
    for num in range (0, n+1, 1):
        sum = sum + num
    #Print the output value    
    print ("Sum of numbers 1 to", n, "is: ", sum)
else:
    print ("Oops, It is a negative number") 