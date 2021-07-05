# Luxor Interview

## Installing and Running

* Ensure you have the following two packages installed: `apt-get install libpq-dev python3-dev`.
* Clone the file into your working directory: `git clone https://github.com/felixsuarez0727/stratum_server_v1.git`
* Install the requirements file: `pip3 install -r requirements.txt`
* Turn the database service on: `docker-compose up`
* Execute the service: `python3 server/svc.py`

## Testing

* You can have check to the database by executing below command:

`psql -h localhost -p 5432 -d luxor -U luxor`

* You can test our mock service by executing below command:

`bash server/test/test_svc.sh`

# Deployment in GCP.

The system was deployed in GCP and it will be online for a couple of weeks. See below documentation for testing and more details:

http://34.136.5.130:5001/api/browse

![image](https://user-images.githubusercontent.com/25110207/124396234-83a18200-dcc5-11eb-8c11-42d7594741e1.png)
