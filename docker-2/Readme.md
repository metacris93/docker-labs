## Setting up

```sh
docker build -t python-flask-api:0.1 .
docker run -it --rm -d -p 80:5000 --name api python-flask-api:0.1
```