## Gestione migrazioni

1) Aggiornare il codice in produzione con ultima versione migrazioni
2) Eseguire il comando flask db upgrade dentro al container dove è presente gunicorn

### SOLO se prima volta

Dopo aver eseguito **flask db upgrade** eseguire **flask insert-db** per inserire le patologie di default a database.


**N.B** di base le migrazioni le gestisco manualmente per evitare casini con gli entrypoint

## Come installare https

Questi comandi vanno eseguiti dalla root. Perchè i volumi presenti in docker hanno le path in base alla root del progetto

1) Fai partire nginx con configurazione senza https


    upstream app {
        server web:4050;
    }

    server {
        listen 80;
        server_name www.picomir.it picomir.it;

        location /.well-known/acme-challenge/ {
            root /var/www/html;
            allow all;
        }

        location / {
        return 301 https://$host$request_uri;
        }
        }

2) Usa il comando di Certbot per creare i certificati

```
docker compose run --rm certbot certonly --webroot -w /var/www/html --email eric.tondelli@gmail.com -d picomir.it -d www.picomir.it --agree-tos --no-eff-email
```
nella cartella nginx ssl/live/picomir.it sono creati i certificati

3) Crea la configurazione di Nginx per gestire il comande


4) Rinnovare il certificato di certbot nel futuro


Rinnovare il certbot automaticamente con uno script e cron job

services:
  certbot:
    image: certbot/certbot
    volumes:
      - ./nginx/ssl:/etc/letsencrypt
      - ./nginx/www:/var/www/html
    entrypoint: "/bin/sh -c 'while true; do certbot renew; sleep 12h; done'"


## Connessione in Remoto

ssh 46.101.189.188
La chiave si trova in C:\Users\Vision-e\digital_ocean.pub


### Caricare una nuova release

scp 0.0.3.zip 46.101.189.188:/home/release/{versione}

unzip {versione}


# Debug

Per vedere i log del docker container 

docker logs -f <container_name_or_id>
