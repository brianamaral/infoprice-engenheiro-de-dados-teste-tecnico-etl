
build:
	python3 -m venv --without-pip .venv

	. .venv/bin/activate

	pip install -r requirements.txt

run:
	python3 pipeline/main.py

run-docker:
	sudo docker-compose up