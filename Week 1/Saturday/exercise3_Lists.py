#Sum the numbers
x = [1, 2 , 3]
y = sum(x)
print y

#Largest Numbers
x = [8744, 5324, 3246, 2543, 3454, 3421, 3256, 1321, 3225 ,8937, 323, 3232]
y = max(x)  
print y  

#Smallest Numbers
x = [8744, 5324, 3246, 2543, 3454, 3421, 3256, 1321, 3225 ,8937, 7323, 3232]
y = min(x)  
print y  

#Even Numbers
x = [8744, 5324, 3246, 2543, 3454, 3421, 3256, 1321, 3225 ,8937, 7323, 3232]
for index in x:
    if index % 2 == 0:
        print index

#Postive Numbers
x = [8744, -5324, -3246, 2543, 3454, 3421, -3256, 1321, 3225 , -8937, 7323, -3232]
for index in x:
    if index > 0:
        print index

#Postive Numbers II
x = [8744, -5324, -3246, 2543, 3454, 3421, -3256, 1321, 3225 , -8937, 7323, -3232]
def positiveNumbers(list):
    num = []
    for index in list:
        if index > 0:
            num.append(index)
    return num
print positiveNumbers(x)

#Multiply a List
y = 2
x = [8744, -5324, -3246, 2543, 3454, 3421, -3256, 1321, 3225 , -8937, 7323, -3232]
def multiply(list, factor):
    num = []
    for index in list:
        num.append(index * factor)
    return num
print multiply(x, y)

#Multiply Vectors
y = [2, 4, 8]
x = [3, 6, 9]
def multiply(list1, list2):
    num = []
    for index in range(len(list1)):
        num.append(list1[index] * list2[index])
    return num
print multiply(x, y)

#Matrix Addition
y = [[2, 4,], 
    [8, 3]]
x = [[3, 6,], 
    [9, 5]]
def matAdd(list1, list2):
    num = []
    for i in range(len(list1)):
        for j in range(len(list1[0])):
            num.append(list1[i][j] + list2[i][j])
    return num
print matAdd(x, y)



