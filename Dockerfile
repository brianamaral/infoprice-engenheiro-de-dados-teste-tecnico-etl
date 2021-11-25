FROM python:3.9

WORKDIR /code

COPY . .

RUN make build

CMD ["python","pipeline/main.py"]