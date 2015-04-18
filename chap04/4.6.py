# coding: utf-8

nameHandle = open('kids', 'w')
for i in range(2):
    name =  raw_input('Enter name: ')
    nameHandle.write(name + '\n')
nameHandle.close()
nameHndle = open('kids', 'r')
for line in nameHandle:
    print line
nameHandle.close()
