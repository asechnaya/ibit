# install python packages
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# create allure folder
mkdir report
mkdir drivers

# run tests
pytest --alluredir=allure-reports test_login_page.py
pytest --alluredir=allure-reports test_payment_page.py