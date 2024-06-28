#this program is about calculating interest
#principal = 100000    #100000 is assigned to pricipal which doesn't mean that are equal
#rate_of_interest = 7 # assinging values
#num_of_years = 5 # assinging values
principal = float(input("Enter principal amount: "))#converting the enteredcvalues to float
rate_of_interest = float(input("Enter rate of interest: "))

num_of_years = float(input("Enter number of years: "))

choice = int(input("\n What interest you want?\n1.Simple Interest\n2.Compound Interest\n"))
#Branching
if choice ==1:
    #simple interest calculation
    simple_interest_amount = (principal*rate_of_interest*num_of_years)/100  # doing arithmetic operation 

    print("Simple Interest: ", simple_interest_amount) # for displaying many values in a single line use ,
elif choice==2:
    #compound interest calculation
    compound_interest = principal*(1+rate_of_interest/100)**num_of_years - principal
    print("Compound  Interest: ", compound_interest)
else:
    print("Read the instructions properly!Try again next time\n")