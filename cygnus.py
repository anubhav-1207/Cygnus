import colorama 
from colorama import init, Fore, Style

init(autoreset=True)

variables = {}

def run_cygnus_shell():
    cygnus_art = Fore.CYAN + r'''
                
  ______                                                         
 /      \                                                        
|  $$$$$$\ __    __   ______   _______   __    __   _______      
| $$   \$$|  \  |  \ /      \ |       \ |  \  |  \ /       \     
| $$      | $$  | $$|  $$$$$$\| $$$$$$$\| $$  | $$|  $$$$$$$     
| $$   __ | $$  | $$| $$  | $$| $$  | $$| $$  | $$ \$$    \      
| $$__/  \| $$__/ $$| $$__| $$| $$  | $$| $$__/ $$ _\$$$$$$\     
 \$$    $$ \$$    $$ \$$    $$| $$  | $$ \$$    $$|       $$     
  \$$$$$$  _\$$$$$$$ _\$$$$$$$ \$$   \$$  \$$$$$$  \$$$$$$$      
          |  \__| $$|  \__| $$                                   
           \$$    $$ \$$    $$                                   
            \$$$$$$   \$$$$$$                                             
'''
    print(Style.BRIGHT + cygnus_art)

#Errors : 
def ass_error():
    print(Fore.RED+'!!! ~ Assignment Error')

def name_error():
    print(Fore.RED+f'!!! ~ Name Error')

def opr_error():
    print(Fore.RED+'!!! ~ Operation Error')

def zero_div():
    print(Fore.RED+'!!! ~ Zero Division Error')

def format_error():
    print(Fore.RED+'!!! ~ Format Error')

    

username = input("!!! ~ Username required to initialize Cygnus session. Please input desired identifier : ")

run_cygnus_shell()



while True:
    command = input(Fore.BLUE + f'{username}' + Fore.WHITE+'@cygnus:~$ ' + Fore.CYAN)
    if command == 'exit':
        break

    parts = command.split()


    # Set Command
    if parts[0] == 'set':
        if len(parts) == 4 and parts[2] == '=' and parts[3].isdigit():
            var_name = parts[1]
            value = int(parts[3])
            variables[var_name] = value     

        else:
            ass_error()

    

    # Print Command
    elif len(parts) == 2 and parts[0] == 'print':
        var_name = parts[1]
        if var_name in variables : 
            print(variables[var_name])

        else:
            name_error()

    # Add command
    elif parts[0] == 'add':
        if len(parts) == 3 and parts[1] in variables and parts[2].isdigit():
            value = int(parts[2])
            var_name = parts[1]
            variables[var_name] += value

        else:
            opr_error()

    # Sub Command
    elif parts[0] == 'sub':
        if len(parts) == 3 and parts[1] in variables and parts[2].isdigit():
            value = int(parts[2])
            var_name = parts[1]
            variables[var_name] -= value

        else:
            opr_error()
            
    # Mul Command
    elif parts[0] == 'mul':
        if len(parts) == 3 and parts[1] in variables and parts[2].isdigit():
            value = int(parts[2])
            var_name = parts[1]
            variables[var_name] *= value

        else:
            opr_error()
    # Div Command
    elif parts[0] == 'div':
        if len(parts) == 3 and parts[1] in variables and parts[2].isdigit():
            value = int(parts[2])
            var_name = parts[1]

            if value == 0:
                print(Fore.RED + '!!! ~ Math Error: Cannot divide by zero')
            else:
                variables[var_name] //= value
        else:
            ass_error() if not parts[2].isdigit() else name_error()

    # List Command
    elif parts[0] == 'list':
        if len(parts) == 1 :
            if variables:
                print(Fore.LIGHTMAGENTA_EX+'>>> Variables : ')
                for var_name,value in variables.items():
                    print(f'{var_name} = {value}')

            else:
                name_error()

    # Del Command
    elif parts[0] == 'del':
        if len(parts) == 2 and parts[1] in variables:
            del variables[var_name]

        else:
            name_error()
    
        
    # Clear Command
    elif parts[0] == 'clear':
        if len(parts) == 1 and variables:
            variables.clear()

        else:
            name_error()

    # Help Command
    elif parts[0] == 'help':
        if len(parts) == 1:
            print(Fore.LIGHTGREEN_EX + '''
    >>> Cygnus Help Menu:

    set <var> = <value>      : Create a new variable
    print <var>              : Display a variable's value
    add <var> <number>       : Add number to variable
    sub <var> <number>       : Subtract number from variable
    mul <var> <number>       : Multiply variable by number
    div <var> <number>       : Integer divide variable (0 not allowed)
    del <var>                : Delete a specific variable
    clear                    : Delete all variables
    list                     : Show all variables and values
    exit                     : Exit the Cygnus shell
    help                     : Show this help menu
    ''')
        else:
            format_error()

    #Rename Command
    elif parts[0] == 'rename':
        if len(parts) == 3:
            new = parts[2]
            old = parts[1]
            
            if old in variables:
                if new not in variables:
                    variables[new] = variables[old]
                    del variables[old]

                else:
                    ass_error()

            else:
                name_error()

        else:
            format_error()



