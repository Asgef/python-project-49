build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

install:
	poetry install

start:
	brain-games

lint:
	poetry run flake8 brain_games
