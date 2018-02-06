#!/bin/env python

### A version of the same script which uses subprocess
### Assumes the key authentication has been properly setup and tested
### to the remote machine (NAS)

import subprocess

import sys, os

from tempfile import mkstemp
import time

user = 'admin'
#host = 'compbio-nas'
host = '10.251.61.6'

def remote_move(src_, dst_):

    ### Must suppress error
    subprocess.call('ssh {}@{} "mv {} {} 2> /dev/null"'.format(user, host, src_, dst_), shell=True);

def create_log(remote_dst):

    # Create tmp file
    fd, tmp_file_path = mkstemp()

    remote_file_name = "BACKUP_{}.log".format(time.strftime("%Y%m%d"))

    os.write(
    fd,
    str.encode(
        "Backup was completed successfully at {}".format(time.strftime("%H:%M:%S %d/%m/%Y"))
        )
    )

    # Copy it in the remote folder
    subprocess.call('scp {} {}@{}:{}/backup.0/{}'.format(tmp_file_path, user, host, remote_dst, remote_file_name), shell=True);

    # Close the file
    os.close(fd)


def remote_rm(target):

    subprocess.call('ssh {}@{} "rm -rf {}"'.format(user, host, target), shell=True);


def remote_copy(src_, dst_):
    """
    Copy using hard links
    """

    ### cp -al dst/backup.0 dst/backup.1
    subprocess.call('ssh {}@{} "cp -al {} {} 2> /dev/null"'.format(user, host, src_, dst_), shell=True);

def rsync(local_src, remote_dst):
    """
    """

    # rsync -a --delete src/  dst/backup.0/
    subprocess.call('rsync -a --delete {} {}@{}:{}/backup.0/'.format(local_src, user, host, remote_dst), shell=True);


def daily_backup():

    if len(sys.argv) < 3:
        print("Usage:")
        print("back.py local_folder remote_folder")

        return

    #######################
    ### GLOBAL SETTINGS ###
    #######################

    ### the home folder where all backups are stored
    admin_home = '/volume1/homes/admin'
    ### the password for the admin user

    ######################
    ### LOCAL SETTINGS ###
    ######################

    ### The total number of backups kept in memory (the actual number is N + 1)
    N = 10

    ### The local folder that must be backed up (keep the trailing /)
    # local_src = 'src/'
    local_src = sys.argv[1]

    ### The remote folder where backups will be kept. All backups will be found in remote_dst/backup.i for i = 0..N (0 being the most recent one)
    # remote_dst = admin_home + '/backup-shared'
    remote_dst = os.path.join(admin_home, sys.argv[2])

    #################
    ### PROCEDURE ###
    #################

    ### First delete the oldest backup
    # rm -rf dst/backup.$N
    print("Removing oldest backup...")
    remote_rm(remote_dst + '/backup.{}'.format(N))
    print("Done!")

    ### Then shift the numbers of all existing backup folders, i.e:
    # mv dst/backup.2 dst/backup.3
    print("Shifting old backup folders...")
    # for i in range(N,0,-1):
    for i in range(N,1,-1):
        src_ = remote_dst + '/backup.{}'.format(i-1)
        dst_ = remote_dst + '/backup.{}'.format(i)
        remote_move(src_, dst_)
    print("Done!")

    ### Copy the newest existing backup
    #cp -al dst/backup.0 dst/backup.1
    print("Copying latest backup...")
    src_ = remote_dst + '/backup.{}'.format(0)
    dst_ = remote_dst + '/backup.{}'.format(1)
    remote_copy(src_, dst_)
    print("Done!")

    ### Finally, create a new backup
    # rsync -a --delete src/  dst/backup.0/
    print("Pushing latest snapshot...")
    rsync(local_src, remote_dst)
    print("Done!")

    print("Creating backup log...")
    create_log(remote_dst)
    print("Done!")

    print("Finished.")

if __name__ == '__main__':

    daily_backup()


# N=10
#
#
# for i in `seq 1 $N`;
# do
#   aft=`expr $N - $i + 1`
#   bef=`expr $N - $i`
#   #echo "$b"
# done
#
# rm -r dst/backup.$N
# #mv dst/backup.2 dst/backup.3
# #mv dst/backup.1 dst/backup.2
# #cp -al dst/backup.0 dst/backup.1
# #rsync -a --delete src/  dst/backup.0/
