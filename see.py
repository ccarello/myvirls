import requests
from pprint import pprint


def get_repos(org='ccarello', query=None):
    resp = requests.get('https://api.github.com/orgs/{}/repos'.format(org))
    ret = list()

    if query is None:
        return resp.json()

    for repo in resp.json():
        name = repo['name']
        descr = repo['description']
        if query in name:
            ret.append(repo)
        if descr and query in descr:
            ret.append(repo)

    return ret


pprint(get_repos())
