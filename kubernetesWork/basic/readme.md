run kubectl get pods -o wide --all-namespaces
if theres no ingress controller --> minikube addons enable ingress --> check again
run kubectl describe pod <nginx ingress controller pod> --namespace <its namespace> | grep Ports
run kubectl port-forward <nginx ingress controller> 3000:<nginx tcp port> --namespace <nginx namespace>
you can now reach at http:localhost:3000
