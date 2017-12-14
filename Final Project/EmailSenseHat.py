def main():
    from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
    from imapclient import IMAPClient
    import time
    import sys
    from time import gmtime, strftime


    LOG = True
    HOSTNAME = 'imap.gmail.com'
    USERNAME = 'raspberrypiorc@gmail.com'
    PASSWORD = 'rpi12345'
    MAILBOX = 'Inbox' 
    NEWMAIL_OFFSET = 0 
    MAIL_CHECK_FREQ = 5

    sense = SenseHat()
    sense.load_image("hello.png")

    def spinning_cursor():
        while True:
            for cursor in '|/-\\':
                yield cursor
    spinner = spinning_cursor()

    print("\n\n\n############# MAIL CHECKER SYSTEM ###########")
    print("#\n#")
    print('# Login:  ' + USERNAME)
    for _ in range(50):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    try:
        server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
        server.login(USERNAME, PASSWORD)
    except:
        verif = False
        print ("Can not login check your configuration")
        sense.load_image("error.png")
    else:
        verif = True
        sense.load_image("done.png")
        select_info = server.select_folder(MAILBOX)
        print("# Connection Successful! \n#")
        print("# Press The Joystick To Quit")
        
    print('#\n#')
    print("#############################################\n")
    time.sleep(2)
                    
    if verif == True:
        sense.load_image("up.png")
        folder_status = server.folder_status(MAILBOX, 'UNSEEN')
        newmails = int(folder_status['UNSEEN'])
        
        if LOG:
                print ('You have %d new emails.' % newmails)
                    
        if newmails > NEWMAIL_OFFSET:
            nbr = str(newmails)
            msgs = (nbr)
            sense.show_message(msgs)

            if newmails == 1:
                sense.load_image("mail.png")
            elif newmails > 1 and newmails < 15:
                sense.load_image("mailFew.png")
            elif newmails > 14:
                sense.load_image("mailLot.png")
            else:
                sense.load_image("nomail.png")
            
        time.sleep(MAIL_CHECK_FREQ)
        sense.clear()
        import MasterFile
        



            


