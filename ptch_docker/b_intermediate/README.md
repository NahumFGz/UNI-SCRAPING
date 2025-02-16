- Buscar xvfb .
  docker build -t selenium-xvfb .

- URL
  http://localhost:5555/ui/#

docker build -t selenium-chrome-volume .
docker run -d -p 5555:4444 --shm-size=2g -v /home/nahumfg/Projects/GithubProjects/UNI-SCRAPING/ptch_docker/b_intermediate/outputs:/home/seluser/Downloads --name selenium-container-volume selenium-chrome-volume

docker exec -it 6171e32e14d1 bash
