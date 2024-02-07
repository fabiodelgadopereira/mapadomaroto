# To create a Docker image locally that displays a simple HTML page, you can follow these steps:

## 1. Create a new directory for your project and navigate to it:
```bash
mkdir my-html-page
cd my-html-page
touch index.html
touch dockerfile
```

## 2. Create an index.html file with the following content:
```html
<!DOCTYPE html>
<html>
  <head>
    <title>My HTML Page</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
```

## 3. Create a Dockerfile with the following content:
```bash
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
```

This Dockerfile uses the nginx:alpine base image and copies the index.html file to the default Nginx web root directory.

## 4. Build the Docker image:
```bash
docker build -t my-html-page .
```

This command builds the Docker image with the tag my-html-page.

## 5. Run the Docker container:
```bash
docker run -d -p 8080:80 my-html-
```

This command runs the Docker container in detached mode (-d) and maps port 8080 on the host to port 80 on the container (-p 8080:80).

    Open a web browser and navigate to http://localhost:8080 to view your HTML page.

You should see a "Hello, World!" heading displayed on the page.

Note: You can customize the HTML page by modifying the index.html file and rebuilding the Docker image.

## Troubleshooting

Add your user to the docker group:
```bash
sudo usermod -aG docker.socket $USER
```

How to fix "dial unix /var/run/docker.sock: connect: permission denied" when group permissions seem correct?
```bash
sudo setfacl --modify user:$USER:rw /var/run/docker.sock
```

Stop all the containers
```bash
docker stop $(docker ps -a -q)
```

Remove all the containers
```bash
docker rm $(docker ps -a -q)
```

“Process Status”, shows all of the Docker processes actively running.
```bash
docker ps -a
```

List all ports
```bash
lsof -i -P -n
```