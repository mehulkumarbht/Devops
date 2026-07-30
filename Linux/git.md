#Steps to start with Git:
#1: git config --global user.name "Mehul Bhatt"
#2: git config --global user.email "mehulbhatt@gmail.com
#3: Create a folder (make sure you are in correct folder by using pwd): mkdir cats
#4: Go to that folder: cd cats
#5: Initialize as a Git repository and set the name of the default branch to main: git init -b main
#6: Create new html file: touch index.html
#7: check it with: ls -a (use '-a' to see subdirectory .git exits in the folder)
#8: check it's status in git with: git status
#9: Add this folder to git: git add . (or use sepecific path, git add cats/index.html to be safe)
#10: Now commit that file to git: git commit index.html -m "Create an empty index.html file"
#11: If you make any changes to the file and want to make them on git: git commit -a -m "Add a heading to index.html" (Thi '-a' command will include all changes made to the repository including anything added, modified or delted)

#12: if you want to see logs: git log --oneline (this will show you changes made in the repository)
#13: To see changes made to the file: git diff
#14: To make changes to the file: git commit -m "Add HTML body in index.html"
#15: Add gitignore file to ask git to avoid specific file type: code .gitignore (and then save it)
#16: There is another option: git commit -am "Make small change; ignore edit or backups (This way you can avoid git add step, but use this step with caution as this will add all files creates and modified. If you only want to add one changes made to one file, git add and git commit -m steps are safe to use)
#17: by mistake if you delete a file in your workig directory with: rm index.html 
#18: and to recover it from git, use: git checkout --index.html
#19: Another mistake, if you remove a file from git like, : git rm index.html
#20: to bring that back in git, use: git reset HEAD index.html
#21: And then, to bring it back in working directory use: git checkout --index.html
#22: In case if you removed a part of code or all code from the file and committed it on gib and you want to bring that back, then follow this steps: git log --one line (and find out the commint hash# you want to go back i.e. 4e40438)
and then: git checkout 4e40438 . (do not miss dot (.) at the end)
and to solidify this commit it with: git commit -m "Revert the changes"
#23: Lastly to get help with commands: git --help