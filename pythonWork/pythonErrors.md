Error:
```
(venv) ngarrow@PS-MacBook-Pro simpleSocket % python
 client.py 
Traceback (most recent call last):
  File "/Users/ngarrow/Documents/repos/PersonalNonRepo/pythonWork/pyNetworking/simpleSocket/client.py", line 7, in <module>
    s.connect((host, port))
socket.gaierror: [Errno 8] nodename nor servname provided, or not known
```
Fix:
For me I fixed this by
1. sudo su
2. echo 127.0.0.1 $HOSTNAME >> /etc/hosts
3. (optional/or alternative depending on machine) echo 127.0.0.1 $HOST >> /etc/hosts