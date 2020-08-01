build:
	docker build -t anthroponymie:latest .

run:
	docker build -t anthroponymie:latest . && docker run -it --rm -v ${CURDIR}:/usr/src/app anthroponymie:latest

test:
	pytest -vv tests/

plot:
	R < lib/plot.R  --vanilla
