# TRO Reports System Guide

## Deploying a new release to Test

**If FireStarter has not been updated to specify a release, stage the desired release in the /tmp directory before running auto_update. Then be sure to select the option to use the existing tar file.**

```
cd /tmp
git clone https://github.com/jasmit35/TROReports.git --branch release/v1.0.0
```
### Archive the existing version:

```
cd ~/test/
tar -czvf TROReports_2022_06_25.tar.gz TROReports
```

### Clean up any much older archives and the current version:

```
cd ~/test/
ll
rm TROReports_2021*
rm -rf TROReports
```

### Use auto-update to install the new release:

```
export ENVIRONMENT=test
auto-update -e test -a TROReports
```

### Update .db_secrets.env
The secrets files are not stored on GitHub because they contain user names and passwords. You need to manually copy the files:

```
cd /Users/jeff/test/TROLoad/local/etc
cp /Users/jeff/devl/TROLoad/local/etc/.db_secrets.env .



## Steps to upgrade Test and Prod environments to a new version.

### Hide the existing version:

`cd ~/test/trorpts`

`mkdir .old`

`mv * .old`


### Use the standard auto-update to download and install the latest version from github:

`export ENVIRONMENT=devl`

`. ~/.bash_profile`

`auto-update -e test -a troload`

### Set the password for the database user:

The password for the database user (tro_rw) is stored in a file that is NOT saved to github. You must recreate it. troload/local/etc/.db_secrets.env.


