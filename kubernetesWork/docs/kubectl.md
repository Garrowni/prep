
check for taints
`kubectl describe nodes minikube | grep -i taints`
Create a taint so that resources with app=web will not be scheduled on node minikube
`kubectl taint node minikube app=web:NoSchedule`
change context (move between clusters)
`kubectl config use-context`
get all object types
`kubectl api-resources`
get status of each control plane component
`kubectl get componentstatus`



