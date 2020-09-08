## python-gmail :
Automatically  Send Gmail with SMTP Server.

[![Downloads](https://pepy.tech/badge/python-gmail)](https://pepy.tech/project/python-gmail)

## Package Installation : 
```
pip install python-gmail
```
[Package Link](https://pypi.org/project/python-gmail/)
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
```
gmail_id = ('') #sender g-mail id

password = ('') #sender g-mail password
```
## Single Reciver mail id :
```
reciver_mail_id = [
                    'reciver_mail_id_1@gmail.com'
                    ]
```

## Multiple Reciver mail id's :
```
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
```
subject = ('') #mail subject
```
## mail contain :
```
mail_contain = ('') #mail contain
```
## How to import the module :
```
from gmail.gmail import gmail
```
## create mail object :
```
mail = gmail()
```
## give sender login credential :
```
mail.login(gmail_id, password)
```
## give reciver mail id or id's. :
```
mail.reciver_mail(reciver)
```
## send mail :
```
mail.send_mail(subject, mail_contain)
```
## Example :
```
from gmail.gmail import gmail

mail = gmail()

mail.login(gmail_id, password)

mail.reciver_mail(reciver)

mail.send_mail(subject, mail_contain)
```

## Requirement’s:
```
• Python 

• Anaconda

• Visual Studio Code
```
## LINK’S:
• [Python Download](https://www.python.org/downloads/)

• [Anaconda Download](https://www.anaconda.com/downloads)

• [Visual Studio Download](https://code.visualstudio.com/Download)

## Linux:
 How to install Anaconda In Linux | Create Environment | Install TensorFlow | Opencv library |
 [![How to install | Python | | Anaconda | | Opencv library |](https://yt-embed.herokuapp.com/embed?v=Mfbrxy8gK6A)](https://www.youtube.com/watch?v=Mfbrxy8gK6A "How to install Anaconda In Linux | Create Environment | Install TensorFlow | Opencv library |")

##  Windows:
How to install | Python | | Anaconda | | Opencv library |
 [![How to install | Python | | Anaconda | | Opencv library |](https://yt-embed.herokuapp.com/embed?v=eVV3byQlYvA)](https://www.youtube.com/watch?v=eVV3byQlYvA "How to install | Python | | Anaconda | | Opencv library |")

## License :
MIT Licensed

## Author :
Sujit Mandal

[GitHub](https://github.com/sujitmandal)

[PyPi](https://pypi.org/user/sujitmandal/)

[LinkedIn](https://www.linkedin.com/in/sujit-mandal-91215013a/)
