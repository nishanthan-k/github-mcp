import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

mcp = FastMCP("Github MCP Server")


import requests

@mcp.tool()
def get_profile():
    """Get the authenticated user's GitHub profile information"""

    url = "https://api.github.com/user"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {
            "error": "Failed to fetch profile",
            "status_code": response.status_code
        }

    data = response.json()

    return {
        "username": data["login"],
        "name": data.get("name"),
        "bio": data.get("bio"),
        "followers": data["followers"],
        "following": data["following"],
        "public_repos": data["public_repos"]
    }


def main():
  mcp.run(transport="stdio")

if __name__ == "__main__":
  main()