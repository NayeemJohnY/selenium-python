ARG TESTNAME

FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt --upgrade

COPY . .

CMD ["python", "tests/${TESTNAME}.py""]