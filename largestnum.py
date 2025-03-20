num = [10002, 23, 23, 3466, 45, 6, 5640000]

min = num[0]

for i in num:
    if i < min:
        min = i
    print("current number",i,"mini",min)

print("Min is ",min)