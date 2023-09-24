def replace_hosts_file_with_input_file(input_file_path):
    try:
        hosts_file_path = 'C:\Windows\system32\drivers\etc\hosts'

        with open(input_file_path, 'r') as input_file:
            input_content = input_file.read()

        with open(hosts_file_path, 'w') as hosts_file:
            hosts_file.write(input_content)

        print(f'Successfully replaced the content of {hosts_file_path} with the content from {input_file_path}.')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    input_file_path = 'network\hosts.txt'
    replace_hosts_file_with_input_file(input_file_path)

# import sys

# def replace_hosts_file_with_input_file(input_file_path):
#     try:
#         # Specify the correct hosts file path on Windows
#         hosts_file_path = r'C:\Windows\System32\drivers\etc\hosts'

#         # Read the content from the specified input file
#         with open(input_file_path, 'r') as input_file:
#             input_content = input_file.read()

#         # Write the input file content to the hosts file, overwriting its content
#         with open(hosts_file_path, 'w') as hosts_file:
#             hosts_file.write(input_content)

#         print(f'Successfully replaced the content of {hosts_file_path} with the content from {input_file_path}.')
#     except Exception as e:
#         print(f'Error: {e}')

# if __name__ == '__main__':
#     if len(sys.argv) != 2:
#         print("Usage: python network_reverser.py <input_file_path>")
#     else:
#         input_file_path = sys.argv[1]
#         replace_hosts_file_with_input_file(input_file_path)

# def read_input_file_path_from_config():
#     try:
#         with open('config.txt', 'r') as config_file:
#             return config_file.readline().strip()
#     except FileNotFoundError:
#         print("Error: Configuration file 'config.txt' not found.")
#         return None

# def replace_hosts_file_with_input_file():
#     try:
#         # Specify the correct hosts file path on Windows
#         hosts_file_path = r'C:\Windows\System32\drivers\etc\hosts'

#         # Read the input file path from the configuration file
#         input_file_path = read_input_file_path_from_config()

#         if input_file_path:
#             # Read the content from the specified input file
#             with open(input_file_path, 'r') as input_file:
#                 input_content = input_file.read()

#             # Write the input file content to the hosts file, overwriting its content
#             with open(hosts_file_path, 'w') as hosts_file:
#                 hosts_file.write(input_content)

#             print(f'Successfully replaced the content of {hosts_file_path} with the content from {input_file_path}.')
#     except FileNotFoundError:
#         print(f'Error: The specified file {input_file_path} was not found.')
#     except Exception as e:
#         print(f'Error: {e}')

# if __name__ == '__main__':
#     replace_hosts_file_with_input_file()
