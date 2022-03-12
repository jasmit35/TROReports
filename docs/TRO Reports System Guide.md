# TRO Reports System Guide

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


