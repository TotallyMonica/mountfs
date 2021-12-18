# mountfs

## Descripton
An easy-to-use Python script to mount network shares based off of your current local IP

## How to set up:
1. `git clone https://github.com/TotallyMonica/mountfs && cd mountfs`
2. Open mountfs.py in your favorite text editor (I personally use `nano`, but to each their own) and modify lines 14 and 17 to fit the relevant IPs
3. Adjust the mounts to your liking, following the provided comments (Feel to free to add as many elif statements and mount statements as you need.)
4. Save and quit, and make note of the directory it's saved to.
5. Open mountfs.service in your favorite text editor and adjust line 6 to the path of the python file previously edited
6. `cp mountfs.service /etc/systemd/system`
7. `systemctl daemon-reload`
8. `systemctl start mountfs.service`

## Prerequisites
 - Python3

## To-do list
 - Create script to easily set this up, possibly for a release?
 - NFS support
 - sshfs support
 - Other network file system supports
 - Support for other daemons
 - (To avoid Python bashing) write it in other languages (top priority, bash)