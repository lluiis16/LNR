# Lluís Pellicer Juan
# 3CD2
# Sesión 1 Laboratorio LNR. Ejercicio 4

from random import shuffle
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

# Código ejercicio 4:
shuffle(corpus_simple)
partition_size = len(corpus_simple) // 10
accuracies = []
for i in range(10):
    test_set = corpus_simple[i * partition_size: (i + 1) * partition_size]
    train_set = corpus_simple[:i * partition_size] + corpus_simple[(i + 1) * partition_size:]
    tagger = hmm.HiddenMarkovModelTagger.train(train_set)
    total = 0
    correct = 0
    for tagged_sentence in test_set:
        for word, tag in tagged_sentence:
            predicted_tag = tagger.tag([word])[0][1]
            if tag == predicted_tag:
                correct += 1
            total += 1
    accuracy = correct / total
    accuracies.append(accuracy)

for i, accuracy in enumerate(accuracies):
    print(f"El accuracy el la partición {i+1} es: {accuracy}")

media = sum(accuracies) / len(accuracies)
print(f"\nLa media del accuracy es: {media}")

# Resultado por si tarda mucho: 
# El accuracy en la partición 1 es: 0.871869623803995
# El accuracy en la partición 2 es: 0.8729294090398291
# El accuracy en la partición 3 es: 0.8721337704233803
# El accuracy en la partición 4 es: 0.8739088014788949
# El accuracy en la partición 5 es: 0.8710292085454093
# El accuracy en la partición 6 es: 0.872001812857342
# El accuracy en la partición 7 es: 0.8711309061404872
# El accuracy en la partición 8 es: 0.8681984959275547
# El accuracy en la partición 9 es: 0.8731814701378254
# El accuracy en la partición 10 es: 0.8711168623311171

# La media del accuracy es: 0.8717500360685835