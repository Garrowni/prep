

## Services
<img src="./images/services.png" />

### ClusterIP Service
<img src="./images/clusterIP.png" />
Use Case:
- internal communication within cluster
External Access: No
LB : Yes
Internal Communication: Yes
Stable Network Identities: No

### NodePort Service
<img src="./images/nodeport.png" />

Use Case:
- external access to services from outside the cluster
External Access: yes
LB: yes
Internal Communication: yes
Stable Network Identities: 

### LoadBalancer Service
<img src="./images/lb.png" />
Use Case:
- exposing services externally in cloud environments
External Access: yes
LB: yes
Internal Communication: yes
Stable Network Identities: no

### ExternalName Service
<img src="./images/externalName.png" />
Use Case:
- mapping service to an external DNS name
External Access: no
LB: no
Internal Communication: yes
Stable Network Identities: no

### Headless Service
<img src="./images/headless.png">
Use Case:
- stateful apps requiring stable identities
External Access: no
LB: no
Internal Communication: yes
Stable Network Identities: yes

### Ingress
<img src="./images/ingress.png" />

NGINX
<img src="./images/nginx-ingress.png"/>
- independent of your service
- enables routing rules to be consolidated in one place
