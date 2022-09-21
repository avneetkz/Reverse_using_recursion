# function for reversing string using recursion 

def rev_recursion(str):
    if not str:
        return ' '
    else:
        return str[::-1] 
''' or we can write
        return (rev_recursion(str[1::]) + str[0]) '''
    
# driver code   

if __name__ == "__main__":
    str = input("Enter a string you want to reverse: ")
    print(f'{str} after reversing is {rev_recursion(str)}')
        
