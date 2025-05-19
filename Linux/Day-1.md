## User & Group Management
Create a user devops_user and add them to a group devops_team.

sudo groupadd devops_team # Creates a group names devops_team
sudo useradd -m -s /bin/bash -g devops_team devops_user # add user named devops_user

## Set a password and grant sudo access.
sudo passwd devops_user
sudo usermod -aG sudo devops_user        - By adding the user to sudo group

## Restrict SSH login for certain users in /etc/ssh/sshd_config
sudo nano /etc/ssh/sshd_config #Edit the SSH daemon config File
At the bottom, add:
Allowusers devops_user mehulkumarbht, then ctrl+0, Enter, Ctrl+X.

## Restart SSH
sudo systemct1 restart ssh


## File & Directory Permissions
## Create /devops_workspace and a file project_notes.txt.

sudo mkdir/devops_workspace
sudo touch /devops_workspace/project_notes.txt

sudo chmod 640 /devops_workspace/project_notes.txt

#Use ls -l to verify permissions.

ls -l /devops_workspace
Expected output:
-rw-r----- 1 your_username devops_team 0 <timestamp> project_notes.txt #rw- for owner, r--for group, ---for others
