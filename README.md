# sample-h2o-mruby

Sample setup for h2o + mruby


## Install h2o

```
./install-h2o.sh
```


## Start h2o

```
./h2o/h2o-1.6.3/h2o -c h2o.conf

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

## Performance

- Mac OS X 10.11.2
- 4 Core: 1.8 GHz Intel Core i7
- 4 GB 1333 MHz DDR3

```
$ wrk http://localhost:8080/
Running 10s test @ http://localhost:8080/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    15.20ms   21.10ms  53.89ms   78.72%
    Req/Sec     1.48k     1.01k    3.44k    58.70%
  27556 requests in 10.01s, 10.80MB read
Requests/sec:   2754.17
Transfer/sec:      1.08MB
```


```
$ wrk http://localhost:8080/mruby/
Running 10s test @ http://localhost:8080/mruby/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.21ms   18.64ms  59.06ms   86.59%
    Req/Sec     1.23k   774.42     2.77k    62.27%
  23126 requests in 10.00s, 7.34MB read
Requests/sec:   2311.87
Transfer/sec:    751.81KB
```
