.DEFAULT_GOAL := help

ansible-playbook = $(shell command -v ansible-playbook)

facts-profiling: export ANSIBLE_CONFIG = ansible_profiling.cfg
facts-profiling: ## example of profiling
	ansible-playbook facts_profiling.yml	

unixy-callback: export ANSIBLE_STDOUT_CALLBACK = unixy
unixy-callback: ## example of unix output
	ansible-playbook facts_from_api.yml

json-callback: export ANSIBLE_STDOUT_CALLBACK = json
json-callback: ## example of json output
	ansible-playbook facts_from_api.yml

selective-callback: export ANSIBLE_STDOUT_CALLBACK = selective
selective-callback: export ANSIBLE_SELECTIVE_DONT_COLORIZE = true
selective-callback: ## example of selective machine readable output 
	ansible-playbook selective.yml
	

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
