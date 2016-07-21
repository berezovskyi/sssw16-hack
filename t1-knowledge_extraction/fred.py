import json

import urllib.request
import sys
import fetchreviews

import rdflib

#rev_json = json.load(open('reviews.json'))
endpoint = "localhost:8890"
if len(sys.argv) > 1:
    endpoint = sys.argv[1]
rev_json = fetchreviews.getreviewsjson(endpoint)

g = rdflib.Graph()

for binding in rev_json.get('results')['bindings']:
    review = binding['review']['value']

    params = urllib.parse.urlencode({
        'text': review[:150],
        'prefix': 'fred',
        'namespace': 'http://www.ontologydesignpatterns.org/ont/fred/domain.owl#',
        'textannotation': 'earmark',
        'format': 'text/turtle',
    })
    req = urllib.request.Request('http://wit.istc.cnr.it/stlab-tools/fred?%s' % params)
    req.add_header('Accept', 'text/turtle')
    f = urllib.request.urlopen(req)

    g.parse(f, format='turtle')
    labels = [str(lbl) for lbl in g.objects(None, rdflib.RDFS.label)]
    # print(labels)



# // Create connection
# URLConnection conn = new URL(fredEndpoint + request).openConnection();
#
# // Set the output format in the Accept header
# conn.setRequestProperty("Accept", "text/turtle");
#
# // Get the RDF output as an InputStream
# InputStream is = conn.getInputStream();
#
# // Load the RDF output into an Apache Jena in-memory model
# Model model = ModelFactory.createDefaultModel();
# model.read(is, null, "TURTLE");
#
