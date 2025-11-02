# Open the log file in read mode

# Open the file in write mode
with open("./server.log", "w") as file:
 file.write("Server nginx restarted successfully.\n")

content = ""
with open("./server.log", "r") as file:
    # As long as I am in the With section , the file is opened
    # When Im out of the with section The file is closed
    # Reading All lines at once
    content = file.read()
    print(content)

with open("./server.log", "r") as file:
    # Reading of all the lines , one by one
    for line in file:
        print("/n")
        print(line)
        print(line.strip()) # Remove extra whitespace
