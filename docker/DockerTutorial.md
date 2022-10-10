# Tutorial Docker
# Author
   **Binh Minh**


# 1. Docker containers là gì?

<details>
    <summary> <b> Docker containers </b> </summary>

* seperate the file system and networks between container, unless you explicitly allow it 
* Does not have it own OS like Virtual Machine

</details>

<details>
    <summary><b>Dockerfile</b></summary>

* a set of instructions which are executed by docker command line tool
</details>

<details>
    <summary><b>Docker image</b></summary>

* executes Dockerfile produces a Docker image, all needed files and instructions
* Possible start multiple Docker containers from same Docker image
</details>

<details>
    <summary><b>Docker Compose</b></summary>

* link multiple docker containers into a single composition, which can be installed and start up all at once
</details>


# 2. Dockerfile
* can use base Docker image on top to own Docker image
* a set of file copied into Docker image
* possible a network (TCP/UDP) port 
```base
FROM base_image:latest
CMD echo print result
CMD java -cp /myapp/myapp.jar arg1 arg2
COPY /MyHost/myapp.jar /DockerImage/myapp.jar
COPY /MyHost/conf/conf1.cfg /MyHost/conf/conf2.cfg /DockerImage/conf/
ADD file.tar /DockerImage/extracted/
ADD http://download.com/myfile.jar /DockerImage/myapp/
ENV MY_VAR 13
RUN apt-get install some-needed-app
ARG tcpPort

```
# 3. Docker Commands

* restart docker service
```bash
systemctl start docker
sudo service docker restart
```

* list all docker image
```bash
sudo docker images
sudo docker image ls
```
* remove docker image
```bash
sudo docker rmi <image id>
```
* show docker container
```bash
sudo docker ps -a
```
* build Dockerfile found in directory
```bash
# use first time build
sudo docker build -t electra:lastes .
sudo docker-compose -f <compose file> build
```
* docker run in container
```bash
sudo docker run hello-world
sudo docker-compose -f <compose file> up
```
* shutdown container
```bash
sudo docker-compose -f <compose file> down
```
* Remove docker container
```bash
docker container rm -f <container id>
```
# 4. Run commands in Stopped Docker Containers
```bash
docker commit <container id> debug/ubuntu
docker run -v /home/hact/mrc:/data -it --rm --entrypoint /bin/bash debug/ubuntu
```
```bash
docker exec -it <container-id> bash
```
# 5. Retrieve logs until a specific point in time
```bash
docker logs -f --until=2s <name container>
```
# 6. Remove < none > image
```bash
docker images | grep none | awk '{ print $3; }' | xargs docker rmi --force
```
# 7. Access an NVIDIA GPU
* prerequisites download and install the proper drivers
* Install nvidia-container-runtime
```bash
apt-get install nvidia-container-runtime
```
* Flush changes and restart Docker 
```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```
* Ensure the `nvidia-container-runtime-hook` is accessible from `$PAHT`
```bash
which nvidia-container-runtime-hook
``` 
* Expose GPUs for use
```bash
docker run -it --rm --gpu all ubuntu:18.04 nvidia-smi
```

# 8. Debug docker
add row at the end of Dockerfile 
```docker
CMD tail -f /dev/null
```