FROM nginx
RUN apt-get update; apt-get install openssl

# Gen fresh SSL key
RUN openssl genrsa -des3 --passout "pass:hello" -out /etc/private.key 4096
RUN openssl req -nodes -new -subj '/CN=elk.dreamsai/O=DreamsAI/C=HK' --passin "pass:hello" -x509 -keyout /etc/private.key -out /etc/key.crt

COPY nginx.conf /etc/nginx/nginx.conf
COPY htpasswd /etc/htpasswd
