FROM alpine:3.4

RUN apk --update add nginx && \
    mkdir -p /var/log/nginx && \
    mkdir -p /run/nginx&& \
    ln -sf /dev/stdout /var/log/nginx/access.log&& \
	ln -sf /dev/stderr /var/log/nginx/error.log


EXPOSE 80
CMD  ln -sf /etc/hosts /var/lib/nginx/html/index.html;nginx -g "daemon off;"
