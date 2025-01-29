# Lluis Pellicer Juan
# 3CD2
# Sesión 3 Laboratorio LNR

import sys
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

def search_index(index_dir, query=None, extend=False):
    with open_dir(index_dir) as ix:
        with ix.searcher() as searcher:
            parser = QueryParser("content", ix.schema)
            if query:
                query = parser.parse(query)
            else:
                query = input("Enter your query: ")
                if not query.strip():
                    print("Empty query. Exiting.")
                    return
                query = parser.parse(query)
            results = searcher.search(query)
            total_results = len(results)
            if extend:
                if total_results > 0:
                    print("Total results:", total_results)
                    print(results[0])
                else:
                    print("No results found.")
            else:
                print("Total results:", total_results)
                for hit in results:
                    if extend:
                        print("Date:", hit['date'])
                        print("Title:", hit['title'])
                        print("Content:", hit['content'])
                    else:
                        print(hit['date'], "-", hit['title'])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python Searcher.py index_directory [-q=query] [--extend]")
        sys.exit(1)
    
    index_dir = sys.argv[1]
    query = None
    extend = False
    
    if "-q=" in sys.argv:
        query_index = sys.argv.index("-q=")
        query = sys.argv[query_index].split("=")[1]
    
    if "--extend" in sys.argv:
        extend = True
    
    search_index(index_dir, query, extend)

