# TROReports User's Guide

## Test Environment
Remove any old log files from previous runs:

```
cd /Users/jeff/test/TROReports/local/log
rm *
```
Edit the existing crontab to run the desired report. Make sure all the parameters are correct.

Switch to the log directory and check the files to insure the job ran as expected.

```
cd /Users/jeff/test/TROReports/local/log
view *
```

If everything looks good, go to the rpt directory and open the generated spreadsheet:

```
cd /Users/jeff/test/TROReports/local/rpt
view 
```
