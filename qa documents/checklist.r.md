# checklist

* Check list in a table mode

| Test name                                                                             | Chrome | FF     | Edge   |
|---------------------------------------------------------------------------------------|--------|--------|--------|
| **site access**                                                                           |        |        |        |
| Site authorization is successful                                                      | passed | passed | passed |
| Site authorization is unsuccessful (401)                                              | passed | passed | passed |
| **email auth**                                                                            |        |        |        |
| languages are switched, the site is displayed in the selected language                | passed | passed | passed |
| Password can be recovered using the Forgot Password link.                             | passed | passed | passed |
| If the email is not registered, there should be an error                              | passed | passed | passed |
| There is a check for the entered email format                                         | failed | failed | failed |
| The entered password is not shown or has a hide password icon                         | failed | failed | failed |
| Registration button and recover pass link should have proper names in all languages                                            | failed | failed | failed |
| Any unregistered user must not be authorized                                          | passed | passed | passed |
| The registered user must be authorized and directed to the balance replenishment page for all languages | failed | failed | failed |
| **PAYMENTS**                                                                              |        |        |        |
| Should be privileges and bonuses description                                          | failed | failed | failed |
| Should be statuses Mini, Silver, Gold, VIP                                            | passed | passed | passed |
| Bonuses can be switch off and on and add extra sum of money                           | passed | passed | passed |
| User can chose one of currencies and amount should be converted according currency    | passed | passed | passed |
| User can choose one of currencies                                                     | passed | passed | passed |
| User can choose from payment systems                                                  | passed | passed | passed |
| User can add bonus to their amount                                                    | passed | passed | passed |
| User can enter sum manually                                                           | passed | passed | passed |
| User should make a successful payment and see Successful text  in any language        | failed | failed | failed |
| User should make a successful payment in every payment system and currency            | passed | passed | passed |
| Back button should appear and be clickable in every language                          | passed | passed | passed |