# Docker Learn

- ## [The Docker Handbook](https://www.freecodecamp.org/news/the-docker-handbook/)

### 1. Ubuntu Installation

- [https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)

### 2. Odoo Installation

- [https://registry.hub.docker.com/\_/odoo](https://registry.hub.docker.com/_/odoo)

### 3. Creating Docker Compose File

- Make folder on local system

  ```
  mkdir -p ~/ODOO_ERP/odoo-docker
  cd ~/ODOO_ERP/odoo-docker
  touch docker-compose.yaml
  mkdir ./config && touch config/odoo.conf
  mkdir ./addons
  ```

- Add the conf in the `config/odoo.conf` file

  Link: [odoo.conf](odoo.conf)

- Add the `./docker-compose.yaml` contents

  Link: [docker-compose.yaml](docker-compose.yaml)

### 4. Start the Docker daemon

```
sudo systemctl start docker
```

### 5. Add user to the docker group

```
sudo usermod -aG docker $USER
```

### 6. Test docker containers

```
docker run hello-world
```

### 7. Check the docker containers

```
docker ps -a
```

### 8. Check the running containers

```
docker ps
```

### 9. Start the docker containers

```
docker-compose up
```

### 10. Run the docker containers using yaml

```
docker-compose -f docker-compose.yaml up
```

### 11. Some other commands

```
# Start containers up in the background
docker-compose up -d

# Restart containers
docker-compose restart

# Stop containers
docker-compose stop

# Destroy containers (WARNING: This could mean data inside those containers as well)
docker-compose down

# Show container processes
docker ps
docker ps --filter name={container_name}

# Show container process stats
docker stats

# SSH into a container
docker exec -it {container_id} sh
docker exec -it $(docker ps -q --filter name={container_name}) sh
docker exec -u {user} -it {container_id} sh
docker exec -u root -it {container_id} bash

# Copy contents to container from host
docker cp ~/my/file {container_id}:~/myfile

# Copy contents from container to host
docker cp {container_id}:~/myfile ~/my/file

# Tail the process from a container
docker logs -f {container_id}
```

### 12. Rename docker image

```
docker image tag 3c2629942f0f kamrul/myodoo:latest
```

### 13. Stop all docker containers

```
docker stop $(docker ps -a -q)
```

### 14. Installed Docker info

```
docker system df --format 'table {{.Type}}\t{{.TotalCount}}\t{{.Size}}'
```

### 15. Save image as tar

```
docker save kamrul/myodoo:latest > odoo-image.tar
```

### 16. Load image from tar

```
docker load -i odoo-image.tar
```

### 17. Remove image

```
docker rmi kamrul/myodoo:latest
```

### 18. Inspect docker image

```
docker inspect kamrul/myodoo
```

### 19. Remove all images

```
docker rmi $(docker images -q)
```

### 20. Remove all containers

```
docker rm $(docker ps -a -q)
```

### 21. Remove all containers and images

```
docker-compose down
```

### 22. Remove all containers and images

```
docker-compose rm -f
```

### 23. Remove all containers and images

```
docker-compose down -v
```
