# Contact API for studies

This is a simple API for studies. It is a REST API that uses JSON for data exchange.

## TODO LIST:

- [ ] Wait for new VM on Oracle Cloud
- [ ] Create Dockerfile
- [ ] Create Docker-compose
- [ ] Unit Test based on Coverage
- [ ] Create Github Workflow to build and push image to Dockerhub when pipeline is successful
- [ ] Integrate this api with mongodb

## Installation

1 - Clone this repository
```bash
git clone https://github.com/bsfraga/contacts-api.git
```
2- Create a virtual environment
```bash
python3 -m venv venv
```
3 - Install dependencies from requirements.txt
```bash
pip install -r requirements.txt
```
3 - Run the application
```bash
python app.py
```

## Swagger Documentation

You can access the swagger documentation on the following link: `http://localhost:5000/api/docs/`