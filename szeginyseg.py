





def printoutbabe(statistic):
    sorted_statistic = sorted(statistic, key=lambda x: x['CSOROSAG'],reverse=True)
    print(f'A Föld 100 legszegényebb országa:')
    for item in sorted_statistic:
        name = item['ORSZAGNEV']
        precent = item['CSOROSAG']
        print(name,precent)







statistic = []
#sorted_statistic = sorted(statistic, key=lambda x: x['CSOROSAG'])
#statisticprecent = []

with open('szegenyseg.txt','r',encoding='utf=8') as file:
    fileintoproject = file.read()
    formatfile = fileintoproject[:-1].split('\n')
    formatfile1 = formatfile[4:]
for lines in formatfile1:
    splitted_lines = lines.split('\t')
    statistic.append({
        "ORSZAGNEV" : splitted_lines[0],
        "CSOROSAG": splitted_lines[1],
        "EVJARAT": splitted_lines[2],
    })


#sorted_statistic = sorted(statistic, key=lambda x: x['CSOROSAG'],reverse=True)
#for item in sorted_statistic:
#    print(item)


#print(statistic)
#print(sorted_statistic)
printoutbabe(statistic)
#print(formatfile)
#print(formatfile1)
print(statistic)












