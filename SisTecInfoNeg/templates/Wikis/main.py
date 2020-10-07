import requests

if __name__ == "__main__":
    url='https://www.dolarsi.com/api/api.php?type=valoresprincipales'
    response = requests.get(url)

print(response.content)