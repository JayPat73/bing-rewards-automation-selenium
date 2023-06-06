Inspired by saisandeepvaddi's selenuium bing automation script: https://github.com/saisandeepvaddi/selenium-bing-rewards-automation

# bing-rewards-automation-selenium

This repo contains code to automate the collection of Microsoft rewards points via random keyword searches in Microsoft Edge. Bing gives you 5 points per search, up to a max of 150 points per day (Level 2 Rewards), with an added 20 point bonus for using Microsoft Edge. This script should be ran **once** per day to recieve a max of 170 points.

## Requirements
1. Python 3 (Confirmed working with Python 3.11)
2. Install [Selenium](https://pypi.org/project/selenium/) (Confirmed working with selenium 4.7.2)
3. Install [Python Requests](https://pypi.org/project/requests/) (Confirmed working with requests 2.28.2)
4. Download the [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) and place it in the same root directory as the repository. The correct version can be found in your Edge Settings under 'About Microsoft Edge'
5. Make sure to log into your Microsoft Account in Edge. You should log in on the top right and have your account as the browser profile. Close the broser prior to running the script.

You should now be able to run the script as ```cmd> python bing-rewards.py```  

## Automation (run when computer is not being used)
1. Set file paths in bing-rewards.bat
  1. python.exe file path is most likely located in Appdata\Local\Programs\Python
2. Set power and sleep settings -> time to sleep -> minimum 15 minutes.
3. Create a task in Windows Task Scheduler (Search Task Scheduler in Window's Search Bar)
  1. Create a new task
  2. **General**
    1. Run only when user is logged in (Active session)
  3. **Triggers** -> New
    1. On a schedule
    2. Daily, recur every 1 days (I have it running at 3:00AM, task will run until completion)
    3. Disable all advanced settings
  4. **Actions** -> New
    1. Start a program
    2. Program/Script: "FILEPATH\TO\bing-rewards.bat"
  5. **Contitions**
    1. Start task only if the computer is idle for X minutes (I have it set for 1 minute)
    2. Wait for idle for 23 hours
  6. **Settings**
    1. Allow task to be run on demand
    2. Run task as soon as possible after a scheduled start is missed
    3. If the running task does not end when requested, force it to stop
