reminder = {}



while True:
    def date():
        question = input('What is the date range you looking? ')
        if question not in reminder:
            print()
            print('The date you looking is not in the list')
            print()
            print('Please enter in the dd/mm/yyyy format otherwise the date is not added.')
            print()
            print('Please enter the date and add reminders if needed.')
            print()
            return index()
        else:
            ret = reminder[question]['reminders']
            print()
            print(question)
            print()
            for i, search in enumerate(ret,1):
                print(i, search)

    def date1():
        
        while True:
            items = []
            state = []
            date = input('What is the date you wanted to add reminder? ')
            
            if date == '0':
                return index()
            else:
                while True:
                
                    remi = input('What is the reminder you wanted to add? ')

                    if remi == '0':
                        reminder[date] = {'reminders': items, 'status': state}
                        break
                    else:
                        items.append(remi)
                        state.append('Not Completed')
                        

    def date2():
        while True:
            date = input('What date range status are you looking for? ')
            if date not in reminder:
                print()
                print('The date you looking is not in the list')
                print()
                print('Please enter in the dd/mm/yyyy format otherwise the date is not added.')
                print()
                print('Please enter the date and add reminders if needed.')
                print()
                return index()
            else:
                info = reminder[date]
                print()
                print(date)
                print()

                for i in range(len(info['reminders'])):
                    print(f"{info['reminders'][i]} - {info['status'][i]}")
                    print()
                        

    def index():
        while True:
            print()
            print('[1 - To see reminders]')
            print('[2 - To add reminders]')
            print('[3 - To add reminders with status]')
            print()
            what = input('What would like to do for today? ')

            if what == '1':
                return date()
            elif what == '2':
                return date1()
            elif what == '3':
                return date2()
            else:
                print()
                print('The index you have entered, is not valid. Please try again.')
                return index()
    index()
