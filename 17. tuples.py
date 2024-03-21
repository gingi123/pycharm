# tuples = collection which is ordered and unchangeable
#          used to group together related data

student = ("bro",21,"male")

#print(student.count("bro"))  # ez megszámolja
#print(student.index("male")) #ez megnezi hanyas helyen helyezkedik

for x in student:
    print(x)

if "bro" in student:      #"if its tru" akkor mit csináljon
    print("bro is here")