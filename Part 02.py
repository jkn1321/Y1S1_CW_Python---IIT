#I declare that my work contains no examples of misconduct, such as plagarism,or collusion.
#Any code taken from other sources is referenced within my code solution.
#Student ID: 
#Date: 31/03/2023

#Part 1

while True:
    #Selecting the version
    version = input("Which version would you want?\nEnter 's' for student version or 't' for staff version\nEnter the version: ").lower()
    print()

    if version == "s":
        print("Student version.")
        def check_the_validity(message):
            while True:
                try:
                    volume_of_credits = int(input(message))
                    if volume_of_credits % 20 == 0 and 0<= volume_of_credits<=120:
                        break
                    else:
                        print("Out of range.")
                        print()
                        continue
                except ValueError:
                    print("Integer required.")
                    print()
            return volume_of_credits

        while True:
            Pass = check_the_validity("Please enter your credits at pass: ")
            Defer = check_the_validity("Please enter your credits at defer: ")
            Fail = check_the_validity("Please enter your credits at fail: ")

            #Checking the total
            if Pass + Defer + Fail != 120:
                print("Total incorrect. ")
                print()
                continue

            else:
                #Checking the outputs
                if Pass == 120:
                    print("Progress")
                elif Pass == 100:
                    print("Progress (module trailer)")
                elif 0 <= Pass <=80 and 0<= Fail <= 60:
                    print("Module retriever")
                else:
                    print("Exclude")
            print()

    elif version == "t":
         print("Staff version. ")
         def check_the_validity(message):
            while True:
                try:
                    volume_of_credits = int(input(message))
                    if volume_of_credits % 20 == 0 and 0<= volume_of_credits<=120:
                        break
                    else:
                        print("Out of range.")
                        print()
                        continue
                except ValueError:
                    print("Integer required.")
                    print()
            return volume_of_credits

         def selection():
            while True:
                #Selecting whether the program will continue or quit
                option = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view resuts: ").lower()
                if option == "y":
                    return True
                elif option == "q":
                    return False
                else:
                    print("Please enter a valid option.")
                    print()

         Progress_count  = 0
         Trailer_count   = 0
         Retriever_count = 0
         Excluded_count  = 0
         Progress_list   = []
         Trailer_list    = []
         Retriever_list  = []
         Excluded_list   = []
         

         while True:
            Pass = check_the_validity("Enter your total PASS credits: ")
            Defer = check_the_validity("Enter your total DEFER credits: ")
            Fail = check_the_validity("Enter your total FAIL credits: ")
            
            #Checking the total
            if Pass + Defer + Fail != 120:
                print("Total incorrect. ")
                print()
                continue

            else:
                #Checking the outputs
                if Pass == 120:
                    print("Progress")
                    Progress_count += 1
                    Progress_list.append([Pass, Defer, Fail])
                    
                elif Pass == 100:
                    print("Progress(module trailer)")
                    Trailer_count += 1
                    Trailer_list.append([Pass, Defer, Fail])
                    
                elif 0 <= Pass <=80 and 0<= Fail <= 60:
                    print("Module retriever")
                    Retriever_count += 1
                    Retriever_list.append([Pass, Defer, Fail])
                    
                else:
                    print("Exclude")
                    Excluded_count += 1
                    Excluded_list.append([Pass, Defer, Fail])
                    
            print()

            option = selection()
            print()
            if option == False:
                break
         print()

         #Histogram
         print("-" * 70)
         print("Histogram")
         print("Progress", Progress_count, ":", Progress_count * "*" )
         print("Trailer", Trailer_count, ":", Trailer_count * "*" )
         print("Retriever", Retriever_count, ":", Retriever_count * "*" )
         print("Excluded", Excluded_count, ":", Excluded_count * "*" )
         print()
         print((Progress_count + Trailer_count + Retriever_count + Excluded_count),"outcomes in total.")
         print("-" * 70)
         print()
         
    else:
         print("Please enter a valid version.")
         print()
         continue

#Part 2
    print("Part 2")
    for item in Progress_list:
        print(f"Progress - {', '.join(str(i) for i in item)}")

    for item in Trailer_list:
        print(f"Trailer - {', '.join(str(i) for i in item)}")

    for item in Retriever_list:
        print(f"Retriever - {', '.join(str(i) for i in item)}")

    for item in Excluded_list:
        print(f"Excluded - {', '.join(str(i) for i in item)}")

    print()
        
         
