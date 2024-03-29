[![Build Status](https://travis-ci.org/sujitmandal/python-gmail.svg?branch=master)](https://travis-ci.org/sujitmandal/python-gmail) [![GitHub license](https://img.shields.io/github/license/sujitmandal/python-gmail)](https://github.com/sujitmandal/python-gmail/blob/master/LICENSE) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python-gmail) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/python-gmail) ![PyPI](https://img.shields.io/pypi/v/python-gmail) [![Conda Version](https://img.shields.io/conda/vn/conda-forge/python-gmail.svg)](https://anaconda.org/conda-forge/python-gmail) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/python-gmail/badges/version.svg)](https://anaconda.org/conda-forge/python-gmail) [![Anaconda-Server Badge](https://anaconda.org/conda-forge/python-gmail/badges/installer/conda.svg)](https://conda.anaconda.org/conda-forge) [![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/python-gmail.svg)](https://anaconda.org/conda-forge/python-gmail) [![Conda Recipe](https://img.shields.io/badge/recipe-python--gmail-green.svg)](https://anaconda.org/conda-forge/python-gmail) ![](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/python-gmail-feedstock?branchName=main)


[![Downloads](https://pepy.tech/badge/python-gmail)](https://pepy.tech/project/python-gmail)

## Package Installation : 
```
pip install python-gmail
```
[Package Link](https://pypi.org/project/python-gmail/)
```
conda install -c conda-forge python-gmail
```
[Conda Package Link](https://anaconda.org/conda-forge/python-gmail)

[python-gmail-feedstock Link](https://github.com/conda-forge/python-gmail-feedstock)


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

gmail_password = ('') #sender g-mail password
```
## Single destination mail id :
```python
destination_addresses = [
                    'reciver_mail_id_1@gmail.com'
                    ]
```

## Multiple destination mail id's :
```python
destination_addresses = [
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
## mail message :
```python
message = ('') #mail message
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
mail.login(gmail_id, gmail_password)
```
## give reciver mail id or id's. :
```python
mail.receiver_mail(destination_addresses)
```
## send mail :
```python
mail.send_mail(subject, message)
```
## Example :
```python
from gmail.gmail import gmail

mail = gmail()

mail.login(gmail_id, gmail_password)

mail.receiver_mail(destination_addresses)

mail.send_mail(subject, message)
```

## License :
MIT Licensed

## Author :
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)
