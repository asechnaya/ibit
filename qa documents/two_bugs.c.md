# Bug report 1 (critical) Chinese user could not make a payment

 
  **Data**: _login = ...; password = ...;_ 
  _email = username2@name.ru | pass: pass2_;

  > Open the [ibitcy.com](https://ibitcy.com/interview/qa/mobile-deposit)
  > Enter login and pass

  **Expected result**
  * Status code == 200, New page opens, there is an authentication form
  
  **Actual result**
  * Status code == 200, New page opens, there is an authentication form
  
  > Switched to CH language

  **Expected result**
  * Page has been translated into chinese

  **Actual result**
  * Page has been translated into chinese

  > Enter valid email and password, click on proceed button 

  **Expected result**
  * New page opens, there is a payment form

  **Actual result**
  * New page opens, there is a payment form

 > Choose any status and click the proceed button
 
  **Expected result**
  * New page opens, there is a successful payment text

  **Actual result**
  * No page opens, the user is still on the payment page


# Bug report 2 (high) Total sum is not calculated correctly if the amount is entered manually

**Data**: _login = ...; password = ...;_
_email = username2@name.ru | pass: pass2_;

> Open the [ibitcy.com](https://ibitcy.com/interview/qa/mobile-deposit)
> Enter login and pass

**Expected result**
* Status code == 200, New page opens, there is an authentication form

**Actual result**
* Status code == 200, New page opens, there is an authentication form

> Enter valid email and password, click on proceed button

**Expected result**
* New page opens, there is a successful payment text

**Actual result**
* No page opens, the user is still on the payment page

> Enter a random amount (i.e. 3535) in the amount form
> Change currency

**Expected result**
* Total amount should be the same as in the form 

**Actual result**
* Total amount has been calculated from entered amount in previous 
currency to current currency, while the number in the form still 
remains



