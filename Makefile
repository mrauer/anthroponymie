build:
	docker build -t anthroponymie:latest .

run:
	docker build -t anthroponymie:latest . && docker run -it --rm -v ${CURDIR}:/usr/src/app anthroponymie:latest

test:
	pytest -vv tests/

chart:
	R --vanilla < lib/visu.r
