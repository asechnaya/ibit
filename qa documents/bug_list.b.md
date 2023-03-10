# bugs_list

* Minor bugs [do not affect the functional]
    * Password has textarea tag instead of input
    * No email format check (i.e. for dots, ats, etc)
    * Extra symbols in the input form: 123 after "forgot password" in all languages 
    * Extra symbol after "enter email" text (and email placeholder text as well) in all languages
    * No question mark after "Forgot password" in English
    * Chinese is spelled as "CH", but "ZH" in tags. Should be consistent
    * Proceed button is a div, but repair password button is a button
    * "Send" instead of "sent" in restore password success notification ("New password was send to your email address")
    * [A designer has a humor] Obscene language: `<wtf>` tag
    * Chinese success text in restoring password action is 好吧，你是一個硬漢, 
  that is translated as "well you are a tough guy"


* Medium bugs [do not affect the functional or there is a workaround]
  * Password cannot be concealed [affects security]
  * The more you switch between languages the more slashes you obtain in the address link 
  [might have affect to the future functions, now just looks strange]
  * No possibility to register [no possibility to test new emails]
  * In indian version there is "message forget" text while restoring password
  * On payment page if you right-click on "you get" element, then choose "Inspect" and switch to another status, there will be two sums (current and previous)
  * When restoring a password, the email address is not checked. Registered and unregistered users receive the same notification.
  * The same name applies to two separate payments (VISA, MasterCard, Maestro) [There should be a distinction here, since that confuses users.]

* High [affects functional or customer's requirements]
  * Total sum is not calculated correctly if the amount is entered manually
  * Bonus link ("/#/bonus-terms?lang=en%23%2Fpayment") does not have a bonus description
  * Clicking on the "STATUS PRIVILEGES DESCRIPTION" link does not go to the description page
  * "Repair password" instead of "restore password" in English (wording is not obvious)
  * When a bonus is checked, the status slider does not change
  * You can enter [payment page](https://qa:Af4shrewyirlyuds@ibitcy.com/interview/qa/mobile-deposit/#/payment) directly without logging
  * Phone number does not show in qiwi payment if the payment is repeated in one session


* Critical [the bug does not allow to archive main goal, no workaround, affects business goals]
  * You can't log in as a korean user: when loging there an error instead of payment page
  * Chinese user could not succeed in payment (proceed button does not lead anywhere)
  * Bonus check does not add x2 when the entered sum is small < 10  [breach of contract]
  * Skrill and Neteller payment can't be processed, alert raises (0x0000fffe Resolve 0x0000fffe-Resolve PC Issues)
  [a user cannot top up their balance]
 