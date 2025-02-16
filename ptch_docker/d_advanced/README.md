docker-compose up

- Inicia los contenedores usando imágenes existentes
- Ejecución más rápida
- Mejor cuando no se han realizado cambios en el código

docker-compose up --build

- Fuerza la reconstrucción de todas las imágenes antes de iniciar los contenedores
- Asegura que se incluyan los últimos cambios del código
- Usar cuando se han modificado el Dockerfile o el código fuente

docker compose up --abort-on-container-exit && docker compose down --volumes --remove-orphans

- Inicia los contenedores y se detiene cuando cualquier contenedor termine
- Después elimina:
  - Contenedores
  - Volúmenes
  - Redes
  - Contenedores huérfanos

# Alternativa usando modo detached

docker compose up -d && docker compose down --volumes --remove-orphans

- Inicia los contenedores en segundo plano
- Después elimina todos los recursos
