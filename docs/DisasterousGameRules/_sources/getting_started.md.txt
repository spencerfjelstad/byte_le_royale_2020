# Getting Started

* First thing you should do is get acquainted with this documentation. It is your game manual!
* Next, download the .zip file [here](https://drive.google.com/uc?export=download&id=1MHCV_sHKObTQF9K9FlUa3WvtCCri8m4z) and extract it.
* Open a powershell window at that location by holding shift and right clicking in the extracted folder, then selecting "Open PowerShell window here."
* Ensure Python is installed correctly and at least version 3.7.
* Type `pipenv install -d` and wait for it to finish.
* Type `pipenv shell`.
* If your launcher is out of date, run `python ./launcher.pyz u` to get updates.
* Type `python ./launcher.pyz s` to enter the scrimmage command line.
* Type `r` to register your teamname. Follow on-screen instructions to enter it properly.
* This creates vID file in your folder. This is your team ID number. Do not lose this file! You can share it with your teammates so they may submit code and view stats too.
* Write your client code! You may edit the `my_client.py` file as you wish, or you may create any python file with "client" in the name.
* To test your client, use your PowerShell window (that is in the Pipenv shell) to run `python ./launcher.pyz generate` to create a new world, `python ./launcher.pyz run` to test your client, and `python ./launcher.pyz visualizer` to view the results of the last run.
* To submit your client, run `python ./launcher.pyz s` to enter the scrimmage command line, and use `s` to submit your code.
* You may also use the scrimmage command line to view the leaderboard and your stats.
