# Docker and Kubernetes
### Docker

- containers bundle application, dependencies together .
- containers share the same low lever OS (kernel) so they are lightweight (fast startup).
- They solve the "it works on my machine" problem.
- Machine resources are partitioned and shared.
VMs are more heavy cause they include OS. So you can run VMs with different OS in the same machine.
Containers are managed by a container manager (hypervisor).

Docker daemon : manages images and container, resources,...  
Docker image : set of instruction to create a container.  
Docker Registry : where we store images.  
DockerHub : registry of pre-existing docker images.  

```
docker ps
docker pull postgres:latest
docker run --name psql -e POSTGRES_PASSWORD=password! -p 5432:5432 -d postgres:latest
psql -h 0.0.0.0 -p 5432 -U postgres
docker stop <container_id>
```

docker file.  
-> define docker images.  
starts with basic image on top of which you can add layers.  

```python 
FROM python:3.7.2-slim
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install flask
ENTRYPOINT [“python”, “app.py”] 
```

running container from docker file.  
DockerFile -> DockerImage -> Docker container

Some commands:   
FROM, RUN, COPY, ENTRYPOINT, ENV, WORKDIR, CMD

```
# build a docker image
docker build --tag testimage .
docker build -t testimage .
docker run testimage
docker run testimage -rm
docker run -p 80:8080 testimage
```

### Kubernetes

Containers orchestration tools.  
- Horizontal Scaling: deploy more or less container following the demand

Components of kubernetes: 
- cluster: group of machine or VMs on which containers will be ran
- node: a single machine or VM part of the cluster 
- pods: a single deployment of a container. pods are not persistent. Volumes can be attached to pods for the persistent part.
- master system: managing the cluster
- kubernetes service provide persistent way of communication between pods

Amazon elastic kubernetes: you just deploy your nodes and services on it and they do the rest.  








