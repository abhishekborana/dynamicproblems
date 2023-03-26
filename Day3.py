# Minimize the Heights II https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1
k=5
n=10
arr=[2,6,3,4,7,2,10,3,2,1]
arr.sort()
res=arr[-1]- arr[0]
print(arr)
for i in range(1,n):
    big=max(arr[i-1]+k,arr[-1]-k)
    print(big,"=",arr[i-1]+k,arr[-1]-k)
    small=min(arr[i]-k,arr[0]+k)
    print(small,"=",arr[i]-k,arr[0]+k)
    if small<0:
        continue
    res=min(res,big-small)
print(res)



# Minimum number of jumps
arr=[2,3,1,1,4]
arr=[1,2,2,3,6,1]
jump=0
position=arr[0]
destination=arr[0]
for i in range(1,len(arr)):
    
    print(destination,arr[i]+i)
    destination=max(destination,arr[i]+i)
    
    if(position==i):
        position=destination
        jump+=1

def minJumps(arr, n):
    if(arr[0]==0):
        return -1
    des=arr[0]
    steps=arr[0]
    jumps=1
    for i in range(1,n):
        if i==n-1:
            return jumps
        des=max(des,arr[i]+i)
        steps+=-1
        if steps==0:
            jumps+=1
            if i>=des:
                return -1
            steps=des-i
    return jumps 
    



# Merge 2 sorted arrays without using Extra space.

arr1=[16,18,56,82]
arr2=[6,12,18,26,54,63]
res=[]
i=0
j=0
while(i<len(arr1) and j<len(arr2)):
    if(arr1[i]<arr2[j]):
        res.append(arr1[i])
        i+=1
    elif(arr1[i]>arr2[j]):
        res.append(arr2[j])
        j+=1
    else:
        res.append(arr2[j])
        res.append(arr1[i])
        i+=1
        j+=1
while(i<len(arr1)):
    res.append(arr1[i])
    i+=1
while(j<len(arr2)):
    res.append(arr2[j])
    j+=1
print(res)