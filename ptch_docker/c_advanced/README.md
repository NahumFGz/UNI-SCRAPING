docker build -t selenium-demo .
docker run --rm \
 --shm-size=2g \
 -v /home/nahumfg/Projects/GithubProjects/UNI-SCRAPING/ptch_docker/c_advanced/outputs:/home/seluser/Downloads \
 selenium-demo

docker run --rm \
 --shm-size=2g \
 selenium-demo
