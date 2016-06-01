# sample-h2o-mruby

Sample setup for h2o + mruby


## Install h2o

```
./install-h2o.sh
```


## Start h2o

```
./h2o/h2o-2.0.0/h2o -c h2o.conf

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
    Latency     6.81ms    7.44ms  54.12ms   81.31%
    Req/Sec     1.09k   218.98     1.61k    85.00%
  21706 requests in 10.06s, 8.51MB read
Requests/sec:   2158.31
Transfer/sec:    866.27KB
```


```
$ wrk http://localhost:8080/mruby/
Running 10s test @ http://localhost:8080/mruby/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.53ms   18.33ms 202.13ms   94.82%
    Req/Sec   835.83    370.94     1.80k    63.64%
  16596 requests in 10.07s, 4.99MB read
Requests/sec:   1647.55
Transfer/sec:    506.82KB
```

```
$ wrk http://localhost:8080/qs/
Running 10s test @ http://localhost:8080/qs/
  2 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.20ms   19.17ms 198.43ms   95.17%
    Req/Sec     0.92k   453.98     1.82k    55.61%
  18011 requests in 10.06s, 2.73MB read
Requests/sec:   1790.71
Transfer/sec:    278.05KB
```
