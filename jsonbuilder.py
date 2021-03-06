#!/usr/bin/python -tt

import sys

def main():
    # Check that no parameters were included
    if len(sys.argv) != 2:
        print 'Usage: ./jsonbuilder.py IDnum (i.e. 64610)'
        sys.exit(1)

    # The employee ID that this program will consider to be the user
    employeeID = sys.argv[1]

    # Open "AllCommunicationList.xml", a list of email interactions of Enron employees
    f = open('AllCommunicationList.xml', 'rU')

    # Dicts to store the number of emails sent and received to/from each user. Use of this data is TBD.
    sent = {}
    received = {}
    # Dict for total emails sent/received to each user. This is used to size each node.
    totalemails = {}

    # Total emails sent/received for the user. This is used to size the middle "Me" node.
    myTotalEmails = 0

    # Load sent, received, and totalemails lists
    for line in f:
        if line[0] == ' ':
            numbers = line.split('"')

            if numbers[1] == employeeID:
                sent[numbers[3]] = numbers[5]
                myTotalEmails += int(numbers[5])
                if numbers[3] in totalemails:
                    totalemails[numbers[3]] = int(totalemails[numbers[3]]) + int(numbers[5])
                else:
                    totalemails[numbers[3]] = numbers[5]

            elif numbers[3] == employeeID:
                received[numbers[1]] = numbers[5]
                myTotalEmails += int(numbers[5])
                if numbers[1] in totalemails:
                    totalemails[numbers[1]] = int(totalemails[numbers[1]]) + int(numbers[5])
                else:
                    totalemails[numbers[1]] = numbers[5]
    f.close()


    # Open "AddressList.xml", a list of emails and email ID numbers
    f = open('AddressList.xml', 'rU')
    # Dict to store addresses
    addresses = {}

    # Store the address for each email ID
    for line in f:
        if line[0] == ' ':
            addressline = line.split('"')
            if addressline[3] in totalemails or addressline[3] == employeeID:
                addresses[addressline[3]] = addressline[1]
    f.close()


    # Open json file to write to
    fw = open('emaildata.json', 'w')

    fw.write('{\n  "nodes":[\n    {"name":"Me (' + addresses[employeeID] + ')","group":1, "total":' + str(int(myTotalEmails)/1000 + 5) + '},\n')

    # Write each node
    num = 1
    for item in totalemails:
        if num == len(totalemails):
            fw.write('    {"name":"' + addresses[item] + '","group":' + str(num+1) + ',"total":' + str(int(totalemails[item])/100 + 5) + '}\n')
        else:
            fw.write('    {"name":"' + addresses[item] + '","group":' + str(num+1) + ',"total":' + str(int(totalemails[item])/100 + 5) + '},\n')
        num = num + 1

    fw.write('  ],\n  "links":[\n')

    # Write each link
    num = 1
    for item in totalemails:
        if num == len(totalemails):
            fw.write('    {"source":0,"target":' + str(num) + ',"value":2}\n')
        else:
            fw.write('    {"source":0,"target":' + str(num) + ',"value":2},\n')
        num = num + 1

    fw.write('  ]\n}')

    fw.close()

if __name__ == '__main__':
    main()
