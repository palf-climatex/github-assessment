# GitHub Repository Access Checker

Lists teams and users with access to repositories in a GitHub organization.

## Setup

1. Install package:
```bash
uv venv
source .venv/bin/activate
uv pip install -e .
```

2. Create `.env` file:
```
GITHUB_TOKEN=your_github_personal_access_token_here
```

## Usage

```bash
github-access
```

Enter organization name when prompted. Script will display teams and users with access to each repository.

Note: GitHub token requires `repo` and `read:org` scopes. 