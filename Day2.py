# Move all negative numbers to beginning and positive to end with constant extra space
arr=[2,-12, 11, -13, -5, 6, -7, 5, -3, -6]
i=0
j=len(arr)-1
while(i<j):
    if(arr[i] > arr[j]):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
    else:
        if(arr[j]>0):
            i+=1
            j+=-1
        else:
            i+=1
print(arr)



# Union of two arrays
a=[1 ,2 ,3 ,4 ,5]
b=[1,2,3]
ans=dict()
for i in a:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=0
for i in b:
    if i in ans:
        ans[i]+=1
    else:
        ans[i]=0
print(len(ans))



# Cyclically rotate an array by one
j=len(arr)-1
while(j>0):
    arr[j],arr[j-1]=arr[j-1],arr[j]
    j+=-1
print(arr)



# Kadane's Algorithm
# maxi=-9999999999      
currmax=0
start=0
end=0
for i in range(N):
    currmax+=arr[i]
    if(currmax>maxi):
        maxi=currmax
        end=i
    if currmax<0:           #put this inside else then corrected after taking help
        start=i
        currmax=0
print(start,end)
print(maxi)