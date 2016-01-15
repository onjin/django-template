## Configuration

Configure project using env vars (http://12factor.net/).

Put settings withing a local `.env` file.

For example:

```
PORT=80
SECRET_KEY=asdf
DATABASE_URL=postgres://user:pass@docker0ip/dbname
DEBUG=1
HOSTNAME=myhostname.dev
```

To use with `nginx-proxy` (https://github.com/jwilder/nginx-proxy) add:

```
VIRTUAL_HOST=myhostname.dev
```

To create local `.dev` DNS add file `/etc/dnsmasq.d/dev`:

```
address=/dev/127.0.0.1
```


## Build docker

```
docker build -t myproject .
docker run -d -v `pwd`/media:/app/public/media --env-file .env myproject
```




