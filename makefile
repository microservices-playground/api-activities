run:
	python run.py

test:
	python activities_tests.py

db-data-copy:
	python db-data-copy.py

sv-stop:
	sudo supervisorctl stop api_activities

sv-start:
	sudo supervisorctl start api_activities

sv-restart:
	sudo supervisorctl start api_activities
