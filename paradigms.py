# PROCEDURAL PARADIGM:C

# define function(arguments){

# }
# I will call it, function(data)


#Modern way...
#OBJECT ORIENTED PROGRAMING
class Customer:
    #Constructor => setting the data
    def __init__(self,name,type):
       self.name=name
       self.type=type

       if (type == "senior"):
           self.interest=7.5
       else:
           self.interest=6

    #Functions here on 
    def get_interest_on_deposit(self,principal,years):
        interest_amount = principal*years*self.interest/100
        return interest_amount
    
customer1 = Customer("indhu","normal")
customer2 = Customer("priya","senior")

print(customer1.interest,customer2.interest)
       
print(customer1.get_interest_on_deposit(10000,5))
print(customer2.get_interest_on_deposit(10000,5))

#IF IT IS IN C get_interest_on_deposit(customer1,10000,5)