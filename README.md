# sample-h2o-mruby

Sample setup for h2o + mruby


## Install h2o

```
./install-h2o.sh
```


## Start h2o

```
./h2o/h2o-1.5.0/h2o -c h2o.conf

[INFO] raised RLIMIT_NOFILE to 10240
h2o server (pid:39147) is ready to serve requests
```

## Access

```
$ curl http://localhost:8080/
<!DOCTYPE html>
<html>
  <head>
    <title>Welcome to H2O</title>
  </head>
  <body>
    <p>Welcome to H2O - an optimized HTTP server</p>
    <p>It works!</p>
  </body>
</html>
```

```
$ curl http://localhost:8080/mruby/
hello from h2o_mruby. User-Agent:curl/7.43.0 New User-Agent:new-curl/7.43.0-h2o_mruby path:/ host:localhost:8080 method:GET query:
```
