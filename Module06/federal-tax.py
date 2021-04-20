# def calculate_tax(income, status):
#     if(income <= 9875 and status  =='single') or (income <= 19750 and status == 'married'):
#         return 0.1
#     elif (9876 < income <= 40125 and status  =='single') or (19751<= income <= 80250 and status == 'married'): 
#         return 0.12
#     else :
#         return 0.22


# if __name__ == '__main__':
#     income = int(input('Income Please, Enter -1 to exit '))
#     tax_amount = income * calculate_tax(income, 'single')    
#     print(f'Your tax amount is : {tax_amount}')















def calculate_tax(income):
    def calculate_tax_single():
        if(income <= 9875):
            return income * 0.1
        elif(9876 < income <= 40125):
            return income * 0.12
        else:
            return income * 0.22

    def calculate_tax_married():
        if(income <= 19750):
            return income * 0.1
        elif(19751 < income <= 80250):
            return income * 0.12
        else:
            return income * 0.22   

    return f'Taxes (Single): {calculate_tax_single()} and (Married): {calculate_tax_married()}'                        


if __name__ == '__main__':
    income = int(input('Income Please, Enter -1 to exit '))
    print(calculate_tax(income))