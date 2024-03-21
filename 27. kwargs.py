# **kwargs =  parameter the will pack all arguments into a ditionary
#             useful so tha a function can accept a verying amount od keyword argument

def hello(**kwargs):
    #print("Hello "+ kwargs['first'] +" "+ kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items(): #key:first  value:"bro"
        print(value,end=" ")

hello(title="Mr.",first="Bro",middle="Dude",last="Code")