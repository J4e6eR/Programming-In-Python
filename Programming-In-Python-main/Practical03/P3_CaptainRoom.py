# 20CS021 - Mitren Kadiwala
# GIT Link - https://github.com/MitrenKadiwala/Programming-In-Python.git

print("Input : ")
k = int(input())
input_strng = input()
lst = input_strng.split()

print("Output : ")
for i in range(0, len(lst)):
    if(lst.count(lst[i]) != k):
        print(lst[i])
