# args = parameters that will pack all arguments iinto tuple
#        useful so that a funcion can accept a varyin amount of arguments

def add(*args):
   sum = 0
   #args = list(args)
   #args[5] = 0        #indexel 5. elemet lecseréli 0 ra
   for i in args:
       sum += i
   return sum

print(add(1,2,3,4,5,6))
#print(type(sum))