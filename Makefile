validate:
	python3 scripts/validate.py
	python3 scripts/render.py --check

test:
	python3 -m unittest discover -s tests -v

assess:
	python3 scripts/assess.py examples/answers.example.json

links:
	python3 scripts/check_links.py

render:
	python3 scripts/render.py
