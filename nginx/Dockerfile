# Second stage: build the Nginx server
FROM nginx:1.27-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY default.conf /etc/nginx/conf.d