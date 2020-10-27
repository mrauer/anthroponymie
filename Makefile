build:
	docker build -t anthroponymie:latest .

run:
	docker build -t anthroponymie:latest . && docker run -it --rm -v ${CURDIR}:/usr/src/app anthroponymie:latest

test:
	pytest -vv tests/

chart:
	docker build -t anthroponymie_r:latest -f Dockerfile_R . && docker run -it --rm -v ${CURDIR}:/usr/src/app anthroponymie_r:latest

cut:
	python3 main.py cut $(cutoff)

urls:
	python3 main.py urls $(cutoff)

countries:
	python3 main.py countries

show:
	python3 main.py show

stats:
	python3 main.py stats

agg:
	python3 main.py agg
