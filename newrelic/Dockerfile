FROM python:3.9.14-alpine3.16

RUN pip install --no-cache-dir newrelic

COPY newrelic.ini newrelic.ini

ENTRYPOINT ["newrelic-admin", "run-program"]
