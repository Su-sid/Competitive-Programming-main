n, m = list(map(int,input().split()))
store= dict()


for _ in range(n):
    server, ip = list(map(str,input().split()))
    store[ip]= server

# print(store)

for _ in range(m):
    server, ip = list(map(str,input().split()))
    ip=ip[:-1]
    # print(store,ip)
    if ip in store:
        print(f"{server} {ip}; #{store[ip]}")
