##############
# Base build #
##############

FROM python:3.11-alpine AS base

LABEL maintainer="hernansaa88@gmail.com"

WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libpq-dev postgresql-dev

# Copy and install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . /usr/src/app/

# Run unit test
RUN python manage.py test


###############
# Final build #
###############

FROM python:3.11-alpine

# Install runtime dependencies
RUN apk add --no-cache libpq

# Copy app and dependencies from base build
COPY --from=base /usr/src/app /usr/src/app
COPY --from=base /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/

WORKDIR /usr/src/app

# Expose the Django web server port
EXPOSE 8000



