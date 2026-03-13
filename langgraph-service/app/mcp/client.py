import sys
from pathlib import Path
from mcp.client.stdio import stdio_client, StdioServerParameters
from mcp.client.session import ClientSession


class MCPClient:
    def __init__(self):
        self.session = None
        self.read = None
        self.write = None
        self.stdio_context = None
        self.session_context = None

    async def connect(self):
        # Resolve project root
        BASE_DIR = Path(__file__).resolve().parents[3]

        server_path = BASE_DIR / "mcp-server" / "src" / "server.py"

        server_params = StdioServerParameters(
            command=sys.executable,
            args=[str(server_path)]
        )

        # Properly enter and store context managers
        self.stdio_context = stdio_client(server_params)
        self.read, self.write = await self.stdio_context.__aenter__()
        
        self.session_context = ClientSession(self.read, self.write)
        self.session = await self.session_context.__aenter__()

        await self.session.initialize()

    async def disconnect(self):
        """Properly cleanup resources"""
        if self.session_context:
            await self.session_context.__aexit__(None, None, None)
        if self.stdio_context:
            await self.stdio_context.__aexit__(None, None, None)
        self.session = None
        self.read = None
        self.write = None

    async def list_tools(self):
        tools = await self.session.list_tools()
        return [tool.name for tool in tools.tools]

    async def call_tool(self, name: str, params: dict):
        result = await self.session.call_tool(name, params)
        return result.content


mcp_client = MCPClient()