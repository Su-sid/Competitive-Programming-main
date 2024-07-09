array_shapes= input()
counter=0
maximum= float("-inf")
length = len(array_shapes)

for i in range(length):
    if not array_shapes[i] == 'O':
        maximum= max(maximum, counter)
       
        counter= 0
    else:
        counter+=1
maximum= max(maximum, counter)

print(maximum)
