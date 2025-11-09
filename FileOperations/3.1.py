import shutil
config = """server {
    location / {
        root /data/www;
    }

    location /images/ {
        root /data;
    }
}"""

with open("nginx.conf", "w") as file:
    file.write(config)
print("Configuration file generated.")

# Back up the configuration file
shutil.copy("nginx.conf", "nginx.conf.bak")
print("Backup created: nginx.conf.bak")
