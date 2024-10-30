##############
# Base build #
##############

FROM python:3.11 AS base

LABEL maintainer="hernansaa88@gmail.com"

WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# # Install build dependencies
# RUN apt-get install gcc musl-dev libpq-dev postgresql-dev

# Copy and install development dependencies
COPY requirements.txt ./
COPY requirements-dev.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements-dev.txt

# Copy the application code
COPY . /usr/src/app/

# Run unit test
# RUN python manage.py test


###############
# Final build #
###############

FROM python:3.11-alpine

# Install runtime dependencies
RUN apk add --no-cache libpq

# Copy app files from base build
COPY --from=base /usr/src/app /usr/src/app

# Copy and install production dependencies
COPY requirements.txt ./
COPY requirements-prod.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements-prod.txt

COPY newrelic.ini /usr/src/app/newrelic.ini

WORKDIR /usr/src/app

# Expose the Django web server port
EXPOSE 8000