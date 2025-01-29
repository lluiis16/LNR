# LLuis Pellicer Juan
# 3CD2
# Sesión 3 Laboratorio LNR. Actividad 2

import argparse
import re
from whoosh.index import open_dir
from whoosh.qparser import QueryParser
from whoosh.query import Term, Or

def buscar_indice(index_dir, query_text, extend=False):
    ix = open_dir(index_dir)
    with ix.searcher() as searcher:
        parser = QueryParser("content", ix.schema)
        query = parser.parse(query_text)
        modified_query = modify_query_terms(query)
        res = searcher.search(modified_query)
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

def modify_query_terms(query):
    modified_terms = []
    for term in query:
        if isinstance(term, Term):
            term_text = term.text
            modified_term = Or([Term(term.fieldname, modify_term(term_text))])
            modified_terms.append(modified_term)
        else:
            modified_terms.append(term)
    return query.__class__(modified_terms)

def modify_term(term):
    return f"({term}|{term.lower()}|{term.upper()}|{term.capitalize()}|{term + 's'}|{re.sub(r's$', '', term)}|{term + 'es'}|{re.sub(r'es$', '', term)}|{term + 'ed'}|{re.sub(r'ed$', '', term)}|{term + 'ing'}|{re.sub(r'ing$', '', term)})"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search information using the indexes created.")
    parser.add_argument("index_directory", help="Directory where the index is located")
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

