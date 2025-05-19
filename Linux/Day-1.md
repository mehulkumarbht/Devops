# Day 1 Notes
##User & Group Management
Create a user devops_user and add them to a group devops_team.

sudo adduser devops_user
sudo groupadd devops_team
sudo usermod -aG devops_team devops_user
Set a password and grant sudo access.

sudo passwd devops_user
sudo usermod -aG sudo devops_user        - By adding the user to sudo group
Restrict SSH login for certain users in /etc/ssh/sshd_config

vim /etc/ssh/sshd_config
Add the following to the config file: 
"DenyUsers dev1 dev2"



## File & Directory Permissions
Create /devops_workspace and a file project_notes.txt.

mkdir devops_workspace
cd devops_workspace
touch project_notes.txt
Set permissions: Owner can edit, group can read, others have no access.

chmod 640 project_notes.txt
Use ls -l to verify permissions.

ls -l
total 0
-rw-r----- 1 devops_user devops_team 0 May 17 07:32 project_notes.txt