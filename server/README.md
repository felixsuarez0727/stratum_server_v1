# Luxor Interview

## Installing and Running

* Ensure you have the following two packages installed: `apt-get install libpq-dev python3-dev`.
* Clone the file into your working directory: `git clone https://github.com/felixsuarez0727/stratum_server_v1.git`
* Install the requirements file: `pip3 install -r requirements.txt`
* Turn the database service on: `docker-compose up`
* Execute the service: `python3 svc.py`

## Testing

* You can have check to the database by executing below command:

`psql -h localhost -p 5432 -d luxor -U luxor`

* You can test our mock service by executing below command:

`bash server/test_svc.sh`

