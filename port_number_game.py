'''
This is a short command line game 
to help test knowledge of common ports
and protocols. Please feel free to copy
and use this game to help you study!

'''
import random 

def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


def pickport(ports):
    ports_list = list(ports.values())
    return ports_list[random.randint(0,len(ports.values())-1)]


def play_round():
    protocol = pickport(portdict)
    guess = input("enter the port number of " + protocol + "... ")
    correct_answer = get_key(protocol,portdict)
    if guess == correct_answer:
        print("Correct")
        return 1
    else:
        print("Wrong! The correct answer is " + correct_answer)
        return -1


def game():
    score = 0
    keep_playing = 'y'
    while keep_playing == 'y':
        score += play_round()
        print("Your score is " + str(score))
        keep_playing = input("Would you like to keep playing? y or n... ")
        if keep_playing != 'y' or keep_playing != 'n':
            keep_playing = input("Sorry, I'm not sure what you meant. Please type either y or n... ")


portdict = {
    "TCP80":"http",
    "TCP443":"https",
    "TCP20, TCP21":"ftp",
    "TCP22":"ssh, sftp",
    "TCP143":"imap",
    "TCP110":"pop3",
    "TCP25":"smtp",
    "TCP23":"telnet",
    "TCP3389":"rdp",
    "UDP5060":"sip",
    "UDP53":"dns",
    "UDP67, UDP68":"dhcp",
    "TCP389":"ldap",
    "UDP161, UDP162":"snmp",
    "TCP445":"smb",
    "UDP69":"tftp",
    "UDP123":"ntp",
    "TCP636":"ldaps",
    "UDP5060, UDP5061":"sip",
    "TCP137, TCP139":"netbios",
    "TCP5004, TCP5005":"rtp",
    "TCP1720":"h.323"
}


game()


