# Docker Learn

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
