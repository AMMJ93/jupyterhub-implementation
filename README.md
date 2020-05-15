# Documentation

## Instructions

Change .env.example to .env and insert values. Also insert values for traefik.toml. 

## Compose file

```
version: '3'

services:
  jupyhub: #service name
    build: jupyterhub #specifies what folder to look for Dockerfile 
    container_name: hub #container name
    environment: #environment values (${value} are retrieved from .env file)
      DOCKER_JUPYTER_IMAGE: jupyterlab_img
      DOCKER_NETWORK_NAME: ${COMPOSE_PROJECT_NAME}_default
      OAUTH_CLIENT_ID: ${OAUTH_CLIENT_ID} #google oauth
      OAUTH_CLIENT_SECRET: ${OAUTH_CLIENT_SECRET} #google oauth
      OAUTH_CALLBACK_URL: ${OAUTH_CALLBACK_URL} #google oauth
      HUB_IP: hub
    labels:
      - "traefik.enable=true" #This sets traefik rules 
      - "treafik.frontend.rule=Host:${HOST}" #This sets traefik rules 
    volumes: #(formatting is path_on_server:path_within_container)
      - jupyterhub_data:/srv/jupyterhub #This binds the volume to the container path
      - /var/run/docker.sock:/var/run/docker.sock #this allows the container to run docker commands
volumes: #volumes are created here, but bound in the service description (see example above for jupyterhub)
  - jupyterhub_data: #tells docker to create a volume. Docker volumes are created under /var/lib/docker/volumes

```

## Traefik

This file contains the Traefik configuration such as domain, email and LetsEncrypt implementation. Example of this file are easily found on Google. This is the standard config of Traefik + LetsEncrypt. 

## conda-activate.sh

This file is copied to **/usr/local/bin/before-notebook.d/** during the build process of jupyterlab_img. The file is responsible for launching hooks before a Lab instance is started. This means that everything that is specified in this file **is executed before a Lab instance is launched**.

## Jupyterlab image

Jupyterlab service is only there to build the Jupyterlab image that is used to fire up instances of Lab for every user that signs in. This container makes the jupyterlab_img. It is very important to know that this Dockerfile defines the base image that Hub uses to spawn user JupyterLab instances. This means that everything in the Dockerfile will be propagated to the jupyterlab_img. This is the BASE image, eg. what you want users to have at the first start of their Lab container. For example the file conda-activate.sh is copied to /usr/local/bin/before-notebook.d/ , this is a directory that holds scripts that are run before before a Lab environment starts. 

## Volumes

**jupyterhub_jupyterhub_data**: Contains JupyterHub data (persistent)
**jupyterhub_postgres_data**: Contains postgres data (for MLflow)
**jupyterhub-shared**: This is the shared volume (mounted as /shared in user Lab containers)
**jupyterhub-user-{user}**: The Lab volume for every user different (/home/jovyan)
