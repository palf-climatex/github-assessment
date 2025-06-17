import json
import os

from dotenv import load_dotenv

from .access import get_repo_access


def main():
    load_dotenv()

    github_token = os.getenv('GITHUB_TOKEN')
    org_name = "climate-x-org"

    access_info = get_repo_access(github_token, org_name)
    print(access_info)

    with open(f"{org_name}_access.json", "w") as f:
        json.dump(access_info, f, indent=2)
        print(f"\nOutput written to {org_name}_access.json")

    for repo, access_list in access_info.items():
        print(f'\nRepository: {repo}')

        for access_type, name in access_list:
            print(f'  - {access_type}: {name}')

if __name__ == '__main__':
    main()
