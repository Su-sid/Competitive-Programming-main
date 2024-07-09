# GET COUNT OF VALUES
def getCount(string, ch):
    count=0
    for i in range(len(string)):
         if string[i] != ch:
              count+=1
    return count 

# RECURSIVE CONDITION     
def countShiftsFunc(string,n,c):
    if len(string)==1:
        if string == c:
            return 0
        else:
            return 1
                
    half= n//2

    left_s= string[:half]
    right_s= string[half:]
    left = getCount(left_s,c)+ countShiftsFunc(right_s,half,chr(ord(c)+1))
    right = getCount(right_s,c)+ countShiftsFunc(left_s,half,chr(ord(c)+1))

    return min(left,right)

# Main Func
tests= int(input().strip())
for _ in range(tests):
    n = int(input().strip())
    s= input().strip()
    print(countShiftsFunc(s,n, c='a'))
