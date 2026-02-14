#!/usr/bin/env python3
"""
Sceptre MCP Server

Exposes Sceptre CloudFormation management capabilities via MCP using FastMCP.
"""

import json
from pathlib import Path
from typing import Optional

from fastmcp import FastMCP
from sceptre.context import SceptreContext
from sceptre.plan.plan import SceptrePlan

# Initialize FastMCP server
mcp = FastMCP("sceptre-mcp-server")


def create_context(
    command_path: str, project_path: str = ".", **kwargs
) -> SceptreContext:
    """Create a Sceptre context."""
    return SceptreContext(
        command_path=command_path, project_path=Path(project_path).resolve(), **kwargs
    )


@mcp.tool()
def sceptre_launch(
    command_path: str,
    project_path: str = ".",
    yes: bool = False,
    prune: bool = False,
    ignore_dependencies: bool = False,
    max_concurrency: Optional[int] = None,
) -> str:
    """
    Launch (create or update) a stack or stack group.

    Args:
        command_path: Path to stack config (e.g., 'dev/vpc.yaml' or 'dev' for group)
        project_path: Path to Sceptre project directory (default: '.')
        yes: Skip confirmation prompts (default: False)
        prune: Delete obsolete stacks (default: False)
        ignore_dependencies: Ignore stack dependencies (default: False)
        max_concurrency: Maximum number of concurrent operations

    Returns:
        JSON string with launch results
    """
    try:
        context = create_context(
            command_path=command_path,
            project_path=project_path,
            ignore_dependencies=ignore_dependencies,
        )

        plan = SceptrePlan(context)
        responses = plan.launch(prune=prune)

        result = {
            "status": "success",
            "stacks": {
                str(stack): str(response) for stack, response in responses.items()
            },
            "message": f"Successfully launched {command_path}",
        }

        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_create(
    command_path: str,
    project_path: str = ".",
    yes: bool = False,
    ignore_dependencies: bool = False,
) -> str:
    """
    Create a new stack.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')
        yes: Skip confirmation prompts (default: False)
        ignore_dependencies: Ignore stack dependencies (default: False)

    Returns:
        JSON string with creation results
    """
    try:
        context = create_context(
            command_path=command_path,
            project_path=project_path,
            ignore_dependencies=ignore_dependencies,
        )

        plan = SceptrePlan(context)
        responses = plan.create()

        result = {
            "status": "success",
            "stacks": {
                str(stack): str(response) for stack, response in responses.items()
            },
            "message": f"Successfully created {command_path}",
        }

        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_update(
    command_path: str,
    project_path: str = ".",
    yes: bool = False,
    ignore_dependencies: bool = False,
) -> str:
    """
    Update an existing stack.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')
        yes: Skip confirmation prompts (default: False)
        ignore_dependencies: Ignore stack dependencies (default: False)

    Returns:
        JSON string with update results
    """
    try:
        context = create_context(
            command_path=command_path,
            project_path=project_path,
            ignore_dependencies=ignore_dependencies,
        )

        plan = SceptrePlan(context)
        responses = plan.update()

        result = {
            "status": "success",
            "stacks": {
                str(stack): str(response) for stack, response in responses.items()
            },
            "message": f"Successfully updated {command_path}",
        }

        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_delete(
    command_path: str,
    project_path: str = ".",
    yes: bool = False,
    ignore_dependencies: bool = False,
) -> str:
    """
    Delete a stack or stack group.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')
        yes: Skip confirmation prompts (default: False)
        ignore_dependencies: Ignore stack dependencies (default: False)

    Returns:
        JSON string with deletion results
    """
    try:
        context = create_context(
            command_path=command_path,
            project_path=project_path,
            ignore_dependencies=ignore_dependencies,
        )

        plan = SceptrePlan(context)
        responses = plan.delete()

        result = {
            "status": "success",
            "stacks": {
                str(stack): str(response) for stack, response in responses.items()
            },
            "message": f"Successfully deleted {command_path}",
        }

        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_status(
    command_path: str, project_path: str = ".", output_format: str = "json"
) -> str:
    """
    Get the status of stacks.

    Args:
        command_path: Path to stack or group
        project_path: Path to Sceptre project directory (default: '.')
        output_format: Output format: 'text', 'json', or 'yaml' (default: 'json')

    Returns:
        JSON string with stack statuses
    """
    try:
        context = create_context(command_path=command_path, project_path=project_path)

        plan = SceptrePlan(context)
        statuses = plan.get_status()

        result = {str(stack): str(status) for stack, status in statuses.items()}

        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_describe(
    command_path: str,
    project_path: str = ".",
    describe_type: str = "stack",
    output_format: str = "json",
) -> str:
    """
    Describe stack resources, outputs, or events.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')
        describe_type: Type to describe: 'resources', 'outputs', 'policy', or 'stack' (default: 'stack')
        output_format: Output format: 'text', 'json', or 'yaml' (default: 'json')

    Returns:
        JSON string with stack description
    """
    try:
        context = create_context(command_path=command_path, project_path=project_path)

        plan = SceptrePlan(context)

        if describe_type == "outputs":
            responses = plan.describe_outputs()
        elif describe_type == "resources":
            responses = plan.describe_resources()
        elif describe_type == "policy":
            responses = plan.get_policy()
        else:  # stack
            responses = plan.describe()

        result = {str(stack): response for stack, response in responses.items()}

        return json.dumps(result, indent=2, default=str)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_validate(command_path: str, project_path: str = ".") -> str:
    """
    Validate CloudFormation templates.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')

    Returns:
        JSON string with validation results
    """
    try:
        context = create_context(command_path=command_path, project_path=project_path)

        plan = SceptrePlan(context)
        responses = plan.validate()

        result = {
            "valid": True,
            "stacks": {str(stack): response for stack, response in responses.items()},
            "message": "Templates are valid",
        }

        return json.dumps(result, indent=2, default=str)

    except Exception as e:
        return json.dumps(
            {
                "status": "error",
                "valid": False,
                "error": str(e),
                "type": type(e).__name__,
            },
            indent=2,
        )


