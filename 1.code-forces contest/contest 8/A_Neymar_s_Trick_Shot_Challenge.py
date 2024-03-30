
N, X= list(map(int, input().split()))
L = list(map(int, input().split()))

total_distance = 0
bounce_count = 1

# Calculate the total distance for each bounce and count the bounces within the pitch length
for i in range(N):
    total_distance += L[i]
    if total_distance > X:
        break
    bounce_count += 1

print(bounce_count)