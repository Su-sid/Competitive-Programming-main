s=input()
target = "hello"
target_index = 0
ans= 'NO'
for char in s:
    if char == target[target_index]:
        target_index += 1
        if target_index == len(target):
            ans= "YES"
            break
    # print("NO")
    # break
print(ans)
# print(can_say_hello(input()))  

