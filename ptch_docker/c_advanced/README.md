- Buscar xvfb .
  docker build -t selenium-xvfb .

- URL
  http://localhost:4444/ui/#

docker build -t selenium-runner .

docker build -t selenium-chrome-volume .
docker run -d -p 4444:4444 --shm-size=2g -v /home/nahumfg/Projects/GithubProjects/UNI-SCRAPING/ptch_docker/c_intermediate/outputs:/home/seluser/Downloads --name selenium-container-volume selenium-chrome-volume

docker exec -it 6171e32e14d1 bash
