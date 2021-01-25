# Contents
* [1. Introduction](#1-introduction)
  * [1.1 Why do these guidelines exist?](#11-why-do-these-guidelines-exist)
  * [1.2 What kinds of contributions are we looking for?](#12-what-kinds-of-contributions-are-we-looking-for)
* [2. Ground Rules](#2-ground-rules)
* [3. Your First Contribution](#3-your-first-contribution)
* [4. Getting Started](#4-getting-started)
  * [4.1 Setting up your development environment](#41-setting-up-your-development-environment)
  * [4.2 To contribute changes](#46-to-contribute-changes)
  * [4.3 How To Report A Bug](#47-how-to-report-a-bug)
* [5. Code Review Process](#5-code-review-process)
  * [5.1 Issues](#51-issues)
  * [5.2 Pull Requests](#52-pull-requests)

# 1. Introduction
**Welcome!** First off, thank you for contributing to the further development of TearDrops. We're always looking for new ways to improve our project and we appreciate any help you can give us.

### 1.1 Why do these guidelines exist?
TearDrops is an open source project. This means that each and every one of the developers and contributors who have helped make TearDrops what it is today have done so by volunteering their time and effort. It takes a lot of time to coordinate and organize issues and new features and to review and test pull requests. By following these guidelines you will help the developers streamline the contribution process and save them time. In doing so we hope to get back to each and every issue and pull request in a timely manner.

### 1.2 What kinds of contributions are we looking for?
We love receiving contributions from our community. Any assistance you can provide with regards to bug fixes, feature enhancements, and documentation is more than welcome.

# 2. Ground Rules
1. Ensure cross compatibility for Windows, Mac OS and Linux.
2. Ensure all Python features used in contributions exist and work in Python 3.8.1 and above.
3. Create any issues for new features you'd like to implement and explain why this feature is useful to everyone and not just you personally.
4. Don't add new cogs unless specifically given approval in an issue discussing said cog idea.
5. Be welcoming to newcomers and encourage diverse new contributors from all backgrounds. See [Python Community Code of Conduct](https://www.python.org/psf/codeofconduct/).
6. Get yourself assigned to an issue before working on the PR to avoid double work. 

# 3. Your First Contribution
Unsure of how to get started contributing to TearDrops? Please take a look at the Issues section of this repo and sort by the following labels:

* good first issue - issues that can normally be fixed in just a few lines of code and maybe a test or two.
* help-wanted - issues that are currently unassigned to anyone and may be a bit more involved/complex than issues tagged with beginner.

**Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)

At this point you're ready to start making changes. Feel free to ask for help; everyone was a beginner at some point!

# 4. Getting Started

TearDrops's repository is configured to follow a particular development workflow, using various reputable tools. We kindly ask that you stick to this workflow when contributing to TearDrops, by following the guides below. This will help you to easily produce quality code, identify errors early, and streamline the code review process.

### 4.1 Setting up your development environment
The following requirements must be installed prior to setting up:
 - Python `3.8.1` or greater
 - git
 - pip
 
If you're not on Windows, you should also have GNU make installed, and you can optionally install [pyenv](https://github.com/pyenv/pyenv), which can help you run tests for different python versions.

1. Fork and clone the repository to a directory on your local machine.
2. Open a command line in that directory and execute the following command:
    ```bash
    python3 -m venv venv
    ```
    TearDrops, its dependencies, and all required development tools, are now installed to a virtual environment located in the `.venv` subdirectory. TearDrops is installed in editable mode, meaning that edits you make to the source code in the repository will be reflected when you run TearDrops.
3. Activate the new virtual environment with one of the following commands:
    - Posix:
        ```bash
        source .venv/bin/activate
        ```
    - Windows:
        ```powershell
        .venv\Scripts\activate
        ```
    Each time you open a new command line, you should execute this command first. From here onwards, we will assume you are executing commands from within this activated virtual environment.
 
**Note:** If you're comfortable with setting up virtual environments yourself and would rather do it manually, just run `pip install -r bot/requirements.txt` after setting it up.

### 4.2 To contribute changes

> - Make sure you have been assigned the issue to which you are making a PR.
> - If you make PR before being assigned, It will be labeled `invalid` and closed without merging.

* Fork the repo and clone it on your machine.
* Add a upstream link to main branch in your cloned repo
    ```
    git remote add upstream https://github.com/Vyvy-vi/TearDrops
    ```
* Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)
    ```
    git pull upstream master
    ```
* Create your feature branch
    ```
    git checkout -b <feature-name>
    ```
* Commit all the changes
    ```
    git commit -am "Meaningful commit message"
    ```
* Push the changes for review
    ```
    git push origin <branch-name>
    ```
* Create a PR from our repo on Github.

##### Some Additional Notes:
* Code should be properly commented to ensure it's readability.
* If you've added code that should be tested, add tests as comments.
* Make sure your code properly formatted.
* Issue that pull request!
* use Flake8 for python code


### 4.3 How To Report A Bug
Submit an issue on GitHub and add as much information as you can about the bug, with screenshots of inputs to the bot and bot response if possible (if the issue is regarding bugs). Try to make issues that are not blank and are in their respective category. 

### 5.1 Issues
Any new issues will be looked at and evaluated for validity of a bug or for the usefulness of a suggested feature. If we have questions about your issue we will get back as soon as we can (usually in a day or two) and will try to make a decision within a week.
**Great Issue suggestions** tend to have:

- A quick summary of the changes.
- In case of any bug provide steps to reproduce
  - Be specific!
  - Give sample code if you can.
  - What you expected would happen
  - What actually happens
  - Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)


### 5.2 Pull Requests
Pull requests are evaluated by their quality and how effectively they solve their corresponding issue. The process for reviewing pull requests is as follows:

1. A pull request is submitted
2. Core team members will review and test the pull request (usually within a week)
3. After a member of the core team approves your pull request:
    * If your pull request is considered an improvement or enhancement the project owner will have 1 day to veto or approve your pull request.
    * If your pull request is considered a new feature the project owner will have 1 week to veto or approve your pull request.
4. If any feedback is given we expect a response within 1 week or we may decide to close the PR.
5. If your pull request is not vetoed and no core member requests changes then it will be approved and merged into the project.

By contributing, you agree that your contributions will be licensed under its [MIT License](http://choosealicense.com/licenses/mit/)
