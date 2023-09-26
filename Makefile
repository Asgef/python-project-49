build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python -m pip install --user dist/*.whl --force-reinstall

package-uninstall:
	python3 -m pip uninstall hexlet-code

install:
	poetry install

start:
	brain-games

lint:
	poetry run flake8 brain_games
