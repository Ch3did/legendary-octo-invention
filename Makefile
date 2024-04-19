.PHONY: install
# Automate first install
install:
	@echo ">>> Starting project"
	@pip3 install -r requirements.txt
	@echo ">>> Creating Database"
	@touch ./tmp/lambeijos.db
	@python3 ./srv/database.py 


.PHONY: restart_db
# run send database to windows operation system
restart_db:
	@rm -r ./tmp/lambeijos.db
	@touch ./tmp/lambeijos.db
	@python3 ./srv/database.py 


.PHONY: run
# run process
run:
	@python3 main.py
