# Quick Start Guide

## Installation

Install the package:

```bash
pip install sceptre-mcp-server
```

```bash
uvx --from . sceptre-mcp-server
```

## Configuration

1. Copy the example configuration:
```bash
cp example-mcp-config.json ~/.kiro/settings/mcp.json
```

2. Update the paths in the config to point to your sceptre-mcp-server directory.

3. Set your AWS credentials:
```bash
export AWS_PROFILE=your-profile
export AWS_REGION=us-east-1
```

## Testing

Test the server with a simple Sceptre project:

1. Create a test Sceptre project:
```bash
mkdir -p test-project/config test-project/templates
cd test-project
```

2. Create a simple stack config (`config/test-stack.yaml`):
```yaml
template: test-template.yaml
```

3. Create a simple template (`templates/test-template.yaml`):
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: Test stack
Resources:
  TestBucket:
    Type: AWS::S3::Bucket
```

4. Use the MCP server through your AI assistant:
```
"Validate my test-stack configuration"
"Show me the status of test-stack"
"Generate the CloudFormation template for test-stack"
```

## Available Commands

All tools accept these common parameters:
- `command_path`: Path to stack config (e.g., 'dev/vpc.yaml')
- `project_path`: Path to Sceptre project (default: '.')

### Stack Management
- `sceptre_launch` - Create or update stacks
- `sceptre_create` - Create new stacks
- `sceptre_update` - Update existing stacks
- `sceptre_delete` - Delete stacks

### Information
- `sceptre_status` - Get stack status
- `sceptre_describe` - Get detailed stack information
- `sceptre_validate` - Validate templates
- `sceptre_generate` - Generate CloudFormation templates

### Advanced
- `sceptre_diff` - Compare local vs deployed
- `sceptre_drift_detect` - Detect configuration drift
- `sceptre_drift_show` - Show drift details

## Troubleshooting

### Server won't start
- Check that FastMCP and Sceptre are installed: `pip list | grep -E "fastmcp|sceptre"`
- Verify AWS credentials: `aws sts get-caller-identity`

### Tools not appearing
- Restart your AI assistant
- Check MCP server logs in the Kiro MCP panel
- Verify the config path is correct

### Permission errors
- Ensure your AWS credentials have CloudFormation permissions
- Check IAM policies for required actions

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Explore Sceptre documentation: https://docs.sceptre-project.org/
