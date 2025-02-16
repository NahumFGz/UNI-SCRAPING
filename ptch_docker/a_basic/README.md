- Buscar xvfb .
  docker build -t selenium-xvfb .

- URL
  http://localhost:4444/ui/#

docker build -t selenium-chrome .
docker run -d -p 4444:4444 --shm-size=2g --name selenium-container selenium-chrome
