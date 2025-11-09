try:
    with open("config.yaml", "r") as file:
        content = file.read()
except FileNotFoundError as ex:
    print("\n File not found.")
    print(ex)
