def calculate_tax(income, status):
    if(income <= 9875 and status  =='single') or (income <= 19750 and status == 'married'):
        return 0.1
    elif (9876 < income <= 40125 and status  =='single') or (19751<= income <= 80250 and status == 'married'): 
        return 0.12
    else :
        return 0.22


if __name__ == '__main__':
    SENTINAL_VALUE = -1
    income = 0
    tax_amount = 0
    while income != SENTINAL_VALUE:
        income = int(input('Income Please, Enter -1 to exit '))
        if(income == SENTINAL_VALUE): 
            break
        status = input('single or married ')        
        tax_amount = income * calculate_tax(income, status)    
        print(f'Your tax amount is : {tax_amount}')