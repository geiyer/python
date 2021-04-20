def calculate_single_tax(income):
    if(0 < income < 9875 ):
            return 0.1 * income
    elif (9976 < income < 40125):
            return 0.12 * income    
    elif (40126 < income < 85525):
            return 0.22 * income 
    elif (85526 < income < 163300):
            return 0.24 * income 

def calculate_tax(status, income):
    if status == 'single':
        return calculate_single_tax(income)

def calculate_taxes(status, incomes):
    taxes = {}    
    for i in incomes:        
        tax = calculate_tax(status, i)        
        taxes[i] = tax
    return taxes    