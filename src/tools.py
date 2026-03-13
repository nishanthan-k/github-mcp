import requests
import json
from dotenv import load_dotenv
import os
from utils.logger import logger

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_URL = "https://api.github.com/user"

def register_tools(mcp):
  
  @mcp.tool()
  def get_profile():
    """Get the authenticated user's GitHub profile information"""
    
    logger.info("GitHub profile request received")

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    try:
      response = requests.get(url=GITHUB_URL, headers=headers)
      
      if response.status_code != 200:
          logger.error(f"GitHub API failed with status {response.status_code}")
          return {
              "error": "Failed to fetch profile",
              "status_code": response.status_code
          }

      data = response.json()
      logger.info(f"Successfully fetched profile for user: {json.dumps(data, indent=4)}")
      
      return data
    except requests.RequestException as e:
      logger.error(f"GitHub API request failed: {e}", exc_info=True)
      return {
          "error": "GitHub API request failed",
          "details": str(e)
      }