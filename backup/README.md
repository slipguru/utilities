Hello everyone, I'm writing this message in english so that in the future it can be provided to non-italian speakers phd students without having to translate it again.

I wrote a script which you can easily adapt to your needs to perform a backup of your folders on any remote machine that supports ssh and rsync. For the time being of course the machine will be the same for us all, and it is the NAS whose IP address is (at the moment) 10.251.61.6.

I will attach the script itself to this message, later maybe I will devise a smarter way to preserve it (like putting it somewhere on a bitbucket of some sort).

All you have to do is to put it somewhere in your filesystem (I suggest the folder /usr/local/bin/) and then add one or more lines to your crontab in order to activate the backup procedure. The crontab is edited using the following command:

crontab -e

You do not have to be sudoer to edit it, you only need to have read permission on the folder(s) you want to backup. The following line is an example of my crontab

59 2 * * * python /usr/local/bin/backup_folder.py /shared/compbio-disk-data/shared/projects/ backups/compbio/shared-projects

Every night at 2:59 AM it backs up the content of folder /shared/compbio-disk-data/shared/projects/. The backups can be found under /volume1/homes/admin/backups/compbio/shared-projects, there will be a number of folders named backup.i, with i ranging from 0 to 10. The higher i, the oldest the backup. So the latest snapshot is the one called backup.0.

**VERY IMPORTANT**: note that the trailing slash in the source folder (in my case, /shared/compbio-disk-data/shared/projects/) is required, otherwise it creates another level of folders.

**ALSO VERY IMPORTANT**: before the very first backup you have to access the NAS with ssh so that it adds the NAS host to the list of known_hosts (or something like that, just do the damn ssh thing). You should be prompted for something and enter 'yes'. Just to be sure, try again to ssh the NAS and it should ask you the password directly (without that yes/no question). If that's the case, you're good to go.

Before adding the backup job to your crontab (or, at least, before it is executed for the first time) you also have to create the folder on the NAS; I suggest we place all our backups under one folder called backups, then another folder identifying the machine from which the data originated and finally within this folder one folder for each folder we are going to backup.

If you want to backup more than just one folder all you have to do is add several lines to your crontab, changing the two arguments accordingly.

Enjoy!
