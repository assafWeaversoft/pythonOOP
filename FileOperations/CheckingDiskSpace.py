import subprocess

# Run the 'df -h' command to check disk space
result = subprocess.run(["C:\Windows\System32\ping","-c","dir", "-h"], capture_output=True, text=True,)

# Print the output
if result.returncode == 0:
    print(result.stdout)  # Command succeeded
else:
    print(f"Error: {result.stderr}")  # Command failed


import subprocess
result = subprocess.run("dir", shell=True, capture_output=True, text=True)
print(result.stdout)
print("Command executed with return code:", result.returncode)