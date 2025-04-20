# 🐳 Dockerfiles templates
A collection of ready-to-use `Dockerfile` templates for various technologies and use cases.

## 🚀 Usage

1. Go to the directory with the selected `Dockerfile`:
    ```bash
    cd path/to/Dockerfile
    ```

2. Build the image:
    ```bash
    docker build -t image_name:latest .
    ```

3. Create and run a container:
    ```bash
    docker run -it \
        --network=none \
        -v /path/on/host:/path/in/container \
        --name container_name \
        image_name
    ```
    > Note: All flags are optional

4. Start and attach to an existing container:
    ```bash
    docker start -ai container_name
    ```

## 📁 Directory structure

```text
.
├── debian/
│   └── Dockerfile
├── python/
│   ├── app.py
│   └── Dockerfile
├── rockylinux/
│   └── Dockerfile
└── ubuntu/
    ├── flusk/
    │   └── Dockerfile
    └── ns3/
        └── Dockerfile
```
