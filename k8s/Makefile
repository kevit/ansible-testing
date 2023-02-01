.DEFAULT_GOAL := help
ansible-playbook = $(shell command -v ansible-playbook)



dependencies: ## install dependencies 
	ansible-galaxy collection install community.kubernetes

warmup: ## starting minikube
	minikube start

checkout: ## checkout last sources 
	git clone https://github.com/font/k8s-example-apps.git


build-image: ## build image and install in minikube
	$(shell cd k8s-example-apps/pacman-nodejs-app/docker; minikube image build . -t pacman-nodejs-app > /dev/null) 

.PHONY: deploy
deploy: ## deploy in kubernetes
	$(ansible-playbook) deploy.yml
	minikube tunnel

lab: dependencies warmup checkout build-image deploy ## run a lab

clean: ## clean all lab
#	minikube tunnel --cleanup
	$(ansible-playbook) cleaning.yml
	minikube image rm pacman-nodejs-app
	rm -rf k8s-example-apps 


get-info: ## get info about pacman
	kubectl -n pacman get all

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
