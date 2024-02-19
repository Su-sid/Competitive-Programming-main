n, q =list(map(int, input().split()))

words= list(input().split())

#precalculate every single prefix and suffix

prefix_suffix ={}

for wordIndex, word in enumerate(words):
    for i in range(len(words)):
        for j in range(len(words[i])):
            prefix_suffix[(word[:i+1], word[j:])]= wordIndex

for _ in range(q):
    prefix, suffix= input().split()

    print(prefix_suffix.get((prefix, suffix),-1))