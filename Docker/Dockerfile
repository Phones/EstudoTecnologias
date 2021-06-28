FROM ubuntu

WORKDIR /usr/src/teste/

RUN apt-get update -y
RUN apt-get install python3 -y

COPY . .

CMD ["python3", "teste.py"]