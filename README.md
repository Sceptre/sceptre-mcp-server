# Sceptre MCP Server

A Model Context Protocol (MCP) server for Sceptre that exposes CloudFormation stack management capabilities to AI assistants.

## Architecture

```
┌─────────────────┐
│  AI Assistant   │
│   (e.g., Kiro)  │
└────────┬────────┘
         │ MCP Protocol
         │
┌────────▼────────┐
│  Sceptre MCP    │
│     Server      │
└────────┬────────┘
         │
┌────────▼────────┐
│    Sceptre      │
│   Python API    │
└────────┬────────┘
         │
┌────────▼────────--┐
│ AWS CloudFormation│
└─────────────────--┘
```

## Features

- Stack lifecycle management (launch, create, update, delete)
- Stack status and information querying
- Template validation and generation
- Drift detection
- Diff between local and deployed stacks
- Built with FastMCP for easy development

## Installation

```bash
# Install from source
cd sceptre-mcp-server
pip install -e .
```

Or with uv:

```bash
uvx --from . sceptre-mcp-server
```

## Configuration

Add to your MCP settings file (`.kiro/settings/mcp.json` or `~/.kiro/settings/mcp.json`):

```json
{
  "mcpServers": {
    "sceptre": {
      "command": "uvx",
      "args": ["--from", "/path/to/sceptre-mcp-server", "sceptre-mcp-server"],
      "env": {
        "AWS_PROFILE": "default",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

Or if installed globally:

```json
{
  "mcpServers": {
    "sceptre": {
      "command": "sceptre-mcp-server",
      "env": {
        "AWS_PROFILE": "default",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

## Available Tools

### Stack Lifecycle
- `sceptre_launch` - Launch (create or update) a stack or stack group
- `sceptre_create` - Create a new stack
- `sceptre_update` - Update an existing stack
- `sceptre_delete` - Delete a stack or stack group

### Information & Querying
- `sceptre_status` - Get the status of stacks
- `sceptre_describe` - Describe stack resources, outputs, or events

### Template Operations
- `sceptre_validate` - Validate CloudFormation templates
- `sceptre_generate` - Generate the CloudFormation template for a stack

### Change Management
- `sceptre_diff` - Show differences between deployed stack and local template

### Drift Detection
- `sceptre_drift_detect` - Detect drift in a stack
- `sceptre_drift_show` - Show drift details for a stack

## Usage Examples

### With AI Assistant

```
User: "Launch my dev VPC stack"

AI uses: sceptre_launch(command_path="dev/vpc.yaml", project_path=".")

Result: Stack dev-vpc launched successfully in CREATE_COMPLETE state.
```

```
User: "What's the status of my production stacks?"

AI uses: sceptre_status(command_path="prod", project_path=".")

Result: Shows status of all stacks in the prod environment.
```

```
User: "Check if my database stack has drifted"

AI uses: sceptre_drift_detect(command_path="prod/database.yaml", project_path=".")

Result: Shows drift detection results with any configuration changes.
```

## Development

```bash
# Install dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run the server directly
python -m sceptre_mcp_server.server
```

## Requirements

- Python 3.10+
- Sceptre 4.0+
- FastMCP 0.2+
- AWS credentials configured

## License

See LICENSE file.
A Model Context Protocol server for Sceptre
