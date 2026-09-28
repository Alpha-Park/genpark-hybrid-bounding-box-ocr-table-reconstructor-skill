# genpark-ocr-table

Group supplied OCR text boxes into left-aligned table rows and columns. No image OCR is performed.

Python 3.9+; standard library runtime; MIT license.

## Install and run

Download `genpark-ocr-table.mcpb` from [GitHub Releases](https://github.com/Alpha-Park/genpark-hybrid-bounding-box-ocr-table-reconstructor-skill/releases/tag/v1.0.1) and install with an MCPB-compatible client. Python must be installed and available as `python`.

Alternatively clone this repository and configure an MCP stdio server with command `python` and arguments containing the absolute path to `mcp_server.py`.

[Smithery listing](https://smithery.ai/servers/krispang1020/genpark-ocr-table)

## Tools

- `reconstruct_table_grid`
- `format_to_markdown`
- `run_benchmark_table_reconstruction`

Run `python -m unittest discover -s tests` for regression checks. The official MCP SDK integration check uses the development dependency `mcp`: `python tests/check_mcp.py`.

## Limitations

These are deterministic helpers operating on supplied structured data, not machine-learning models. Input and output remain in the local process. No hosted endpoint, automatic file access or network access is required. State lasts only for the current process. Benchmark tools run synthetic examples in isolated state; their status is not a production-quality certification.

Rows use an 8-pixel vertical tolerance; columns use left-edge alignment with a 20-pixel tolerance. Merged cells, rotated text and centered layouts are not supported.
