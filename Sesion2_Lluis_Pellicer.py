# Lluis Pellicer Juan
# 3CD2
# Sesión 2 Laboratorio LNR

import sys
import pandas as pd
from datetime import datetime
from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT, DATETIME, KEYWORD
from whoosh.analysis import RegexTokenizer, LowercaseFilter, StopFilter

def crear_indice(schema, index_dir):
    ix = create_in(index_dir, schema)
    return ix.writer()

def indexar_docs(dataset_path, index_dir):
    df = pd.read_csv(dataset_path)
    my_analyzer = RegexTokenizer() | LowercaseFilter() | StopFilter()
    schema = Schema(
        id=ID(unique=True),
        title=TEXT(stored=True),
        content=TEXT(analyzer=my_analyzer),
        category_level_1=KEYWORD,
        source=TEXT(stored=True),
        date=DATETIME,
        published_utc=DATETIME)
    writer = crear_indice(schema, index_dir)
    for _, row in df.iterrows():
        try:
            published_utc = datetime.fromisoformat(str(row['published_utc']))
        except ValueError:
            published_utc = None
        writer.add_document(
            id=str(row['id']),
            title=row['title'],
            content=row['content'],
            category_level_1=row['category_level_1'],
            source=row['source'],
            date=datetime.fromisoformat(row['date']),
            published_utc=published_utc)
    writer.commit()

if __name__ == "__main__":
    if 'ipykernel' in sys.modules:
        dataset_path = "MN-DS-news-classification.csv"
        index_dir = "prueba"
    else:
        if len(sys.argv) != 3:
            print("Usage: python Indexer.py path_dataset index_directory")
            sys.exit(1)
        dataset_path = sys.argv[1]
        index_dir = sys.argv[2]
    indexar_docs(dataset_path, index_dir)

