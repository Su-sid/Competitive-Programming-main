n, m = map(int, input().split())
ip_command, ip_name = {}, {}

for _ in range(n + m):
    name, ip = input().split()

    if ip[-1] == ';':
        ip_command[name] = ip.replace(';','',1)
    else:
        ip_name[ip] = name

for  command,ip in ip_command.items():
    print(f'{command} {ip}; #{ip_name[ip]}')
    