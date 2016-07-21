mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

d2r:
	cd /media/sssw/external/software/d2rq-0.8.1/ && ./d2r-server $(current_dir)/d2rq.ttl
