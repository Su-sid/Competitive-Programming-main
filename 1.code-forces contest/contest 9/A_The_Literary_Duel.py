n = int(input())
books = list(map(int, input().split()))
left, right = 0, n - 1
hermione, harry = 0, 0
turn = True
while left <= right:
    if books[left] > books[right]:
        chosen_book = books[left]
        left += 1 
    else:
        chosen_book = books[right]
        right -= 1 

    if turn:
        hermione += chosen_book
    else:
        harry += chosen_book
    turn = not turn

print(hermione, harry)
