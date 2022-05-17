from datetime import datetime
class SMS_store():
    def __init__(self):
        self.Allmessages = []
        self.menu()
    def add_new_arrival(self,from_number,time_arrived,txt_of_SMS):
        old_count = self.message_count()
        newMassage = (False,from_number,time_arrived,txt_of_SMS)
        self.Allmessages.append(newMassage)
        new_count = self.message_count()
        if(new_count > old_count):
            return True
        else:
            return False
    def message_count(self):
        return f"number of messages is :  {len(self.Allmessages)}"
    def get_unread_indexes(self):
        listIndex = []
        Unread_messages = list(filter(lambda message : message[0] == False  , self.Allmessages))        
        for i in self.Allmessages:
            for j in Unread_messages :
                if(i == j):
                    listIndex.append(self.Allmessages.index(i))
        return f"index of unread messages : {listIndex}"
    def get_message(self,i):
        Select_message = self.Allmessages[i]
        try:
            print(list(self.Allmessages[i])[0])
            self.Allmessages[i] = (True,Select_message[1],Select_message[2],Select_message[3])
            return f"message is : {(Select_message[1],Select_message[2],Select_message[3])}"
        except IndexError :
            return None    
    def delete(self,i):
        try:
            if(self.Allmessages.pop(i)):
                return True
            else:
                return False
        except IndexError :
            return None
    def clear(self):
        if(self.Allmessages.clear()):
            return True
        else:
            return False
    def menu(self):
        error = True
        print('''
-------- Menu -------- 
1.Send Nnew Message
2.Message Count
3.Unread Message indexes
4.Show Message
5.Delete Message
6.Clear Inbox
7.EXIT
              ''')
        while error:
            try:
                userInput = int(input("Choise one of Items : "))
                listOfNum = [1,2,3,4,5,6,7]
                if(userInput in listOfNum): 
                    error = False
                    self.userInput(userInput)
                else:
                    error = True
            except ValueError:
                error = True
    def userInput(self,userInput):
        if(userInput == 1):
            error = True
            now = datetime.now()
            date = f"{now.month}/{now.day}/{now.year}"
            time = now.strftime("%I:%M %p")
            while error:
                try:
                    number = int(input("Write Your Number Please : "))
                    error = False
                except ValueError:
                    print("Wrong Value !!")
                    error = True
            txt = input("Write Your Text Please : ")
            time_arrived = date + " " + time
            if(self.add_new_arrival(number,time_arrived,txt)):
                print("\n message send successfully !! \n")
            else:
                print("\n message not send ! \n")
            print("||---------------------------------------||")
            print("||---------------------------------------||")
            return self.menu()
        elif(userInput == 2):
            print(self.message_count())
            print("||---------------------------------------||")
            print("||---------------------------------------||")
            return self.menu()
        elif(userInput == 3):
            print(self.get_unread_indexes())
            print("||---------------------------------------||")
            print("||---------------------------------------||")
            return self.menu()
        elif(userInput == 4):
            error = True
            while error :
                try:
                    index = int(input("Write Index of Message : "))
                    error = False
                    print(self.get_message(index))
                except ValueError:
                    error = True
            print("||---------------------------------------||")
            print("||---------------------------------------||")
            return self.menu()
        elif(userInput == 5):
            error = True
            while error :
                try:
                    index = int(input("Write Index of Message to Delete :"))
                    error = False
                    if(self.delete(index)):
                        print("\n Message Deleted successfully !! \n")
                    else:
                        print("\n Message Can Not to delete !! \n")           
                except ValueError:
                    error = True 
            print("||---------------------------------------||")
            print("||---------------------------------------||")
            return self.menu()
        elif(userInput == 6):
            Q = input("Are you sure to Clear Inbox ? (Y/N)")
            if(Q == "Y"):
                if(self.clear()):
                    print("\n Inbox is empty Now \n")
                else:
                    print("\n Error While clear the inbox ! \n")
            print("||---------------------------------------||")
            print("||---------------------------------------||")
            return self.menu()
        elif(userInput == 7):
            print("Program Close !!")

a = SMS_store()