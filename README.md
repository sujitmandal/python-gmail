[![Build Status](https://travis-ci.org/sujitmandal/python-gmail.svg?branch=master)](https://travis-ci.org/sujitmandal/python-gmail) [![GitHub license](https://img.shields.io/github/license/sujitmandal/python-gmail)](https://github.com/sujitmandal/python-gmail/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-gmail) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/python-gmail) ![PyPI](https://img.shields.io/pypi/v/python-gmail)


[![Downloads](https://pepy.tech/badge/python-gmail)](https://pepy.tech/project/python-gmail)

## Package Installation : 
```
pip install python-gmail
```
## python-gmail :
Inorder to send mail form gmail using SMTP Server, first you need to enable "Two-Step Verification" on the sender mail id.

   [Google Account Help](https://support.google.com/accounts/answer/185839?co=GENIE.Platform%3DDesktop&hl=en&oco=0)

1. Open your [Google Account](https://myaccount.google.com/) .
```
2. In the navigation panel, select Security.

3. Under “Signing in to Google,” select 2-Step Verification and then Get started.

4. Set any "Account PIN". This pin will be the passowad of the sender mail is.
```
How to use the module :
----------------------

## E-mail login credential :
```python
gmail_id = ('') #sender g-mail id

password = ('') #sender g-mail password
```
## Single Reciver mail id :
```python
reciver_mail_id = [
                    'reciver_mail_id_1@gmail.com'
                    ]
```

## Multiple Reciver mail id's :
```python
reciver_mail_id = [
                    'reciver_mail_id_1@gmail.com',
                    'reciver_mail_id_2@gmail.com',
                    'reciver_mail_id_3@gmail.com',
                    '............................',
                    '.............................',
                    'reciver_mail_id_N number@gmail.com',
                    ]
```

## main subject :
```python
subject = ('') #mail subject
```
## mail contain :
```python
mail_contain = ('') #mail contain
```
## How to import the module :
```python
from gmail.gmail import gmail
```
## create mail object :
```python
mail = gmail()
```
## give sender login credential :
```python
mail.login(gmail_id, password)
```
## give reciver mail id or id's. :
```python
mail.reciver_mail(reciver)
```
## send mail :
```python
mail.send_mail(subject, mail_contain)
```
## Example :
```python
from gmail.gmail import gmail

mail = gmail()

mail.login(gmail_id, password)

mail.reciver_mail(reciver)

mail.send_mail(subject, mail_contain)
```

## License :
MIT Licensed

## Author :
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)