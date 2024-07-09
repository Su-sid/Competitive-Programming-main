from collections import defaultdict

tests= int(input())

t_required = {chr(i): i - 64 for i in range(65, 91)}
# print(t_required)

for  test in range(tests):
    n=int(input())
    log= input()
    
    t_spent = defaultdict(int)
    solved_problems = 0
    
    for problem in log:
      
        t_spent[problem] += 1

       
              
        if t_spent[problem] == t_required[problem]:
          
            solved_problems+=1
        print(t_spent )#
    # print(t_spent)

    # print(solved_problems)

