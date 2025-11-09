import subprocess

#user_input = input("Please enter something: ")
result = subprocess.run(["ping","8.8.8.8"], capture_output=True, text=True)


# Example: Running a command in the background
ping = subprocess.Popen(['ping',"-t", '8.8.8.8'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
ping.terminate()
# The main program continues execution here
print("Subprocess started in the background.")

# Print the output
if result.returncode == 0:
    print(result.stdout)  # Command succeeded
else:
    print(result.stdout)  # Command failed
    print(f"Error: {result.stderr}")