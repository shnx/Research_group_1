for i in range(7):
    file = open(f'{i}.txt', 'r')
    x = file.readline()
    x = x.replace(' ', '')
    x = x.replace('(', '')
    x = x.replace('\t', '')
    x = x.replace(')', '\n')
    file2 = open(f'{i}.csv', 'w')
    file2.write('strength,angle,distance\n')
    file2.write(x)
    file.close()
    file2.close()