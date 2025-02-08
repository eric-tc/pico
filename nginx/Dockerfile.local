FROM nginx:stable-alpine3.20-otel
RUN rm /etc/nginx/conf.d/default.conf
ADD sites-enabled/default.conf /etc/nginx/conf.d/