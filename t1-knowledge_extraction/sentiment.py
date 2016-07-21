import requests

def get_score(word):
    query_params = {
        "query" : make_query(word)
        "Accept": "application/sparql-results+json"
    }
    print(query_params)
    r = requests.get('http://localhost:2020/sparql', params=query_params)
    resp = r.json()
    print(resp)

def make_query(word):
    return """SELECT ?negativeScore, ?positiveScore WHERE {
        ?s <http://www.semanticweb.org/sssw/ontologies/2016/6/synset#terms> ?terms
        ?s <http://www.semanticweb.org/sssw/ontologies/2016/6/synset#negativeScore> ?negativeScore
        ?s <http://www.semanticweb.org/sssw/ontologies/2016/6/synset#positiveScore> ?positiveScore
        filter( regex(?terms, "$s#" ))
    }
    """ % (word)
    # return """
    #     SELECT DISTINCT ?review
    #     WHERE {?s <http://sematic-web-journal..com/ontology#reviewComment> ?review}
    #     LIMIT 10
    # """


if __name__ == '__main__':
    score = get_score("disgusting")
    print(score)
