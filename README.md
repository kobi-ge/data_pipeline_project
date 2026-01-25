# run localy
* **3 terminals**
1. `uvicorn server-a.app.main:app --host 0.0.0.0 --port 8000--reload`
2. `uvicorn server-b.app.main:app --host 0.0.0.0 --port 8001 --reload`
3. `uvicorn server-c.app.main:app --host 0.0.0.0 --port 8002 --reload`
but you need to create network so use compose

# run compose
from root dir run **docker compose up -d**
to see the data in sql run `docker exec -it mysql_container mysql -u root -p` and use sql queries

# k8s

`kubectl apply -f k8s`

`minikube service service-a`
**to see in sql**
`kubectl exec -it mysql-0 -- mysql -u root -p`

# clean
`kubectl delete all --all`
`kubectl delete pvc --all`