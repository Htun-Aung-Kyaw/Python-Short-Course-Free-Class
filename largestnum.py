num = [10002, 23, 23, 3466, 45, 6, 5640000]

max = num[0]

for i in num[1:]:
    if i > max:
        max = i
    print("current number",i,"max",max)

print("Max is ",max)

# desire 
# we have a list of numbers
# we want to find the largest number in the list

# [10002, 23, 23, 3466, 45, 6, 5640000,0]
# [2,3,8,9,1,10,4,6,9,10]

# 2 > 2
# 2 > 3 
# 3 > 8
# 8 > 9
# 9 > 1
# 9 > 10
# 10 > 4
# 10 > 6
# 10 > 9
# 10 > 10

