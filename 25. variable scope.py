
name = "Bro"   # global scope (available inside & outside funcions)
def display_name():
    name = "Code"   #local scope (available only inside this function)
    print(name)

display_name()
print(name)
                         #python rules
                         #L = Local
                         #E = Enclosing
                         #G = Global
                         #B = Built-in

