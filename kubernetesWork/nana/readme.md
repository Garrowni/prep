1 server + 2 containers
out of the box each pod gets an IP
each pod can talk to eachother using that
they are ephemeral --> die easily
this means if it dies the ip address will change
so we use service!

# services
internal service
--> internal service
    service --> puts static/perm ip address
    lifecycle for pod/service are not connected
external service
--> ingress --> lets have external and give cool names

---

configmap --> external config --> has things like db connection string etc.
    --> connect it to the pod --> lets you not have to rebuild the timage
secrets --> like configmap but would be secure instead :D
            --> should use 3rd party tool to encrypt it

---

data storage
use volumes --> persistent volume claim --> attached physical storage on a hard drive (local machine or remote storage) ex/ S3  k8 cluster doesnt actually do this at all we are responsible for this!

---
deplooyment
 --> the blueprint for the pods
 --> can specifiy # of replicas
 cant use deployment for db because it has a state!
statefulset
    -->specificaly for things like dbs
    --> replicate, scale up, scale down
    --> makes sure synchronized
    --> can be tedious
    --> some people host db outside of cluster and just use a deployment from in k8

