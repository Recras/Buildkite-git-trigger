# Buildkite-git-trigger
Triggers Buildkite pipelines based in changed branches in git.

# Usage

Create a volume-mount for a .ssh folder to /home/flask/.ssh, and export 3 env-vars:
 * BUILDKITE_URL, something like: https://api.buildkite.com/v2/organizations/{org.slug}/pipelines/{pipeline.slug}/builds?access_token={token}
 * GIT_URL, something like: git@github.com:Recras/Buildkite-git-trigger.git, make sure you have access to this repo
 * GIT_DIR, where you want the checkout, something like /tmp/gitdir

Example:

`docker run --rm -v ~/.ssh:/home/flask/.ssh -e "BUILDKITE_URL=https://api.buildkite.com/v2/organizations/{org.slug}/pipelines/{pipeline.slug}/builds?access_token={token}" -e "GIT_URL=git@github.com:Recras/Buildkite-git-trigger.git" -e "GIT_DIR=/tmp/gitdir" recras/buildkite-git-trigger`
