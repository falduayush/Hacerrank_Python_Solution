#problem statment
#The provided code stub reads and integer, n , from STDIN. For all non-negative integers i<n , print i^2.
#n=3 Possible list [0,1,2]
# output :
# 0
# 1
# 4

n=int(input("Enter the Number :"))
for i in range(n):
    if(i<n):
        print(i*i)