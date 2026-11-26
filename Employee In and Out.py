# Create Class
class Employee:

    # Initializing
    def __init__(self):
        print('Employee Created')

    # Calloing Destructor
    def __del__(self):
        print("Destructor Called")

def Create_Obj():
    print('Making Object...')
    obj = Employee()
    print('Function End...')
    return obj

print('Calling Create_Obj() function...')
obj1 =   Create_Obj()
print('Program End...')
