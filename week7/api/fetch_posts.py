import requests


def get_request():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        get_first_five_posts(data)
    else:
        print("Failed to fetch user data with status code: ", response.status_code)

    response.json()


def get_first_five_posts(data):
    first_five_posts = data[:5]
    for i, post in enumerate(first_five_posts, start=1):
        print(f"Post {i}:")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}")
        print("-" * 40)

