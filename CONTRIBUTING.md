# Contributing

Thank you for your interest in contributing to TransBook OSS.

## Development Setup

```bash
python -m pip install -e ".[dev]"

Run tests:

pytest

Run lint:

ruff check .
Contribution Rules

Please follow these rules:

Do not commit copyrighted book samples.
Do not commit real user-uploaded documents.
Do not commit .env files or API keys.
Keep providers mockable.
Keep tests deterministic.
Do not require external OCR or translation APIs for default tests.
Pull Request Checklist

Before opening a pull request:

 Tests pass
 Lint passes
 No private files are included
 No real book images are included
 README or docs are updated if behavior changed