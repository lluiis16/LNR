# Lluís Pellicer Juan
# 3CD2
# Sesión 1 Laboratorio LNR. Ejercicio 2

from nltk.corpus import brown

def simplificador(etiqueta):
    if '-' in etiqueta:
        etiqueta = etiqueta.split('-')[0]
    if etiqueta.startswith('FW'):
        etiqueta = 'FW'
    return etiqueta

corpus_simple = []
for oracion in brown.tagged_sents():
    oracion_reducida = [(palabra, simplificador(etiqueta)) for palabra, etiqueta in oracion]
    corpus_simple.append(oracion_reducida)
print(corpus_simple)

# Resultado por si tarda mucho: 
# [[('The', 'AT'), ('Fulton', 'NP'), ('County', 'NN'), ('Grand', 'JJ'), 
#   ('Jury', 'NN'), ('said', 'VBD'), ('Friday', 'NR'), ('an', 'AT'),
#   ('investigation', 'NN'), ('of', 'IN'), ("Atlanta's", 'NP$'), 
#   ('recent', 'JJ'), ('primary', 'NN'), ('election', 'NN'), ('produced', 'VBD'),
#   ('``', '``'), ('no', 'AT'), ('evidence', 'NN'), ("''", "''"), ('that', 'CS'), 
#   ('any', 'DTI'), ('irregularities', 'NNS'), ('took', 'VBD'), ('place', 'NN'), 
#   ('.', '.')], [('The', 'AT'), ('jury', 'NN'), ('further', 'RBR'), ('said', 'VBD'),
#                 ('in', 'IN'), ('term-end', 'NN'), ('presentments', 'NNS'),...]] 