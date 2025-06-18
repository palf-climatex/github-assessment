import json
import os

from dotenv import load_dotenv

from .access import get_repo_access


def main():
    load_dotenv()

    github_token = os.getenv('GITHUB_TOKEN')
    org_name = "climate-x-org"

    access_info = get_repo_access(github_token, org_name)

    with open(f"{org_name}_access.json", "w") as f:
        json.dump(access_info, f, indent=2)
        print(f"\nOutput written to {org_name}_access.json")

if __name__ == '__main__':
    main()
