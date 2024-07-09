#take length of array
n = int(input().strip())
arr = list(map(int, input().split()))

negative=list()
positive=list()
zero=list()

for i in arr:

    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)

    else:
        zero.append(i)


if len(negative)%2 == 0:
    positive.append(negative.pop())

if not positive:

   positive.append(negative.pop())
   positive.append(negative.pop())

eval_negative=' '.join( map(str,negative))
eval_positive=' '.join( map(str,positive))
eval_zero= ' '.join(map(str, zero))


print(f'{len(negative)} {eval_negative}' )
print(f'{len(positive)} {eval_positive}' )
print(f'{len(zero)} {eval_zero}')

