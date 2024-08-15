import configparser

config = configparser.RawConfigParser()
#config.read("D:\\Credence Class Notes\\CredenceBatches\\RevisionMay2024\\CredKart_Pytest\\Configuration\\config.ini")
config.read(".\\Configuration\\config.ini")


class ReadconfigClass:

    @staticmethod
    def getEmail():
        Email = config.get('login data', 'email')
        return Email

    @staticmethod
    def getPassword():
        Password = config.get('login data', 'password')
        return Password
