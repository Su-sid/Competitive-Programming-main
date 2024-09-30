from collections import defaultdict

store = defaultdict(int)

for _ in range(int(input())):

    word = input()

    store[word]+=1

    if store[word]>1:
        print(f"{word}{store[word]-1}")
    else:
        print('OK')
