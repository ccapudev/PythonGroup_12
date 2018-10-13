import re

def matcher(*args, **kwargs):
    matched = re.match(*args, **kwargs)
    if matched:
        print(matched.group(), matched.start(), matched.end())

pattern = r'Cookie'
sequence = 'Cookies ar genial'
matcher(pattern, sequence)


pattern = r'cookie'
sequence = 'Cookies ar genial'
matcher(pattern, sequence)

pattern = r'Cookie'
sequence = 'The cookies ar genial'
matcher(pattern, sequence)


'''
el punto reemplaza un caracter en el patron 
'''
pattern = r'c.ok.e'  # cookie ciokae caokae
sequence = 'Cookies ar genial'
matcher(pattern, sequence, flags=re.IGNORECASE)


'''
\w representa una letra digito o guion bajo
\s sppce tab o new line
\d solo digitos
'''
pattern = r'c\we'  # cookie ciokae caokae
sequence = 'C_s ar genial'
matcher(pattern, sequence, flags=re.IGNORECASE)
