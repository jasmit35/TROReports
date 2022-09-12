# TRO Reports System Guide

## Deploying a new release to Test

**If FireStarter has not been updated to specify a release, stage the desired release in the /tmp directory before running auto_update. Then be sure to select the option to use the existing tar file.**

```
cd /tmp
git clone https://github.com/jasmit35/TROReports.git --branch release/v1.0.0
```

### Archive existing version:

```
cd ~/test/
tar -czvf TROReports_2022_06_25.tar.gz TROReports
mv TROReports_*.tar.gz ~/test.archive
rm -rf TROReports
```

### Clean up older archives:
```
cd ~/test/.archive
rm TROReports_2021*
ll
```

### Use auto-update to install the new release:
```
export ENVIRONMENT=test
auto-update -e test -a TROReports
```

### Update .db_secrets.env
The secrets files are not stored on GitHub because they contain user names and passwords. You need to manually copy the files:

```
cd /Users/jeff/test/TROReports/local/etc
cp /Users/jeff/devl/TROReports/local/etc/.db_secrets.env .
```

### Install required packages:

```
cd /Users/jeff/test/TROReports
pip install -r requirements.txt
```

## Deploying a new release to Prod
**If FireStarter has not been updated to specify a release, stage the desired release in the /tmp directory before running auto_update. Then be sure to select the option to use the existing tar file.**

```
cd /tmp
git clone https://github.com/jasmit35/TROReports.git --branch release/v0.0.0
```

### Archive the existing version:

```
cd ~/prod/
tar -czvf TROReports_2022_06_26.tar.gz TROReports
```

### Clean up any much older archives and the current version:

```
cd ~/prod/
ll
rm TROReports_2021*
rm -rf TROReports
```

### Use auto-update to install the new release:

```
export ENVIRONMENT=prod
auto-update -e prod -a TROReports
```
### Update .db_secrets.env
The secrets files are not stored on GitHub because the contain user names and passwords. You need to manually copy the files:

```
cd /Users/jeff/prod/TROReports/local/etc
cp /Users/jeff/devl/TROReports/local/etc/.db_secrets.env .
```

### Install required packages:

```
cd /Users/jeff/prod/TROReports
pip install -r requirements.txt
```
