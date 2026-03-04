from langchain_mcp_adapters.client import MultiServerMCPClient

brave_key = None
fmp_key = None

async def init_tools():
    client = MultiServerMCPClient({
        "brave": {
            "transport": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search"],
            "env": {"BRAVE_API_KEY": brave_key}
        },
        "finance": {
            "transport": "stdio",
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-fmp"],
            "env": {"FMP_API_KEY": fmp_key}
        }
    })

    return await client.get_tools()
