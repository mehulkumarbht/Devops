Day 1:

## User & Group Management:

sudo adduser devops_user # create new user
Add password
sudo groupadd devops_team # create new groupadd
sudo usermod -aG devops_team devops_user
groups devops_user # check group of the user 

## Set a password and grant sudo access:
sudo passwd devops_user #set new password for the user
sudo usermod -aG sudo devops_user  # Add user to the sudo group

su - devops_user # Switch to this user
sudo whoami # Expected output 'root' will give confirmation

## Restrict SSH login for certain users in /etc/ssh/sshd_config
sudo nano /etc/ssh/sshd_config # Open SSH configuration file
AllowUsers devops_user # Only users listed here will be allowed to log in via SSH
sudo systemctl1 restart ssh # Restart the SSH service




