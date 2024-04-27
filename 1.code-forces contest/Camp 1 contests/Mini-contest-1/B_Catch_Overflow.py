
# def calculate(commands):
MAX_X = 2**32 - 1
stack = [1] 
x = 0 

tests= int(input())

for i in range(tests):
   
    command= input()

    if command.startswith("add") and x< MAX_X:
        x += stack[-1]

    elif command.startswith("for"):
        n = int(command.split()[1])
        product = stack[-1] * n
        if product > MAX_X:
            product = MAX_X + 1  
        stack.append(product)
    
    elif command.startswith("end"):
        stack.pop()
   
if x <= MAX_X:
   print(x)
else :
    print("OVERFLOW!!!")
    