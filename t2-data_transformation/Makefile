ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


d2r:
	echo $(current_dir)
	cd /media/sssw/external/software/d2rq-0.8.1/ && ./d2r-server $(ROOT_DIR)/d2rq.ttl

query:
	curl -i -H "Accept: text/turtle" --data-urlencode query@query.sparql http://localhost:2020/sparql
