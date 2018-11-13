import os
while True:

    print()
    print('       ******Welcome****** \n Let\'s know about cryptocurrency' )
    #print('The global market cap is $' + global_cap_string)
    print()
    print('1 - To get your portfolio')
    print('2 - To have customised alert for the cryptocurrency')
    print('3 - To rank the cryptocurrency')
    print('4 - To get future market value of cryptocurrency')
    print('5 - To have a excel file storing data regarding cryptocurrency')
    print('0 - Exit')
    print()
    choice = input('What is your choice? (1-5): ')

    if choice == '1':
        os.system('python portfolio.py')
    if choice == '2':
        os.system('python alert.py')
    if choice == '3':
        os.system('python rankingcryptocurrency.py')
    if choice == '4':
        os.system('python futurevalue.py')
    if choice == '5':
        os.system('python storinginexcel.py')
    if choice == '0':
        break
    choice = input('Again? (y/n): ')
    if choice == 'n':
        break
