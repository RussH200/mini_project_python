import optparse

Found = False # This variable is True if the password is found
Fails = 0 # Counts the number of failed tries

######## HELPER CODE: PLEASE DO NOT MODIFY ################
_username = "student"
_hostname = "springboard.com"
_password = "0IvInFSWrdpI9"

# This function simulates an attempted login to the host.
# If the attempt works, it sets Found to True
# Otherwise it increments Fails by 1

def connect(host, user, password):
    global Found
    global Fails
    
    if user == _username and host == _hostname and password == _password:
        print('[+] Password Found: ' + password)
        Found = True
    else:
        Fails += 1
######## END HELPER CODE ##################################


if __name__ == '__main__':
    parser = optparse.OptionParser('usage%prog -H <target host> -u <user> -F <password list>')
    parser.add_option('-H', dest="tgtHost", type="string",help='Specify target host')
    parser.add_option('-F', dest="passwdFile", type="string", help = 'Specify password file')
    parser.add_option('-u', dest="user", type="string", help = 'Specify the user')
    (options, args) = parser.parse_args()

    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user

    if host == None or passwdFile == None or user == None:
        print(parser.usage)
        exit(0)
        
    '''
	Write code to do the following:

        1) Open the password file
        2) For each password, remove any trailing whitespace
        3) Call the connect(host, user, password) function with appropriate arguments
        4) If you find the password, print a message that you've found the password, and the number of failed tries
    '''
    #### YOUR CODE HERE #####

pwordfile = 'passwords.txt'
file = open(pwordfile, mode='r')
pwlines = file.readlines() # read in all lines in file as strings assign to variable pwlines
file.close()

for line in pwlines: # for loop thru strings in password file known as variable pwlines
    line = line.strip() # This strips leading and trailing whitespace from each string on each line
    connect(host, user, line) # Call connect function with helper code arguments and for iterating line
    #print (line)
    if Found == True:
        print ('[+] Password found after' + str(Fails) + 'attempts.')
    else: print('This is to see current file line '+ line + ' and password ' + _password + ' fail number ' + str(Fails))




