"""Sceptre MCP Server - CloudFormation management via MCP."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("sceptre-mcp-server")
except PackageNotFoundError:
    __version__ = "0.0.0"
