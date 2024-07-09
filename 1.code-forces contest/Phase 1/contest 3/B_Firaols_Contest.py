n,m = list(map(int, input().split()))

sequence_questions= list(map(int, input().split()))

pool = {}
number_question = 0

for i in range(m):
    # Adding each quest Ion to the pool
    pool [sequence_questions [i] ] = pool.get(sequence_questions[i],0) + 1
    if pool[sequence_questions [i]]==1:
        number_question+=1

    if number_question== n:
        for i in  range(1, n+1):
            pool[i] -=1

            if pool[i]== 0:
                number_question -=1
        print(1, end ="")

    else:
        print(0, end ="")
    