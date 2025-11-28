# Sysrev API Integration Tests

This directory contains integration tests for the Sysrev OpenAPI client.
---

## Prerequisites

Before running these tests, you need to:

1. Have a Sysrev account with API access
2. Create a test project in Sysrev
3. Generate an API key
4. Set up the required environment variables

## Environment Setup

The tests require the following environment variables:

### Required Variables

- `SYSREV_API_KEY` - Your Sysrev API authentication token
- `SYSREV_TEST_PROJECT_ID` - The ID of the project to use for testing (e.g., `proj_12345`)

### Optional Variables

- `SYSREV_API_URL` - Base URL for the Sysrev API (defaults to `https://sysrev.com`)

### Setting Environment Variables

#### Using the `secrets` file (Recommended)

The project is configured to load environment variables from a `secrets` file in the root directory. This file is created automatically by the `.envrc` script if it doesn't exist.

1. Create or edit the `secrets` file in the project root:

```bash
SYSREV_API_KEY=your_api_key_here
SYSREV_TEST_PROJECT_ID=proj_12345
```

2. If using direnv, the variables will be loaded automatically:

```bash
direnv allow
```

#### Using manual export

Alternatively, you can export the variables manually:

```bash
export SYSREV_API_KEY="your_api_key_here"
export SYSREV_TEST_PROJECT_ID="proj_12345"
```
---

## Test Coverage

The test suite covers the following scenarios:

1. **test_create_source** - Verifies that a project source can be created successfully
2. **test_add_article_with_json_full_text** - Tests adding an article with JSON full text content
3. **test_add_article_with_pdf_full_text** - Tests adding an article with PDF full text content
4. **test_add_article_with_multiple_full_texts** - Tests adding an article with both JSON and PDF full texts

### Run all tests in the file

```bash
uv run pytest test/components/sysrev_client/spec/test_article_full_text.py
```

### Run a specific test

```bash
# Test creating a source
uv run pytest test/components/sysrev_client/spec/test_article_full_text.py::test_create_source

# Test adding article with JSON full text
uv run pytest test/components/sysrev_client/spec/test_article_full_text.py::test_add_article_with_json_full_text

# Test adding article with PDF full text
uv run pytest test/components/sysrev_client/spec/test_article_full_text.py::test_add_article_with_pdf_full_text

# Test adding article with multiple full texts
uv run pytest test/components/sysrev_client/spec/test_article_full_text.py::test_add_article_with_multiple_full_texts
```

### Run with verbose output

```bash
uv run pytest test/components/sysrev_client/spec/test_article_full_text.py -v
```

### Run with detailed output and print statements

```bash
uv run pytest test/components/sysrev_client/spec/test_article_full_text.py -vv -s
```


## Troubleshooting

### Tests are skipped

- **Issue**: Tests show as "SKIPPED" in the output
- **Solution**: Ensure `SYSREV_API_KEY` and `SYSREV_TEST_PROJECT_ID` environment variables are set

### Authentication errors

- **Issue**: Tests fail with 401 or 403 errors
- **Solution**: Verify your API key is correct and has the necessary permissions

### Source creation fails

- **Issue**: The `source_id` fixture fails
- **Solution**:
  - Check that the project ID is correct
  - Ensure your API key has permissions to create sources in the project
  - Verify the project exists and is accessible

### PDF-related test failures

- **Issue**: Tests with PDF full text fail
- **Solution**: The test generates a minimal valid PDF. If it fails, ensure the base64 encoding is working correctly