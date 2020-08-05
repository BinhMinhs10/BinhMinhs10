# Tutorial Docker
# Author
   **Binh Minh**
## 1. Docker containers là gì?
* seperate the file system and networks between container, unless you explicitly allow it 
* Does not have it own OS like Virtual Machine
### 1.1 Dockerfile
* a set of instructions which are executed by docker command line tool
### 1.2 Docker image
* executes Dockerfile produces a Docker image, all needed files and instructions
* Possible start multiple Docker containers from same Docker image
### 1.3 Docker Compose
* link multiple docker containers into a single composition, which can be installed and start up all at once

## 2. Dockerfile
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
```base
CMD base_image:latest
```
```base
FROM base_image:latest
```
## 3. Docker Commands
* build Dockerfile found in directory
```bash
sudo docker build .
```
* list all docker image
```bash
sudo docker images
```
* docker run container
```bash
sudo docker run hello-world
```
* show docker container
```bash
sudo docker ps
```
