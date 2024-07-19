import requests


def get_profile_data(username):
    url = f"https://linkedin-data-api.p.rapidapi.com/?username={username}"
    headers = {
        'x-rapidapi-host': 'linkedin-data-api.p.rapidapi.com',
        'x-rapidapi-key': '74c7bb33f7msh7e0246a5c018f60p1b61eejsnd594badab89f'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return response.text


# Example usage
profile_data = get_profile_data('username')
print(profile_data)
