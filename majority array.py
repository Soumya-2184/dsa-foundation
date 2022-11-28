array=[]
n=int(input("Enter size of array:"))
for i in range(1,n+1):
    ele=int(input("Enter element:"))
    array.append(ele)
print("Array created:")
print(array)
for i in array:
    if array.count(i)>(n/2):
        continue
    print("Majority element:")
    print(i)