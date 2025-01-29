# Lluís Pellicer Juan
# 3CD2
# Sesión 1 Laboratorio LNR. Ejercicio 1

import re

def tokenize_text(input_text):
    expresiones_regulares = [
        r'\b(?:https?://\S+)|(?:www\.\S+)\b',  # URLs
        r'\b(?:\w[-\.\w]*\w)\@\w+\.\w+\b',  # Direcciones de correo
        r'\@\w+\b',  # Menciones a usuarios
        r'\#\w+\b',  # Hashtags
        r'\b\d+(?:\.\d+)?\b',  # Números
        r'\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{1,2} [A-Z][a-z]+ \d{4})\b',  # Fechas
        r'\b\d{1,2}:\d{2}\b',  # Horas
        r'\b(?:[A-Z]\.)+\b',  # Acronimos
        r'\b(?:[^\W\d_](?:[^\W\d_]|[-\'_])+)\b',  # Palabras sin caracteres especiales
        r'[^\w\s]',  # Caracteres especiales
        r'[^\s]'  # Otros
    ] 
    combined_pattern = '|'.join('(?:{})'.format(p) for p in expresiones_regulares)
    tokens = re.findall(combined_pattern, input_text, flags=re.IGNORECASE | re.UNICODE)
    return tokens

def tokenize_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in lines:
            line = line.strip()
            if line:
                f.write("##### " + line + " #####\n")
                tokens = tokenize_text(line)
                for token in tokens:
                    f.write(token + '\n')

if __name__ == "__main__":
    input_file = "input-tokenizer.txt"
    output_file = "output_tokeniser.txt"
    tokenize_file(input_file, output_file)
