# Contributing

## Requirements

* python3.9
* [Poetry](https://python-poetry.org/docs/#installation)

## Development Setup

* `poetry install` - install all dependencies.
* `poetry run task dev` - run code from the source.
* `poetry run task build` - create build zip at `./build/certbot-lambda.zip`
* `poetry run task test` - run created zip at `./build/certbot-lambda.zip`

## Dev configuration

You can create `.env` file and store all ENV variables that will be loaded on execution.

_.env_

```
CERTBOT_EMAILS=my@email.com
CERTBOT_DOMAINS=mydomain.com
CERTBOT_DNS_PLUGIN=dns-cloudflare
```

## Git Commit Guidelines

The semver level that should be bumped on a release is determined by the commit messages since the last release. In order to be able to decide the correct version and generate the changelog, the content of those commit messages must be parsed. It uses a parser for the [Angular commit message style](https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#commits):

```
<type>: <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

> The body or footer can begin with BREAKING CHANGE: followed by a short description to create a major release.

### Type

Must be one of the following:

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing or correcting existing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation

### Subject

The subject contains succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize first letter
* no dot (.) at the end

### Body

Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes". The body should include the motivation for the change and contrast this with previous behavior.


#### Footer

The footer should contain any information about Breaking Changes and is also the place to reference GitHub issues that this commit closes.

Breaking Changes should start with the word `BREAKING CHANGE:` with a space or two newlines. The rest of the commit message is then used for this.
