import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

brave_key = os.getenv("BRAVE_API_KEY")
fmp_key = os.getenv("FMP_API_KEY")

async def init_tools():
    brave_server_path = os.path.abspath("mcp-servers/brave-search-mcp-server/dist/index.js")
    client = MultiServerMCPClient({
        "brave": {
            "transport": "stdio",
            "command": "node",
            "args": [brave_server_path],
            "env": {"BRAVE_API_KEY": brave_key}
        }
    })

    return await client.get_tools()
