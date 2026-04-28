import requests
from typing import List, Dict

def fetch_github_profile(username: str) -> Dict:
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=5"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()
            projects = []
            for repo in repos:
                projects.append({
                    "name": repo.get("name"),
                    "description": repo.get("description"),
                    "language": repo.get("language"),
                    "url": repo.get("html_url")
                })
            return {"username": username, "projects": projects}
        else:
            return {"username": username, "projects": [], "error": f"Failed to fetch: {response.status_code}"}
    except Exception as e:
        print(f"Error fetching GitHub profile: {e}")
        return {"username": username, "projects": [], "error": str(e)}
