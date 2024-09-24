# Development

Questo comando crea l'image per la parte web senza nginx. Una volta create e lanciato il container 
posso sviluppare con VsCode e estensione dei container.

docker-compose -f docker-compose-dev.yaml build
docker-compose -f docker-compose-dev.yaml up

## Rimuovere i container
docker-compose -f docker-compose-dev.yaml down


# Production
docker-compose build
docker-compose up

Questi comandi creano immagine di produzione collegata con nginx e docker. Flask parte con gunicorn
collegandosi ad nginx

In entrambi gli ambienti il database è gestito tramite il container di postgres.

# Development

docker-compose -f docker-compose-dev.yaml build
docker-compose -f docker-compose-dev.yaml up

docker-compose -f docker-compose-dev.yaml down

# Connettersi a Postgres con DBEaver

1) Installare DBEaver
2) Lanciare il container
3) Trovare Ip Container docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' my-postgres-container
4) Configurare DBEaver scegliendo come database Postgres usando indirizzo Ip username e password
5) Configurare la connessione con nome database:db user:postgres psw:postgres usare come porta di connessione 6543 e come host 0.0.0.0