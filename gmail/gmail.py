__author__ = 'Sujit Mandal'
#Date : 07-09-2020
import smtplib 

'''
# Author : Sujit Mandal
Github : https://github.com/sujitmandal
Pypi : https://pypi.org/user/sujitmandal/
LinkedIn : https://www.linkedin.com/in/sujit-mandal-91215013a/
'''

#E-mail login credential
gmail_id = ('') #sender g-mail id
password = ('') #sender g-mail password

#reciver mail id's 
reciver_mail_id = [
                    'reciver_mail_id_1@gmail.com',
                    'reciver_mail_id_2@gmail.com',
                    'reciver_mail_id_3@gmail.com',
                    '............................',
                    '.............................',
                    'reciver_mail_id_N number@gmail.com',
                    ]
#main subject
subject = ('') #mail subject
#mail contain
mail_contain = ('') #mail contain


class loginCredential:
    def login(self,gmail_id, password):
        self.gmail_id = gmail_id
        self._password = password

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.gmail_id, self._password) 
        return(server)

class reciverCredential(loginCredential):
    def reciver_mail(self, reciver_mail_id):
        self.reciver_mail_id =reciver_mail_id

        mail_id = []
        for i in reciver_mail_id:
            mail_id.append(i)
        return(mail_id)

class gmail(reciverCredential):
     def send_mail(self, subject, mail_containt):
        server = self.login(self.gmail_id, self._password)
        reciver_mail_id = self.reciver_mail(self.reciver_mail_id)

        containt = (f'subject: {subject}\n\n{mail_containt}')

        server.sendmail(
            self.gmail_id, 
            reciver_mail_id, 
            containt
        )
        if len(reciver_mail_id) == 1:
            print('Mail has been sent to this : {}'.format(reciver_mail_id),'Address.')
        else:
            print('Mail has been sent to these : {}'.format(reciver_mail_id),'Address.')
        server.quit()

   

if __name__ == '__main__':
    mail = gmail()
    mail.login(gmail_id, password)
    mail.reciver_mail(reciver_mail_id)
    mail.send_mail(subject, mail_contain)