# Lluis Pellicer Juan
# 3CD2
# Sesión 3 Laboratorio LNR. Actividad 1


import argparse
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def buscar_indice(index_dir, query_text, extend=False):
    ix = open_dir(index_dir)
    with ix.searcher() as searcher:
        parser = QueryParser("content", ix.schema)
        query = parser.parse(query_text)
        res = searcher.search(query)
        print(f"Total results: {len(res)}")
        if extend:
            for hit in res:
                print(f"Date: {hit['date']}")
                print(f"Title: {hit['title']}")
                print(f"Content: {hit['content']}")
                print("=" * 20)
        else:
            for hit in res:
                print(f"{hit['date']} {hit['title']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search information using the indexes created.")
    parser.add_argument("C:/Users/lluis/Desktop/lluis/Onedrive/Escritorio/3r Curso/2ndo cuatri/LNR/prueba", help="Directory where the index is located")
    parser.add_argument("-q", "--query", help="Query text")
    parser.add_argument("--extend", action="store_true", help="Show extended information for the first result")
    args = parser.parse_args()
    if args.query:
        buscar_indice(args.index_directory, args.query, args.extend)
    else:
        while True:
            query = input("Enter a query>>: ")
            if not query:
                break
            buscar_indice(args.index_directory, query, args.extend)


