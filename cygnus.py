from flask import Flask, request, render_template_string

app = Flask(__name__)
variables = {}
chat_history = []

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Cygnus Terminal</title>
    <style>
        body { background: black; color: lime; font-family: monospace; padding: 20px; }
        input { background: black; color: lime; border: none; font-size: 16px; width: 100%; }
    </style>
</head>
<body>
    <h2>Welcome to Cygnus Web Terminal</h2>
    <form method="POST">
        <input name="user_input" placeholder="Enter a command..." autofocus autocomplete="off" />
    </form>
    <pre>{{ chat }}</pre>
</body>
</html>
'''

def process_command(command):
    parts = command.strip().split()

    if not parts:
        return "Invalid command."

    if parts[0] == 'set':
        if len(parts) == 4 and parts[2] == '=' and parts[3].isdigit():
            variables[parts[1]] = int(parts[3])
            return f"Set {parts[1]} = {parts[3]}"
        return "!!! ~ Assignment Error"

    elif parts[0] == 'print':
        if len(parts) == 2 and parts[1] in variables:
            return f"{parts[1]} = {variables[parts[1]]}"
        return "!!! ~ Name Error"

    elif parts[0] in ('add', 'sub', 'mul', 'div'):
        if len(parts) == 3 and parts[1] in variables and parts[2].isdigit():
            var = parts[1]
            num = int(parts[2])
            if parts[0] == 'add':
                variables[var] += num
            elif parts[0] == 'sub':
                variables[var] -= num
            elif parts[0] == 'mul':
                variables[var] *= num
            elif parts[0] == 'div':
                if num == 0:
                    return '!!! ~ Math Error: Cannot divide by zero'
                variables[var] //= num
            return f"{parts[0]} successful: {var} = {variables[var]}"
        return "!!! ~ Operation Error"

    elif parts[0] == 'list':
        if variables:
            return "\n".join(f"{k} = {v}" for k, v in variables.items())
        return "No variables defined."

    elif parts[0] == 'del':
        if len(parts) == 2 and parts[1] in variables:
            del variables[parts[1]]
            return f"Deleted {parts[1]}"
        return "!!! ~ Name Error"

    elif parts[0] == 'clear':
        variables.clear()
        return "All variables cleared."

    elif parts[0] == 'rename':
        if len(parts) == 3 and parts[1] in variables and parts[2] not in variables:
            variables[parts[2]] = variables.pop(parts[1])
            return f"Renamed {parts[1]} to {parts[2]}"
        return "!!! ~ Rename Error"

    elif parts[0] == 'help':
        return '''Cygnus Help Menu:

set <var> = <value>      : Create a new variable
print <var>              : Display a variable's value
add <var> <number>       : Add number to variable
sub <var> <number>       : Subtract number from variable
mul <var> <number>       : Multiply variable by number
div <var> <number>       : Integer divide variable (0 not allowed)
del <var>                : Delete a specific variable
clear                    : Delete all variables
list                     : Show all variables
rename <old> <new>       : Rename a variable
exit                     : Quit the shell (not needed here)'''

    elif parts[0] == 'exit':
        return "Cygnus session ended. Refresh to restart."

    return "!!! ~ Format Error"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        chat_history.append(f"You: {user_input}")
        response = process_command(user_input)
        chat_history.append(f"Cygnus: {response}")
    return render_template_string(HTML_TEMPLATE, chat="\n".join(chat_history))

if __name__ == '__main__':
    app.run(debug=True)
