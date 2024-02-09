#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  n scores. Store them in a list and find the score of the runner-up.
#Input 
#5
#2 3 6 6 5
#Output 
#5


print("Enter the Number :")
n = int(input())
arr = map(int, input().split())
arr2=list(arr)
output = []
for x in arr2:
    if x not in output:
        output.append(x)
output.sort()

print("Runner Up Value :")
print (output[-2])