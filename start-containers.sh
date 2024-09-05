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

# Handle arguments for Docker Compose
DETACHED_MODE=""
BUILD_MODE=""

for arg in "$@"; do
    case $arg in
        -d|--detach)
        DETACHED_MODE="-d"
        shift # remove argument from processing
        ;;
        --build)
        BUILD_MODE="--build"
        shift # remove argument from processing
        ;;
        *)
        ;;
    esac
done

# Run Docker Compose
echo "Starting Docker Compose with options: $BUILD_MODE $DETACHED_MODE"
docker compose up $BUILD_MODE $DETACHED_MODE
