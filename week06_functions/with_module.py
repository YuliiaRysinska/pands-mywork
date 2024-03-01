# this uses modult to breake up the code
#main program

import studentUtil as su

students = []

choice = su.displayMenu()
while(choice != 'q'):
 # we could do this with lamda functions
 # I am keeping this basic for the moment
 if choice == 'a':
    su.doAdd(students)
 elif choice == 'v':
    su.doView(students)
 elif choice !='q':
   print("\n\nplease select either a,v or q")
 choice = su.displayMenu()
   