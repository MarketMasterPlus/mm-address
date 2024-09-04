#!/bin/bash

# Installing Docker if not already installed
if ! [ -x "$(command -v docker)" ]; then
    echo 'Error: Docker is not installed.' >&2
    echo 'Installing Docker...'
    curl -fsSL https://get.docker.com | sh
    echo 'Docker installed successfully.'
fi

# Installing Docker Compose if not already installed
if ! [ -x "$(command -v docker compose)" ]; then
    echo 'Error: Docker Compose is not installed.' >&2
    echo 'Installing Docker Compose...'
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    echo 'Docker Compose installed successfully.'
fi

# Create Docker network if it doesn't exist
NETWORK_NAME="marketmaster-network"
if [ -z "$(docker network ls --filter name=^${NETWORK_NAME}$ --format={{.ID}})" ]; then
    docker network create $NETWORK_NAME
    echo "Created Docker network named $NETWORK_NAME"
else
    echo "Docker network $NETWORK_NAME already exists"
fi

# Run Docker Compose
DETACHED_MODE=""
if [[ $1 == "-d" ]]; then
    DETACHED_MODE="-d"
fi

echo "Starting Docker Compose..."
docker compose up $DETACHED_MODE
