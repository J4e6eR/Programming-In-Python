# 20CS021 - Mitren Kadiwala
# GIT Link - https://github.com/MitrenKadiwala/Programming-In-Python.git

input_str = input("Input String : ")

# print(str.swapcase()) ## Shortcut

swap_elements = "" # For storing ans

for i in range(len(input_str)):
    if(input_str[i].islower()):
        swap_elements += input_str[i].upper()
    elif(input_str[i].isupper()):
        swap_elements += input_str[i].lower()
    else:
        swap_elements += input_str[i]

print()
print("Output: ")
print(swap_elements)