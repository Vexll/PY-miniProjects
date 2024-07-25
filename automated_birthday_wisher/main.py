# SMTP: Simple Mail Transfer Protocol
import smtplib


def main():
    my_email = 'ali.vexll0@gmail.com'
    my_pass = ''

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  # making the connection secure
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs='testing@gmail.com', msg='hello world!')


if __name__ == '__main__':
    main()
