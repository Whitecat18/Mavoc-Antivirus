def add_domains_from_file_to_hosts_file(file_path):
    try:
        hosts_file_path = 'C:\Windows\system32\drivers\etc\hosts'

        redirect_ip = '0.0.0.0'

        with open(hosts_file_path, 'a') as hosts_file:
            with open(file_path, 'r') as domains_file:
                for line in domains_file:
                    domain = line.strip()  
                    if domain:  
                        hosts_file.write(f'{redirect_ip} {domain}\n')

        print(f'Successfully added domains from "{file_path}" to the hosts file.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    file_path = 'network\\blacklist.txt'  
    add_domains_from_file_to_hosts_file(file_path)
