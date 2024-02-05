#Problem Statment : 
#If  n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5 , print Not Weird
#If n is even and in the inclusive range of 6 to 20 , print Weird
#If n is even and greater than 20 , print Not Weird

#Sample Test Case :
#n=3 // output : Weird
#n=24 // output : Not Weird


n=int(input("Enter the Number :"))

if(n%2 !=0):
    print("Weird")
elif(n%2 == 0 and n>=2 and n<6):
    print("Not Weird")
elif(n%2 == 0 and n>=6 and n<21):
    print("Weird")
elif(n%2 == 0 and n>20):
    print("Not Weird")
else:
    print("Not Weird")