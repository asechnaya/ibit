
###documentation:
* Bug found [qa documents/bug_list.b.md](https://github.com/asechnaya/ibit/tree/master/qa%20documents/bug_list.b.md)
* Two bugs description [qa documents/two_bugs.c.md](https://github.com/asechnaya/ibit/tree/master/qa%20documents/two_bugs.c.md)
* Checklist: [qa documents/checklist.r.md](https://github.com/asechnaya/ibit/tree/master/qa%20documents/checklist.r.md)
* Test task Automation QA Engineer:: [qa documents/automation QA Engineer.pdf](https://github.com/asechnaya/ibit/tree/master/qa%20documents/automation%20QA%20Engineer.pdf)


### To run tests:

```
pytest --alluredir=allure-reports test_login_page.py 

pytest --alluredir=allure-reports test_payment_page.py 
``` 

### To visualize the report:
```
   allure serve allure-reports 
```

-----------------------------
![](qa%20documents/2022-12-16_12-51-26.png)