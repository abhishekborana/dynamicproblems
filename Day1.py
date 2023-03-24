#  reverse array
arr=[12,5,34,57,86,23,1]
start=0
end=len(arr)-1
while(start<end):
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end+=-1
print("Reverse of [12,5,34,57,86,23,1] ",arr)

# reverse a string
stringToReverse="testingString"
stringToReverse=stringToReverse[::-1]
print("Reverse of 'testingString' ",stringToReverse)


# maximum and minimum element from with min compraision
arr=[12,5,34,57,86,23,1]
mini,maxi= (arr[0],arr[1]) if arr[0]<arr[1] else (arr[1],arr[0])
for i in range(2,len(arr)):
    mini=min(mini,arr[i])
    maxi=max(maxi,arr[i])
print(mini,maxi)


# Kth smallest element
arr=[7 ,10, 4, 3, 20 ,15]
k=3
arr.sort()
print(k,"th smaller number in",arr,arr[k-1])



# Sort an array of 0s, 1s and 2s
zero,one,two=0,0,0
for i in arr:
    if i ==0:
        zero+=1
    elif i==1:
        one+=1
    else:
        two+=1
# print(zero,one,two)
arr=[0]*zero + [1]*one + [2]*two
# print (arr)
# return arr
for i in range (n):
    if(zero>0):
        arr[i]=0
        zero+=1
    elif(one>0):
        arr[i]=1
        one+=-1
    else:
        arr[i]=2
print(arr)