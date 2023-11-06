# Github Commit History Painting

<p align="center">
    <img src="img/git%20commit%20painting.png">
</p>

## Introduction

Whenever your github commit history feels bleak, use it to your advantage by turning it into a subtle canvas for your unresting inner artist! You can use this tool to edit your past commit history, effectively drawing on it.

## Features

Choose a year, committer's name, committer's email, draw on a visual representation of a dashboard and click 'Create!' to make a repository full of commits.

## Prerequisites

- Git Bash

## Installation

1. Download the latest version from Releases tab
2. Extract the archive

## Usage

1. Open git bash in the same folder as main.exe
2. Open the application using command `./main.exe <YEAR>`, specifying the year of displayed dashboard
3. Fill in the canvas
4. Specify user name and email (or leave blank, default is hard-coded)
5. Click 'Create!'

Now the git repository has been created, all you have to do is push it to a new remote repo:

1. Create a new empty repository on GitHub
2. Copy the link ending in `.git` from your new empty repository
3. Go to the `./temp_folder` using git bash, as that is your generated repository
4. Run the following:

```bash
git remote add origin <repository_url.git>
git push -u origin master
```

## Contributing

Feel free to post an issue if you have a suggestion.
To contribute to the code directly, fork the repository, create a branch, make the adjustments and create a pull request to this repo.
