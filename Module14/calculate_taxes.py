class calculate_taxes():

        def calculate_single_tax(self, income):
                if(0 < income < 9875 ):
                        return 0.1 * income
                elif (9976 < income < 40125):
                        return 0.12 * income    
                elif (40126 < income < 85525):
                        return 0.22 * income 
                elif (85526 < income < 163300):
                        return 0.24 * income 
                elif (163301 < income < 500000):
                        return 0.30 * income         


