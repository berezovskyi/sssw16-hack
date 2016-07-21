import urllib.request
import urllib
import json

# Returns an object that contains reviews
# Takes a parameter to define the endpoint, like for example localhost:8890
def getreviewsjson(endpoint):
    queryfile = open('fetchreviews.sparql', 'r')
    query = urllib.parse.quote_plus(queryfile.read())
    uri = "http://" + endpoint + "/sparql?default-graph-uri=&query=" + query + "&format=application%2Fsparql-results%2Bjson&timeout=0&debug=on"

    data = urllib.request.urlopen(uri)
    str_response = data.read().decode('utf-8')
    obj = json.loads(str_response)
    return obj

