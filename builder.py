import git, os, shutil, sys
import requests
from flask import Flask

app = Flask(__name__)

GIT_DIR = os.getenv('GIT_DIR')
if not GIT_DIR:
    GIT_DIR  = "/tmp/gitdir"

BUILDKITE_URL = os.getenv('BUILDKITE_URL')
if not BUILDKITE_URL:
    print('export BUILDKITE_URL env-var')
    exit(1)

GIT_URL = os.getenv('GIT_URL')
if not GIT_URL:
    print('export GIT_URL env-var')
    exit(1)

if not os.path.exists(GIT_DIR ):
    os.mkdir(GIT_DIR )
    print 'Cloning repo'
    repo = git.Repo.init(GIT_DIR , bare=True)
    origin = repo.create_remote('origin',GIT_URL)
else:
    repo = git.Repo(GIT_DIR )
    if not isinstance(repo, git.Repo):
        print 'Not a valid repo'
    exit(1)
    origin = repo.remotes.origin

fetched = origin.fetch()

@app.route('/', methods=['GET', 'POST'])
def build():
    fetched = origin.fetch()
    for fetch in fetched:
    if not fetch.flags & fetch.HEAD_UPTODATE:
        commit = repo.commit(fetch.ref)
        data = {
            'commit': 'HEAD',
            'branch': fetch.remote_ref_path,
            'message': commit.summary,
            'author': {'name': commit.author.name, 'email': commit.author.email}
        }
        requests.post(BUILDKITE_URL, json=data)
    return 'done'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
