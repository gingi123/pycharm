

def ohnegol(results):
    x = 0
    for gols in results:
        golhazai = int(gols['HAZAIGOL'])
        golvendeg = int(gols['VENDEGGOL'])
        if golhazai == 0 and golvendeg == 0:
            x = x + 1
    print(f"Gól nélküli mérkőzések száma: {x}")

def avggol(item):
        avgp = sum(item)/len(item)
        return avgp


def mappahazai(results,resultgolhazai):
    for item1 in results:
        golok = int(item1['HAZAIGOL'])
        resultgolhazai.append(golok)
#    return resultgolhazai

def mappavendeg(results,resultgolvendeg):
    for item2 in results:
        golok = int(item2['VENDEGGOL'])
        resultgolvendeg.append(golok)
#    return resultgolvendeg





results = []
resultgolhazai = []
resultgolvendeg = []

with open('foci.txt','r',encoding='utf=8') as file:
    fileinread = file.read()
    formatlines = fileinread[:-1].split('\n')
    formatlines1 = formatlines[1:]
for lines in formatlines1:
    splitted_lines = lines.split('\t')
    results.append({

        'FORDULO':splitted_lines[0],
        'HAZAICSAPAT':splitted_lines[1],
        'VENDEGCSAPAT':splitted_lines[2],
        'HAZAIGOL':splitted_lines[3],
        'VENDEGGOL':splitted_lines[4]
    })


ohnegol(results)
mappahazai(results,resultgolhazai)
mappavendeg(results,resultgolvendeg)
avggol(resultgolhazai)
avggol(resultgolvendeg)
print(f"Hazai Gólátlag: {avggol(resultgolhazai)}")
print(f"Vedég Gólátlag: {avggol(resultgolvendeg)}")

#print(resultgolhazai)
#print(resultgolvendeg)
#    print(splitted_lines[4])
#    print(formatlines)
#    print(formatlines1)















