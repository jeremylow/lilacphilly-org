info:
	@python --version
	@pyenv --version
	@pip --version

clean:
	rm -fr build
	rm -fr dist
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '*.pyo' -exec rm -f {} \;
	find . -name '*~' ! -name '*.un~' -exec rm -f {} \;

lint:
	pre-commit run -a

test:
	coverage run --source='.' manage.py test
	coverage report
	coverage html

env:
	pyenv install -s 3.6.0
	pyenv local 3.6.0

install:
	pip install -Ur requirements/dev.txt

server:
	python manage.py runserver 0.0.0.0:8000

gulp:
	gulp

ci: clean env info test
	codecov

dump:
	python manage.py dumpdata --natural-foreign --natural-primary > data-`date +'%Y-%m-%d-%H-%M-%S'`.json

uncss:
	node uncss.js

black:
	black .

deploy:
	git pull;
	chown -R www-data .;
	chgrp -R www-data .;
