
#MODULE : LIBRARY MANAGEMENT

import Menulib as ml
while True:
    print("\t\t\t Library Management\n")
    print("==============================================================")
    print("1. Book Management ")
    print("2. Members Management s ")
    print("3. Issue/Return Book ")
    print("4. Exit ")
    print("===============================================================")
    choice=int(input("Enter Choice between 1 to 4-------> : "))
    if choice==1:
        ml.MenuBook()
    elif choice==2:
        ml.MenuMember()
    elif choice==3:
        ml.MenuIssueReturn()
    elif choice==4:
        break
    else:
        print("Wrong Choice......Enter Your Choice again")
    #x=input("Enter any key to continue")
#print("\033[H\033[J")