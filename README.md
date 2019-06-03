# Simple API Service

Use this project as a starting point for creating a new microservice that calls out to a 3rd party API.

## Setup

#### Cloning the Repo

* Clone it.  `git clone git@github.com:LumavateTeam/python-simple=api-service.git <PROJECT_NAME>`
* Switch to dir.  `cd <PROJECT_NAME>`
* Remove remote origin. `git remote remove origin`
* Create new <PROJECT_NAME> repository in github.
* Add the new origin pointing to <PROJECT_NAME>.  `git remote add origin git@github.com:<REPO>/<PROJECT_NAME>.git`
* Push everything to <PROJECT_NAME> repository.  `git push -u origin master`

#### NPM Install

Run `npm install` in your projects working directory.

#### Build <PROJECT_NAME> Docker Image

* Naviagte to <PROJECT_NAME> root directory
* Build your docker image by running the following command. `docker build -t python-simple-api-service:develop .`

#### Add docker-compose Configuration

Update the docker-compose file to replace <PROJECT_DIRECTORY> to the pertient local directories

## Trying it Out

Using the contained docker-compose, you can run ./run-compose which will use the docker-compose configuration after getting your current IP for use with
Docker.

## Routes

### Route: /data

#### Call:GET

*** Communication: server-server only

Purpose: Get a list of all data from the given API Endpoint

Headers:<br/>
Authorization: Bearer{{access_token}}<br/>
Content-Type: application/json

Expected Response:
```bash
{
  "payload": {
    "data": {
      "<apiField1>": "<apiFieldValue1>",
      "<apiField2>": "apiFieldValue2>",
			...
    }
  }
}
```
