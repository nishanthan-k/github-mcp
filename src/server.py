import os
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from utils.logger import logger
from tools import register_tools

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

mcp = FastMCP("Github MCP Server")

register_tools(mcp)

def main():
  logger.info("Starting GitHub MCP Server")
  try:
    mcp.run(transport="stdio")
  except Exception as e:
    logger.error(f"MCP Server error: {e}", exc_info=True)
    raise
  finally:
    logger.info("GitHub MCP Server stopped")

if __name__ == "__main__":
  main()