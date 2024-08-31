distclean:
	#git clean -xdf
	rm -rf dist/
	rm -rf .venv
	hatch env remove dev

setup:
	env

.venv:
	hatch env create dev
	ln -f -s $(shell hatch env find dev) .venv

dev:
	python3 -m pip install -e .

lint:
	hatch run dev:lint

format:
	hatch run dev:format

runapp:
	python3 src/infected/main.py
