import constants

print('First Line: file a')
def my_function(paramA):
    """The function is loaded but not executed. 
    The function will be executed only after it is invoked.
    """
    print('function invoked')

def my__another_function(paramB):
    """The function is loaded but not executed. 
    The function will be executed only after it is invoked.
    """
    print('function invoked')

    
if __name__ =='__main__':
    print('Inside Main: File A')
    print(__name__)

    my_function('A')
    my__another_function('B')