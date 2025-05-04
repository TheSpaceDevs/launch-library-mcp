# Launch Library MCP

MCP server to provide data for The Space Devs API.

### Installation

use uv to install the package

```bash
pip install uv
uv sync
```

For Claude Desktop uses, edit `claude_desktop_config` to enable MCP server.
See also: https://modelcontextprotocol.io/quickstart/user

```json
{
    "mcpServers": {
        "launch-library": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
                "run",
                "launch_library_mcp", "run-llv2"
            ]
        }
    }
}
```
