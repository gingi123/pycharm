#dictionaries = a changeable, unordered collection of unique key:value pairs
#               fast because they use hashing, allow us to access a value quickly


#itt az első pl:USA az value és ami utána jön Washington az key

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':"Las Vegas"})
capitals.pop("China")
#capitals.clear()

print(capitals['Germany'])
#print((capitals.get)('Germany'))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())
#for key,value in capitals.items():
    #print(key,value)