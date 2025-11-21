import requests

class JSONPlaceholderClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()

    def get_posts(self, limit=None):
       
        url = f"{self.BASE_URL}/posts"
        response = self.session.get(url)

        if response.status_code == 200:
            posts = response.json()
            return posts[:limit] if limit else posts
        else:
            raise Exception(f"GET request failed with status {response.status_code}")

    def create_post(self, title, body, user_id):
       
        url = f"{self.BASE_URL}/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = self.session.post(url, json=payload)

        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"POST request failed with status {response.status_code}")



if __name__ == "__main__":
    client = JSONPlaceholderClient()

    print("Fetching first 5 posts:\n")
    posts = client.get_posts(limit=5)
    for p in posts:
        print(f"ID: {p['id']} - Title: {p['title']}")

    print("\nCreating a new post:\n")
    new_post = client.create_post(
        title="My New Post",
        body="This is the content of the post.",
        user_id=1
    )
    print(new_post)
