from rq import Queue
from redis import Redis
from upload import upload

import time

# Tell RQ what Redis connection to use
q = Queue(connection=Redis())

job = q.enqueue(upload, 'testbucket', 'emacs', '/usr/bin/emacs')
print(job.result) # => None

# Now, wait a while, until the worker is finished
time.sleep(5)
print(job.result) # => etag
