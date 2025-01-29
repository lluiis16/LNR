# Lluís Pellicer Juan
# 3CD2
# Sesión 1 Laboratorio LNR. Ejercicio 3

from sklearn.model_selection import train_test_split
from nltk.tag import hmm
from nltk.corpus import brown

# Crear la variable corpus_simple
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

# Código ejercicio 3:
train, test = train_test_split(corpus_simple, test_size=0.1, random_state=42)
mytagger = hmm.HiddenMarkovModelTagger.train(train)
test_etiquetados = [mytagger.tag(oracion) for oracion in test]
accuracy = mytagger.accuracy(test)
print("Accuracy:", accuracy)

# Resultado por si tarda mucho: 
# Accuracy: 0.9451768755624285