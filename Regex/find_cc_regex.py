import optparse
import re


if __name__ == '__main__':
    parser = optparse.OptionParser('usage%prog -F <CC file>')
    parser.add_option('-F', dest="ccFile", type="string", help = 'Specify file with CC numbers')
    (options, args) = parser.parse_args()
    ccFile = options.ccFile

    if ccFile == None:
        print(parser.usage)
        exit(0)
        
    '''
        1) Open the file with potential credit card numbers, one on each line
        2) For each number, remove any trailing whitespace
        3) Create a regular expression to identify a valid credit card number
        4) Go through the file and print the total number of valid credit card numbers that you've found
    '''
    #### YOUR CODE HERE #####

ccnumfile = 'ccnumbers.txt'
file = open(ccnumfile, mode='r')
cclines = file.readlines() # read in all lines in file as strings assign to variable cclines
file.close() # always close file after use

ccNum = r'^(\d{16})|(\d{4}[-]\d{4}[-]\d{4}[-]\d{4})$'
ccCount = 0

for line in cclines: # for loop thru strings in ccnumbers file known as variable cclines
    line = line.rstrip() # This strips trailing whitespace from each string on each line
    ccMatch = re.match(ccNum, line) # perform regex matching on each line

    if ccMatch: # if match found print cc number and add to ccCount
        print (line)
        ccCount += 1

print('There are ' + str(ccCount) + ' valid credit card numbers found' )
