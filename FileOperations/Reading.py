# Open the log file in read mode

# Open the file in write mode
with open("./server.log", "a") as file:
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")
 file.write("Server nginx restarted successfully.\n")

with open("./python-example.py", "a") as file:
   file.write("print(\"I got written by code\")")


content = ""
with open("./server.log", "r") as file:
    # As long as I am in the With section , the file is opened
    # When Im out of the with section The file is closed
    # Reading All lines at once
    content = file.read()
    print(content)

with open("./server.log", "r") as lines:
    # Reading of all the lines , one by one
    for line in lines:
        print("/n")
        print(line)
        for character in line:
           if character == " ":
              
        print(line.strip()) # Remove extra whitespace
