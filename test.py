__author__ = 'student'
Numbers=[]
Names=[]
option =0
while True:
    print "---------------------------------------"
    option = raw_input("Enter the number of the Option you want:"+
                "\n----------------------------------------"+
                "\n| 1 | To Add Contact"+
               "\n| 2 | To search for the Contact by the Name\n| 3 | To search the Contact by the Number"+
               "\n| 4 | To Edit the Contact\n| 5 | To print the Address book\n| 6 | To quit\n"+
                "----------------------------------------\n>")

    if option == "1":
        print "-------------"
        print "Add Contacts!\n-------------"
        name = raw_input("Enter name :")
        Names.append(name)
        number = input("Enter number :")
        Numbers.append(number)

    elif option == "2":
        print "\nSearch Contact by the Name\n--------------------"

        name = raw_input("Enter the name :")
        if name in Names:
            print "The Contact are listed Below"
            print "-----------------------------"
            index = Names.index(name)
            #print "I am rprinting index",index
            print "Name   :", Names[index]
            print "Number : ", Numbers[index]


        elif name not in Names:
            print "\nThis Contact Does Not Exist!!\n----------------------\n"

    elif option == "3":
        print "\nSearch Contact by the Number\n----------------------------"
        number = input("Enter the number :")
        if number in Numbers:
            print "\n---------------------------"
            print "The Contact are listed Below"
            index = Numbers.index(number)
            #print "I am rprinting index",index

            print "\nThe Number : ", Numbers[index]
            print "Belongs to :", Names[index]
            print "----------------------------"

        elif number not in Numbers:
            print "\nThis Contact Does Not Exist!!\n-------------------\n"

    elif option == "4":
        print "\nEdit the Contact!\n------------------\n"

        name = raw_input("Enter Contact Name to Edit:\n->")
        if name not in Names:
            print "\nThis Name Does not exist!\n"

        elif name in Names:
            index = Names.index(name)
            #print "WE are removing item no",index
            Names.remove(name)
            del Numbers[index]


            print "--------------------"
            print "Entering New Contact\n------------------\n"
            name = raw_input("Enter New Name :")
            Names.append(name)
            number =input("Enter New Number :")
            Numbers.append(number)
            print "\n----------------"
            print "Contact Added!!\n--------------\n"

    elif option =="5":
        print "----------------------------"
        print "Printing the Address book\n-----------------------"

        for i in range(len(Names)):
            print str(Names[i]) + "........"+ str(Numbers[i])
        #print Names
        #print Numbers
        print "--------------------"
    elif option == "6":
        print "Bye"
        break
