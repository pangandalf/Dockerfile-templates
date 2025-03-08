# Dockerfiles templates
A collection of ready-to-use `Dockerfile` templates for various technologies and use cases.

### Usage

1. Go to directory with selected `Dockerfile`
```bash
cd path/to/Dockerfile
```

2. Build image
```bash
docker build -t tag .
```

3. Create container
```bash
docker run -it [--network=none] -v [/path/on/host:/path/in/container] [--name name] image_name
```

4. Start and enter (exec) container
```bash
docker start -ai container_name
```

