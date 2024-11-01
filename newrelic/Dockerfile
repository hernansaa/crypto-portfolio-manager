FROM python:3.9.14-alpine3.16

RUN pip install --no-cache-dir newrelic

WORKDIR /app

COPY newrelic.ini .

ENV NEW_RELIC_CONFIG_FILE=/app/newrelic.ini
ENV NEW_RELIC_APP_NAME=crypto-portfolio-manager
ENV NEW_RELIC_LICENSE_KEY=eu01xx331477306f612f5bdabacbd120FFFFNRAL

ENTRYPOINT ["newrelic-admin", "run-program"]
