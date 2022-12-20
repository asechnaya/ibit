# install python packages
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#        run: pip install tox
#      - name: Run tox
#        # Run tox using the version of Python in `PATH`
#        run: tox -e py

# download allure
wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip
unzip allure-2.13.8.zip
rm allure-2.13.8.zip

# create allure folder
mkdir report
mkdir drivers

# run tests
pytest --alluredir=allure-reports test_login_page.py
pytest --alluredir=allure-reports test_payment_page.py

# make reports
allure serve allure-reports