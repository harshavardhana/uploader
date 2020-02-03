# mrq
MinIO uploader example with redis queues

## Background upload Tasks in Python with RQ
RQ (Redis Queue) makes it easy to add background tasks to your Python applications. RQ uses a Redis database as a queue to process background jobs. To get started using RQ, you need to configure your application and then run a worker process in your application.

## Configuration

- Install redis and start `redis-server`

- To setup RQ and its dependencies, install it using pip

```
$ pip install rq
```

## Create a worker
Now that we have everything we need to create a worker process, let’s create one.

```
~ rqworker high default low
17:36:43 Worker rq:worker:7da083fd94844942b0bf6f6e46ec850d: started, version 1.2.2
17:36:43 *** Listening on high, default, low...
```

## Queuing jobs
```
~ python3 uploader.py
None
0c330f1a75e8dbe162215bb1cb497e9c-8
```

Upon success rqworker console should see following output
```
17:36:43 Worker rq:worker:7da083fd94844942b0bf6f6e46ec850d: started, version 1.2.2
17:36:43 *** Listening on high, default, low...
17:36:46 default: upload.upload.upload('testbucket', 'emacs', '/usr/bin/emacs') (50787b37-5fdb-4ac5-b37c-a00ab868f518)
uploading /usr/bin/emacs => testbucket/emacs ..
uploaded testbucket/emacs .. 0c330f1a75e8dbe162215bb1cb497e9c-8
17:36:46 default: Job OK (50787b37-5fdb-4ac5-b37c-a00ab868f518)
17:36:46 Result is kept for 500 seconds
```
