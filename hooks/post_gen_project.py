# https://github.com/uDALES/cookiecutter-u-dales.
# Copyright 2019 D. Meyer. Licensed under MIT.

import subprocess

GITHUB_PROJECT_REMOTE = "{{cookiecutter.github_project_remote}}"

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])

subprocess.call(['git', 'submodule', 'add', '-b', 'master', 'https://github.com/uDALES/u-dales.git'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Add u-dales'])

subprocess.call(['git', 'remote', 'add', 'origin', GITHUB_PROJECT_REMOTE])
subprocess.call(['git', 'push', '-u', 'origin', 'master'])
