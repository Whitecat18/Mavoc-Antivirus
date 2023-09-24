import bcrypt
import subprocess

print("""
┌┬┐┌─┐┬  ┬┌─┐┌─┐  ┌─┐┌┐┌┌┬┐┬┬  ┬┬┬─┐┬ ┬┌─┐
│││├─┤└┐┌┘│ ││    ├─┤│││ │ │└┐┌┘│├┬┘│ │└─┐
┴ ┴┴ ┴ └┘ └─┘└─┘  ┴ ┴┘└┘ ┴ ┴ └┘ ┴┴└─└─┘└─┘
                               ~ By Smukx
      """)
def verify_password(hashed_password, input_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

try:
    with open("core/log_auth.txt", "rb") as file:
        stored_hashed_password = file.read()
except FileNotFoundError:
    print("Password file not found. Please set up authentication.")
    exit()

entered_password = input("Enter your password: ")

if verify_password(stored_hashed_password, entered_password):
    print("Password is correct. Logging in...")

    script_path = r'mavoc.ps1'

    subprocess.run(["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", script_path], shell=True)

else:
    print("Incorrect password. Exiting...")







#stored_password = b'$2a$10$RWv/Mt4so0U9Fj8YYbr/oeFNRfLO.5u0wG5y4qXiY/uI./RH1f0ym'  # Replace with your stored hashed password
