Ubicarse en el directorio raiz donde esta el archivo Dockerfile
Ejecutar:
```sh
docker build . -t website:latest
```

Borrar la imagen:
```sh
docker rmi -f 4d5d15d91bab
```

```sh
docker run -it --rm -d -p 80:80 --name mysite website
```

```sh
docker build -t website:1.5 .
```

```sh
docker images --filter=reference='*:1.0'
docker image tag website:latest admin/website:latest
docker rmi -f <IMAGE ID>

docker run -it --rm -d -p 80:80 -v $(pwd)/website:/usr/share/nginx/html/website --name site website:0.1
docker run -it --rm -d -p 81:80 --name site81 website:0.1
```