@mcp.tool()
def sceptre_generate(
    command_path: str, project_path: str = ".", output_format: str = "yaml"
) -> str:
    """
    Generate the CloudFormation template for a stack.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')
        output_format: Output format: 'json' or 'yaml' (default: 'yaml')

    Returns:
        JSON string with generated template
    """
    try:
        context = create_context(command_path=command_path, project_path=project_path)

        plan = SceptrePlan(context)
        responses = plan.generate()

        result = {
            "templates": {
                str(stack): template for stack, template in responses.items()
            },
            "format": output_format,
        }

        return json.dumps(result, indent=2)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_diff(
    command_path: str, project_path: str = ".", diff_type: str = "deepdiff"
) -> str:
    """
    Show differences between deployed stack and local template.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')
        diff_type: Diff type: 'deepdiff' or 'difflib' (default: 'deepdiff')

    Returns:
        JSON string with diff results
    """
    try:
        context = create_context(command_path=command_path, project_path=project_path)

        plan = SceptrePlan(context)
        responses = plan.diff()

        result = {
            "diffs": {str(stack): diff for stack, diff in responses.items()},
            "has_changes": bool(responses),
        }

        return json.dumps(result, indent=2, default=str)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_drift_detect(command_path: str, project_path: str = ".") -> str:
    """
    Detect drift in a stack.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')

    Returns:
        JSON string with drift detection results
    """
    try:
        context = create_context(command_path=command_path, project_path=project_path)

        plan = SceptrePlan(context)
        responses = plan.drift_detect()

        result = {
            "drift_results": {
                str(stack): response for stack, response in responses.items()
            }
        }

        return json.dumps(result, indent=2, default=str)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


@mcp.tool()
def sceptre_drift_show(
    command_path: str, project_path: str = ".", output_format: str = "json"
) -> str:
    """
    Show drift details for a stack.

    Args:
        command_path: Path to stack config
        project_path: Path to Sceptre project directory (default: '.')
        output_format: Output format: 'text', 'json', or 'yaml' (default: 'json')

    Returns:
        JSON string with drift details
    """
    try:
        context = create_context(command_path=command_path, project_path=project_path)

        plan = SceptrePlan(context)
        responses = plan.drift_show()

        result = {
            "drift_details": {
                str(stack): response for stack, response in responses.items()
            }
        }

        return json.dumps(result, indent=2, default=str)

    except Exception as e:
        return json.dumps(
            {"status": "error", "error": str(e), "type": type(e).__name__}, indent=2
        )


def main():
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
