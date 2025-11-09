config_as_dict = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}


config_as_string = """{
    "host": "localhost",
    "port": 8080,
    "debug": True
}"""


with open("app_config.json", "w") as file:
    file.write(str(config_as_dict))
    file.write(config_as_string)
print("Configuration file generated.")