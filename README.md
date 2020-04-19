# Spinning out of a basic ELK on a server
> `htpasswd` has the login details that can be generated with [htpasswd generator](https://hostingcanada.org/htpasswd-generator/)
### Elasticsearch: Port 9200
The database itself. Setup with Vanilla config. Port 9200

### Kibana: Port 5610
Turning the data into graphical format. Port 5610

### NGINX: Port 443
Managing requests and connections to Kibana and Elasticsearch

### SSL Connection to upgrade to https
1. Generate an private key with openssl
``` shell
openssl genrsa -des3 --passout "pass:password" -out /etc/private.key 4096
```
- `-des3 --passout "pass:password"` Ecnrypts the private key with a password "password" (output is not protected)
- `-out /etc/private.key` output location for private key
- `4096` no bits used

2. Create and process certificate
``` shell
openssl req -nodes -new -subj '/CN=*/O=DreamsHub./C=HK' --passin "pass:hello" -x509 -keyout /etc/private.key -out /etc/key.crt
```
- `-nodes -new` Generate an ssl certificate and do not encrypt private keys that are generated
- `=subj /CN=*/O=DreamsHub./C=HK`: sets subject name for new request or supersedes the subject name when processing a request


# Building

`docker-compose up --build -d`
