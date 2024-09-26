from DBhelper import DBHelper
import msvcrt
import sys


def getch(command):
    print(command)
    return msvcrt.getch().decode()

class Youtube_App:

    def __init__(self):

        self.db=DBHelper()

        self.menu()
    
    def menu(self):

        option=getch('''
            Menu\n
            1.Insert a Video Details\n
            2.Display a Video Details\n
            3.Update a Video Details\n
            4.Delete a Video Details\n
            5.Exit\n
            option : 
            ''')
        match option:

            case '1':
                self.Insert_details()
            case '2':
                self.Display_details()
            case '3':
                self.Update_details()
            case '4':
                self.Delete_details()
            case '5':
                sys.exit(1000)

    def Insert_details(self):

        name=input("Enter the name of the video : ")
        time=input("Enter the time of the video : ")
        link=input("Enter the link of the video : ")
        self.db.Insert(name=name,time=time,link=link)

        self.menu()
    def Update_details(self):
        id = input('Enter the id of the video: ')
        name=input("Enter the name of the video : ")
        time=input("Enter the time of the video : ")
        link=input("Enter the link of the video : ")
        self.db.Update(name=name,time=time,link=link,id=id)

        self.menu()
    def Delete_details(self):
        id = input('Enter the id of the video: ')
        self.db.Delete(id=id)

        self.menu()
    def Display_details(self):

        id = input('Enter the id of the video: ')
        data = self.db.Display(id=id)
        
        if data:  # Check if data is not None
            print('\nName: ', data['name'], ', \nTime: ', data['time'], ', \nLink: ', data['link'])
        else:
            print("No details found for the given key.")
        self.menu()

obj=Youtube_App()