mkfile_path := $(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
mkfile_dir:=$(shell cd $(shell dirname $(mkfile_path)); pwd)
current_dir:=$(notdir $(mkfile_dir))

d2r:
	echo $(current_dir)
	cd /media/sssw/external/software/d2rq-0.8.1/ && ./d2r-server $(current_dir)/d2rq.ttl
