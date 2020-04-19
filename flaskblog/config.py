import os

class Config:
    SECRET_KEY = '2bd2601361ee7a151175024abc9bc935'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' #os.environ.get('SQLALCHEMY_DATABASE_URI') #'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')