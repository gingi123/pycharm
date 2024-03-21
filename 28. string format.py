# str.format() = optional metod that given users
#                more control when displaying output

#animal = "cow"
#item = "moon"

#print("The "+animal+ " Jumper over the "+item)
#print("The {1} jumped over the {1}".format(animal,item)) #position arguments
#print("The {animal} jumped over the {animal}".format(animal="cow",item="moon")) # keyword arguement

#text = "The {} Jumped over the {}"
#print((text.format(animal,item)))

#name = "Bro"

#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. nice to meet you".format(name))
#print("Hello, my name is {:<10}. nice to meet you".format(name))
#print("Hello, my name is {:>10}. nice to meet you".format(name))
#print("Hello, my name is {:^10}. nice to meet you".format(name))

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:x}".format(number))
print("The number pi is {:e}".format(number))
print("The number pi is {:E}".format(number))