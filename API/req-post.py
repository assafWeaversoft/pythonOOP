import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "title": "DevOps Automation",
    "body": "API integration is key to modern DevOps workflows.",
    "userId": 1
}
response = requests.post(url, json=data)

if response.status_code == 201:
    print("Resource created successfully:")
    print(response.content)
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")