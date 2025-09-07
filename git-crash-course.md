## Git Hidden Folder
There is a hidden folder called `.git` which tells you that your project is git repo.
If we want to create a git repo in a new project we' create the folder and then initialize that repo using `git init` 
```sh
mkdir /workspace/tmp/new-project
cd /workspace/tmp/new-project
git init
touch Readme.md
code Readme.md
git status
git add Readme.md
# make chanes to readme.md
git commit -m "add readme file"
```
## Cloning

Three way to clone a repository: 1. HTTPS 2. SSH 3. Github CLI

Since we are using GitHub Codespaces we'll create temporary directory in our workspace
```sh
mkdir /workspace/tmp
cd /workspace/tmp
```

### HTTPS:
```sh
git clone https://github.com/mehulkumarbht/Devops.git
cd Github-examples
```
### SSH:

```sh
git clone git@github.com:mehulkumarbht/Devops.git
cd Github-Examples
```

### Github CLI
Install on Linux(Ubuntu)

```sh
(type -p wget >/dev/null || (sudo apt update && sudo apt install wget -y)) \
	&& sudo mkdir -p -m 755 /etc/apt/keyrings \
	&& out=$(mktemp) && wget -nv -O$out https://cli.github.com/packages/githubcli-archive-keyring.gpg \
	&& cat $out | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
	&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
	&& sudo mkdir -p -m 755 /etc/apt/sources.list.d \
	&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
	&& sudo apt update \
	&& sudo apt install gh -y

    gh auth login
    gh repo clone gh repo clone mehulkumarbht/Devops
```

## Commits
When we want to commit code we can write `git commit` which will open up the commit edit message in the editor of choice.
```sh
git commit

#set the global editor, for example
git config --global core.editor "code --wait"
#make a commit and commit message without opening an editor
git commit -m "add another exclaimation"
```


## Branches
List of branches
```sh
git branch
```
Create a new branch
```sh
git branch dev #use whatever name you want instead dev
git branch 
git checkout dev #switched to branch dev
```



## Remote
We can add remote but often you will just add remote via upstream when adding a branch

```sh
git remote add ...
git branch -u origin new-feature
```
## Stashing
```sh
git stash list
git stash
git stash save my-name
git stash apply
git stash pop
```


## Merging
```sh
git checkout dev
git merge main
```

## Add
When we want to stage changes that will be included in the commit we can use the `.` to add all possible files. 
```sh
git add Readme.md
```


## Reset
Reset allows you to move staged changes to be unstaged. This is useful when you do not want to revert all filed not to be commited.
```sh
git add .
git reset
```
`git reset` will revert `git add .`(git add all files)

## Status
Git status shows you what files will or will not be commited 
```sh
git status
```

## Git config file
The git config file is what stores global configurations for git such as email, name, editor and more.

To show contains of our `.gitconfig` file
```sh
git config --list
```

When you first install Git on a machine you are setup your name and email
```sh
git config --global user.name "John Doe"
git config --gloabl user.email "johndoe@example.com" 
```

## Log
`git log` will show recent git commits to the git tree

## Push
When we want to push a repo to our remote origin 

```sh
git push origin main
```