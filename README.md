# Cygnus
## What is Cygnus?

Cygnus is a simple, customizable, command-line-based code interpreter — written entirely in Python — that simulates a small programming language and terminal environment.

It allows the user to interact with a virtual shell by typing plain-English commands like:

```
set x = 10
add x 5
print x
```

Behind the scenes, Cygnus uses basic Python tools — such as dictionaries, loops, conditionals, and string parsing — to process these commands and simulate how a real programming language or shell works.

---

## ⚙️ How It Works (in simple terms)

**1. Text Input:** Cygnus takes input from the user using ```input()```, just like a normal Python program.


**2. Command Parsing:** It breaks down what the user typed using ```.split()``` — for example:

```
command = "set x = 5"
parts = command.split()  # ['set', 'x', '=', '5']
```

**3. Command Recognition:** Cygnus checks what the first word is ```(like set, print, add, etc.).``` It compares it against known commands and then runs the matching block of code.


**4. Variable Storage:** All user-defined variables (like x, y, etc.) are stored in a Python dictionary named ```variables```. That’s how Cygnus "remembers" values.

```variables = {'x': 10, 'y': 3}```


**5. Operations:** If you use a math command like ```add x 5```, Cygnus will:
i. Find the value of x inside variables
ii. Add 5 to it
iii. Update x with the new result



**6. Output:** Cygnus uses print() and colorama to display results or errors in colorful terminal text, just like a real Linux shell.




---

## Why Cygnus is Special (Even Though It's Simple)

It’s not just a calculator — it mimics how programming languages store, manipulate, and interact with data.

It’s written in pure Python, using only the basics — no heavy modules, no complex syntax.

It looks and feels like a shell, making beginners feel like they’re building their own OS or interpreter.


## 👶 Made for Beginners — Teaches You:

1. How interpreters and shells work

2. How to process user input

3. How to handle variables and operations

4. How to give meaningful error messages

5. How to structure clean code with functions

---

## What Can Cygnus Do?

Cygnus might look simple — but it’s a fully working mini-interpreter built from the ground up. It mimics some of the core behavior of a real programming language or terminal environment.

Here’s what it can do right now:


---

**📝 Variable Management**

```set x = 10```
*Creates a variable x and assigns it the value 10.*

```print x```
*Displays the current value of x.*

```del x```
*Deletes the variable x completely.*

```list```
*Shows all currently defined variables and their values.*

```clear```
*Clears all variables at once (like resetting memory).*



---

**➕ Arithmetic Operations**

You can perform basic math directly on variables:

```add x 5``` → *Adds 5 to x*

```sub x 2``` → *Subtracts 2 from x*

```mul x 3``` → *Multiplies x by 3*

```div x 2``` → *Divides x by 2 (uses integer division //)*


All operations happen in-place:

```
set a = 10  
add a 5  
print a   # Outputs: 15
```

---

**Utility Commands**

```rename old new```
*Renames a variable without changing its value.*

```help```
*Shows all available commands and their formats.*

```exit```
*Exits the Cygnus shell session.*



---

**Error Handling**

Cygnus handles most common errors gracefully and gives helpful messages:

• ``Assignment errors (like missing =)``

• ``Name errors (using undefined variables)``

• ``Math errors (like divide by 0)``

• ``Format errors (wrong syntax or typos)``



---

**Extra Touches**

• Color-coded outputs (using colorama) make it feel like a real terminal.

• Personalized prompt (username@cygnus:~$) adds to the shell experience.

• Clean, readable layout for every command and result.



---

> Cygnus is a shell that teaches you how a shell works. It gives the feeling of working in a coding environment while actually teaching you how environments like Bash or Python REPL are built from scratch.

---



