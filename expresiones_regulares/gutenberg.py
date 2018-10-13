import re

content = open('2638-0.txt').read()


inicio = re.search('I\.', content).end()
final = re.search('II\.', content).start()

content = content[inicio:final]

the_apariciones = re.findall(r'[tT]he', content)
comillas_apariciones = re.findall(r'“', content)
conects_apariciones = re.findall(r'\w+--\w+', content)

print("'the' apareció {}".format(len(the_apariciones),))

print("'\"' apareció {}".format(len(comillas_apariciones),))
print("Lista de palabras con -- :\n\t{}".format(
    '\n\t'.join(conects_apariciones)
))

print(re.sub(r' I ', ' IPhone ',content))
print(re.sub(r' I ', ' IPhone ',content))

# print(conects_apariciones)