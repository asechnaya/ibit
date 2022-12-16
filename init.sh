# install python packages
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# create allure folder
mkdir report
mkdir drivers

# install appium
npm init
sudo nmp install