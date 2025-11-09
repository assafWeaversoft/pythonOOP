import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    print("Response Data:")
    print(response.content)  # Parse JSON response
    strval = response.content 
    objval = response.json()
    userid = objval["userId"]
    print(f"Server provided userID is : { userid}") 
else:
    print(f"Request failed with status code {response.status_code}")