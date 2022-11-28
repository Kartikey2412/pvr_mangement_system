import re
class user_info:

     global dict_info
     list_booked_seats=[]
     myfile=open("info.txt","w+")
     def user(self,book_row,book_column):
        dict_info = {"Name": "", "Gender": "", "Age": int, "Phone_no": int}

        name=input("Enter the Name: ")
        na = re.fullmatch("[a-zA-Z]{1,15}", name)
        while(na==None):
            print("Invalid Name Please try Again \n")
            name=input("Enter the Name: ")
            na = re.fullmatch("[a-zA-Z]{1,15}", name)

        gender=input("Enter your Sex: ")
        while(gender != "male" and gender!="female"):
            print("Invalid gender Please try Again")
            gender=input("Enter your Sex: ")


        Age=int(input("Enter your Age: "))
        while(Age<=0 or Age>100):
            print("Invalid Age Please Try Again")
            Age=int(input("Enter your Age: "))

        phone_no=input("Enter your Phone number: ")

        
        for i in range(10):
            mat = re.fullmatch("[0-9]{10}", phone_no)
            if mat != None:

                dict_info["Name"] = name
                dict_info["Gender"] = gender
                dict_info["Age"] = Age
                dict_info["Phone_no"] = phone_no

                list1 = [book_row, book_column, dict_info]
                user_info.list_booked_seats.append(list1)
                


                print("CONGRATS!!! Booked Successfully")
                break
            else:
                print("Invalid Phone Number!!!")
                phone_no = input("Please Enter Valid Mobile Number: ")
    
    
     def show_seats(self):
        for i in user_info.list_booked_seats :
              print (i,"\n") 


     def booked_tickets_user_info(self,row_c,column_c,current_income):

        if len(user_info.list_booked_seats)>0 :
            for i in range(len(user_info.list_booked_seats)):
                if (user_info.list_booked_seats[i][0]==row_c and user_info.list_booked_seats[i][1]==column_c):

                    print("Name: ",user_info.list_booked_seats[i][2].get("Name"))
                    print("Gender: ", user_info.list_booked_seats[i][2].get("Gender"))
                    print("Age: ", user_info.list_booked_seats[i][2].get("Age"))
                    print("Phone Number: ", user_info.list_booked_seats[i][2].get("Phone_no"))
                    print("Ticket Price :",current_income,'$')
                    break
            else:
                print("Seat is vacant")

        else:
            print("Seat is Empty")







