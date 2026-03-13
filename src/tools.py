import requests
import json
from dotenv import load_dotenv
import os
from utils.logger import logger

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_URL = "https://api.github.com"

def make_github_api_request(url: str, resource_name: str) -> dict:
  """
  Generic GitHub API request handler that encapsulates common logic.
  
  Args:
      url: Full URL for the API endpoint
      resource_name: Name of the resource being fetched (for logging)
  
  Returns:
      API response data or error dict
  """
  headers = {
      "Authorization": f"Bearer {GITHUB_TOKEN}",
      "Accept": "application/vnd.github+json"
  }
  
  logger.info(f"GitHub {resource_name} request received")
  
  try:
      response = requests.get(url=url, headers=headers)
      
      if response.status_code != 200:
          logger.error(f"GitHub API failed with status {response.status_code}")
          return {
              "error": f"Failed to fetch {resource_name}",
              "status_code": response.status_code
          }
      
      data = response.json()
      logger.info(f"Successfully fetched {resource_name}: {json.dumps(data, indent=4)}")
      return data
      
  except requests.RequestException as e:
      logger.error(f"GitHub API request failed: {e}", exc_info=True)
      return {
          "error": "GitHub API request failed",
          "details": str(e)
      }

def register_tools(mcp):
  
  @mcp.tool()
  def get_profile():
    """Get the authenticated user's GitHub profile information"""
    url = f"{GITHUB_URL}/user"
    return make_github_api_request(url, "profile")

  @mcp.tool()
  def list_repos():
    """Get the authenticated user's GitHub repositories"""
    url = f"{GITHUB_URL}/user/repos"
    return make_github_api_request(url, "repositories")

  @mcp.tool()
  def get_repo(user_name: str, repo_name: str):
    """Get a specific GitHub repository"""
    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}"
    return make_github_api_request(url, "repository")

  @mcp.tool()
  def get_repo_issues(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub issues"""
    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/issues"
    return make_github_api_request(url, "issues")
      
  @mcp.tool()
  def get_repo_pull_requests(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub pull requests"""
    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/pulls"
    return make_github_api_request(url, "pull requests")

  @mcp.tool()
  def get_repo_commits(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub commits"""
    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/commits"
    return make_github_api_request(url, "commits")

  @mcp.tool()
  def get_repo_branches(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub branches"""
    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/branches"
    return make_github_api_request(url, "branches")

  @mcp.tool()
  def get_repo_tags(user_name: str, repo_name: str):
    """Get the authenticated user's GitHub tags"""
    url = f"{GITHUB_URL}/repos/{user_name}/{repo_name}/tags"
    return make_github_api_request(url, "tags")