from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List

from github import Github
from tqdm import tqdm


def get_repo_access(
    github_token: str, org_name: str
) -> Dict[str, List[Dict[str, str]]]:
    g: Github = Github(github_token)

    org = g.get_organization(org_name)

    repos = org.get_repos()

    access_info: Dict[str, List[Dict[str, str]]] = {}

    pbar: tqdm = tqdm(
        repos,
        total=repos.totalCount if hasattr(repos, "totalCount") else None,
    )

    def process_repo(repo):
        repo_name: str = repo.name
        pbar.set_description(f"Processing {repo_name}")
        info = []

        for team in repo.get_teams():
            info.append({"type": "team", "name": team.name})

        for collab in repo.get_collaborators(affiliation="direct"):
            info.append({"type": "user", "name": collab.login})

        pbar.update(1)

        return repo_name, info

    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(process_repo, repos))

        for repo_name, info in results:
            access_info[repo_name] = info

    return access_info
