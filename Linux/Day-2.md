# Add log file in repository
touch .gitignore
echo "Log entry: $(date)" > Linux/project.log # This will create Log file with time stamp in the folder
nano .gitignore  # This will open .gitignore and if you see *.log or Linux/, remove or comment them (Add #), save and exit Ctrl + x, then Y then Enter.

git add Linux/project.log #Add and commit the Log file
git commit -m "Add project.log file"
git push origin main

grep "error" project.log # This will show all lines with word "error"

grp -o "error" project.log # This will show exact word instead of entire lines

awk '{print $1, $2, $3, $4, $5, $6, $7}' Linux/project.log

sed -E 's/([0-9]{1,3}\.){3}[0-9]{1,3}/[REDACTED]/g' # by using sed replace all IP address with [REDACTED] for security

# Find the most frequent log entry using awk or sort | uniq -c | sort -nr | head -10.
sort Linux/project.log # Sorts all log lines alphabetically (required for uniq to group them)

uniq -c #Counts how many times each unique line appears

sort -nr # Sorts the counted lines by number (-n) in reverse (-r) to get most frequent first

head-10 # Shows the top 10 most frequent entries


# Volume Management & Disk Usage
##Create a directory /mnt/devops_data.
sudo mkdir -p /mnt/devops_data

# Mounting new volume
lsblk # identify new Volume
sudo mkdir /mnt/myvolume #Create a mount point (if needed)
sudo mount /dev/sdb1 /mnt/myvolume
df -h 
grep /mnt/myvolume


# For Practice: Creating  and  mounting a loop device
dd if=/dev/zero of=disk.img bs=1M count=100 # Create a blank file (e.g. 100 MB)
mkfs.ext4 disk.img # Format it with a filesystem (e.g., ext4)

sudo mkdir /mnt/loopdisk # Create a mount point

sudo mount -o loop disk.img /mnt/loopdisk

df-h # check mounted device
grep loop # check mounted device

sudo umount /mnt/myvolume  #unmount 

# Process management & Monitoring

ping google.com > ping_test.log &  #ping google.com rune the command, > ping_test.log redirects standard output to the file ping_test.log, & runs the command in the background

Additionally,
jobs # to see background jobs

fg %1 #to bring the job in the foreground

## To stop the background jobs
jobs -1 # Find its PID with

kill <PID> #Kill it with
