import requests
import json
from dotenv import load_dotenv
import os
from utils.logger import logger

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_URL = "https://api.github.com"

def register_tools(mcp):
  
  @mcp.tool()
  def get_profile():
    """Get the authenticated user's GitHub profile information"""
    
    logger.info("GitHub profile request received")

    url = f"{GITHUB_URL}/user"

    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    try:
      response = requests.get(url=url, headers=headers)
      
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

  @mcp.tool()
  def list_repos():
    """Get the authenticated user's GitHub repositories"""
    
    logger.info("GitHub repositories request received")

    url = f"{GITHUB_URL}/user/repos"

    headers = {
      "Authorization": f"Bearer {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
    }

    try:
      response = requests.get(url=url, headers=headers)

      if response.status_code != 200:
        logger.error(f"GitHub API failed with status {response.status_code}")
        return {
          "error": "Failed to fetch repositories",
          "status_code": response.status_code
        }
      data = response.json()
      logger.info(f"Successfully fetched repositories: {json.dumps(data, indent=4)}")

      return data
    except requests.RequestException as e:
      logger.error(f"GitHub API request failed: {e}", exc_info=True)
      return {
        "error": "GitHub API request failed",
        "details": str(e)
      }

  @mcp.tool()
  def get_repo(user_name: str, repo_name: str):
    """Get a specific GitHub repository"""
    
    logger.info(f"GitHub repository request received for: {repo_name}")

    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}"

    headers = {
      "Authorization": f"Bearer {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
    }
    try:  
      response = requests.get(url=url, headers=headers)

      if response.status_code != 200:
        logger.error(f"GitHub API failed with status {response.status_code}")
        return {
          "error": "Failed to fetch repository",
          "status_code": response.status_code
        }
      data = response.json()
      logger.info(f"Successfully fetched repository: {json.dumps(data, indent=4)}")
      return data
    except requests.RequestException as e:
      logger.error(f"GitHub API request failed: {e}", exc_info=True)
      return {
        "error": "GitHub API request failed",
        "details": str(e)
      }

  @mcp.tool()
  def get_repo_issues(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub issues"""
    
    logger.info(f"GitHub issues request received for: {repo_name}")

    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/issues"
    
    headers = {
      "Authorization": f"Bearer {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
    }
    try:
      response = requests.get(url=url, headers=headers)
      
      if response.status_code != 200:
        logger.error(f"GitHub API failed with status {response.status_code}")
        return {
          "error": "Failed to fetch issues",
          "status_code": response.status_code
        }
      data = response.json()
      logger.info(f"Successfully fetched issues: {json.dumps(data, indent=4)}")
      return data
    except requests.RequestException as e:
      logger.error(f"GitHub API request failed: {e}", exc_info=True)
      return {
        "error": "GitHub API request failed",
        "details": str(e)
      }
      
  @mcp.tool()
  def get_repo_pull_requests(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub pull requests"""
    
    logger.info(f"GitHub pull requests request received for: {repo_name}")

    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/pulls"
    
    headers = {
      "Authorization": f"Bearer {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
    }
    try:
      response = requests.get(url=url, headers=headers)
      
      if response.status_code != 200:
        logger.error(f"GitHub API failed with status {response.status_code}") 
        return {
          "error": "Failed to fetch pull requests",
          "status_code": response.status_code
        }
      data = response.json()
      logger.info(f"Successfully fetched pull requests: {json.dumps(data, indent=4)}")
      return data
    except requests.RequestException as e:

      return {
        "error": "GitHub API request failed",
        "details": str(e)
      }

  @mcp.tool()
  def get_repo_commits(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub commits"""
    
    logger.info(f"GitHub commits request received for: {repo_name}")

    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/commits"

    headers = {
      "Authorization": f"Bearer {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
    }
    try:
      response = requests.get(url=url, headers=headers)
      
      if response.status_code != 200:
        logger.error(f"GitHub API failed with status {response.status_code}")
        return {
          "error": "Failed to fetch commits",
          "status_code": response.status_code
        }
      data = response.json()
      logger.info(f"Successfully fetched commits: {json.dumps(data, indent=4)}")
      return data
    except requests.RequestException as e:
      logger.error(f"GitHub API request failed: {e}", exc_info=True)
      return {
        "error": "GitHub API request failed",
        "details": str(e)
      }

  @mcp.tool()
  def get_repo_branches(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub branches"""
    
    logger.info(f"GitHub branches request received for: {repo_name}")

    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/branches"
    
    headers = {
      "Authorization": f"Bearer {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
    }
    try:
      response = requests.get(url=url, headers=headers)
      
      if response.status_code != 200:
        logger.error(f"GitHub API failed with status {response.status_code}")
        return {
          "error": "Failed to fetch branches",
          "status_code": response.status_code
        }
      data = response.json()
      logger.info(f"Successfully fetched branches: {json.dumps(data, indent=4)}")
      return data
    except requests.RequestException as e:
      logger.error(f"GitHub API request failed: {e}", exc_info=True)
      return {
        "error": "GitHub API request failed",
        "details": str(e)
      }

  @mcp.tool()
  def get_repo_tags(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub tags"""
    
    logger.info(f"GitHub tags request received for: {repo_name}")

    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/tags"
    
    headers = {
      "Authorization": f"Bearer {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
    }
    try:
      response = requests.get(url=url, headers=headers)
      
      if response.status_code != 200:
        logger.error(f"GitHub API failed with status {response.status_code}")
        return {
          "error": "Failed to fetch tags",
          "status_code": response.status_code
        }
      data = response.json()
      logger.info(f"Successfully fetched tags: {json.dumps(data, indent=4)}")
      return data
    except requests.RequestException as e:
      logger.error(f"GitHub API request failed: {e}", exc_info=True)
      return {
        "error": "GitHub API request failed",
        "details": str(e)
      }