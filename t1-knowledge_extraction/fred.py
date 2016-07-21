import json

import urllib.request

rev_json = json.load(open('reviews.json'))

for binding in rev_json.get('results')['bindings'][:2]:
    review = binding['review']['value']

    params = urllib.parse.urlencode({'text': review[:100]})
    f = urllib.request.urlopen("http://wit.istc.cnr.it/stlab-tools/fred?%s" % params)
    print(f.read)


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
