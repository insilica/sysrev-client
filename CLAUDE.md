# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Python Polylith** monorepo for building the Sysrev client library and related components.

- **Namespace**: `sysrev_client` (see `workspace.toml`)
- **Structure Theme**: "loose" (Polylith structure)
- **Build Tool**: `uv`
- **Build Backend**: hatchling with hatch-polylith-bricks plugin
- **Python Version**: >=3.11

## Architecture

### Polylith Structure

This project follows the Polylith architecture pattern:

- **Components** (`components/`): Reusable implementation units organized by namespace
  - Example: `components/sysrev_client/api/` contains API client implementation
  - Components contain the actual business logic and implementation

- **Bases** (`bases/`): Public API layers that expose components
  - Example: `bases/sysrev_client/lib/` re-exports from components to create a clean public API
  - Bases use `from sysrev_client.<component> import *` to expose component functionality
  - The `__all__` pattern is used to control public exports

- **Projects** (`projects/`): Packaging configurations for distributable artifacts
  - Example: `projects/sysrev_client_lib/` packages the library
  - Each project's `pyproject.toml` maps bases and components using `[tool.polylith.bricks]`
  - Projects define dependencies and build configuration

- **Tests** (`test/`): Mirror structure of bases/components
  - `test/bases/` contains tests for base modules
  - `test/components/` contains tests for component modules

### Development Flow

When adding new functionality:
1. Implementation goes in `components/`
2. Public API wiring goes in `bases/`
3. Packaging configuration goes in `projects/`

## Common Commands

### Environment Setup

```bash
# Install dependencies and activate environment (using Nix + direnv)
direnv allow

# Or manually with uv
uv sync
```

### Creating Polylith Bricks

```bash
# Create a new base
uv run poly create base --name my_base

# Create a new component
uv run poly create component --name my_component
```

### Building

```bash
# Build a specific project
uv build projects/sysrev_client_lib

# The build system uses hatchling with hatch-polylith-bricks plugin
# which automatically includes the bricks defined in the project's pyproject.toml
```

### Testing

```bash
# Run all tests
uv run pytest

# Run tests for a specific component
uv run pytest test/components/sysrev_client/api/

# Run tests for a specific base
uv run pytest test/bases/sysrev_client/lib/

# Run a single test file
uv run pytest test/components/sysrev_client/api/test_core.py

# Run a specific test
uv run pytest test/components/sysrev_client/api/test_core.py::test_sample
```

### Polylith CLI

```bash
# View workspace info
uv run poly info

# Check workspace health
uv run poly check
```

## Project Configuration

### Workspace (workspace.toml)

- Namespace: `sysrev_client`
- Git tag patterns configured for stable releases (`stable-*`) and versions (`v[0-9]*`)
- Tests are enabled in the Polylith configuration

### Project Structure (pyproject.toml in projects/)

Each project maps bricks using the `[tool.polylith.bricks]` section:

```toml
[tool.polylith.bricks]
"../../bases/sysrev_client/lib" = "sysrev_client/lib"
"../../components/sysrev_client/api" = "sysrev_client/api"
```

This maps source directories to their package structure in the built distribution.
