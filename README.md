# Cookiecutter for uDALES experiments

Template repository for starting new experiments project with the uDALES model.

## Prerequisites
- [Git](https://git-scm.com/)
- [Python 3.5+](https://www.python.org/)
- [Cookiecutter](https://github.com/cookiecutter/cookiecutter) (`pip install cookiecutter`)
- Plus [prerequisites for building uDALES](https://github.com/uDALES/u-dales#prerequisites).

## Usage

Create a new empty repository on your GitHub account then, to start a new project within the current working directory:

```sh
cookiecutter https://github.com/uDALES/cookiecutter-u-dales
```

where `<PROJECT_NAME>` is the name of the generated project directory and `<GITHUB_PROJECT_REMOTE>` is the URL to your remote GitHub account. E.g.

```sh
directory_name [<PROJECT_NAME>]: neutral_experiments
github_project_remote [<GITHUB_PROJECT_REMOTE>]: https://github.com/<MY_GITHUB_USERNAME>/<MY_NEW_EMPTY_REPO>.git

```


## Copyright and license

Copyright 2019 D. Meyer. Licensed under MIT.