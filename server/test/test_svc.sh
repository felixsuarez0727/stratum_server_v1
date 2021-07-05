curl -i -X POST -H "Content-Type: application/json; indent=3" -d '{"method": "mining.authorize","params": ["11","12"],"id": "1"}' http://localhost:5001/api
curl -i -X POST -H "Content-Type: application/json; indent=3" -d '{"method": "mining.subscribe","params": ["felix0727"],"id": "1"}' http://localhost:5001/api
curl -i -X POST -H "Content-Type: application/json; indent=3" -d '{"method": "mining.notify","id": "1"}' http://localhost:5001/api
