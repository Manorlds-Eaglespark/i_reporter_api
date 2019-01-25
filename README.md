# iReporter API
[![Build Status](https://travis-ci.org/Manorlds-Eaglespark/i_reporter_api.svg?branch=develop)](https://travis-ci.org/Manorlds-Eaglespark/i_reporter_api)       [![Coverage Status](https://coveralls.io/repos/github/Manorlds-Eaglespark/i_reporter_api/badge.svg?branch=develop)](https://coveralls.io/github/Manorlds-Eaglespark/i_reporter_api?branch=develop)       [![Test Coverage](https://api.codeclimate.com/v1/badges/081ad690f6cad3b3ca9d/test_coverage)](https://codeclimate.com/github/Manorlds-Eaglespark/i_reporter_api/test_coverage)

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter. iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

## GETTING STARTED
* Clone this repo using 

  ```git clone https://github.com/Manorlds-Eaglespark/i_reporter_api.git```

* Then change directory to the new folder
  
  ```cd <Directory-Name> ```

* Create a virtual environment
  
  ```virtualenv <virtual-env-name>```

* Activate the virtual environment

  ```. <virtual-env-name>/bin/activate```

* Switch to the appropriate branch and follow along.

## REQUIREMENTS

* Install all the dependencies in your virtual environment
  
  ```pip install requirements.txt```

## PREREQUITES
- A Working computer. Linnux, windows or Mac OS
- Postman, to test endpoints
- Git, to follow different repo branches smoothly.
- Text Editor, preferably Visual Studio Code.

## TESTING
* Install Pytest to run the unittests
```pip install pyteset```
* Run tests by entering pytest into your terimal.
* To get your test coverage locally, use
```pytest --cov=.```

# Heroku API Endpoints

| HTTP Method  | End Point       | Public Access      |  Action            |
| :------------:|:---------------:| :---------------:|:---------------------:|
| POST    | /api/v1/auth/register | TRUE |  Create an account.  |
| POST    | /api/v1/auth/login | TRUE |  User login.  |
| GET    | /api/v1/red-flags | TRUE |  Fetch all red-flag records.  |
| GET    | /api/v1/red-flags/<red-flag-id>        |  TRUE |   Fetch a specific red-flag record.    |
| POST   | /api/v1/red-flags        |    TRUE |   Create a red-flag record.   |
| PATCH  | /api/v1/red-flags/<red-flag-id>/location  | TRUE  |   Edit the location of a specific red-flag record.  |
| PATCH  | /api/v1/red-flags/<red-flag-id>/comment  | TRUE   |   Edit the comment of a specific red-flag record.  |
| DELETE | /api/v1/red-flags/<red-flag-id>  |  TRUE  |   Delete a specific red flag record.   |

| GET    | /api/v1/interventions/<intervention-id>        |  TRUE |   Fetch a specific red-flag record.    |
| POST   | /api/v1/interventions        |    TRUE |   Create a red-flag record.   |
| PATCH  | /api/v1/interventions/<intervention-id>/location  | TRUE  |   Edit the location of a specific red-flag record.  |
| PATCH  | /api/v1/interventions/<intervention-id>/comment  | TRUE   |   Edit the comment of a specific red-flag record.  |
| DELETE | /api/v1/interventions/<intervention-id>  |  TRUE  |   Delete a specific red flag record.   |

## Built With
Python 3.6, Flask Micro-framework

## Tools Used
-Pylint
-Pytest
-Virtual environment

## Documentation
Find Documentation [here](https://app.swaggerhub.com/apis/Manorlds-Eaglespark/iReporter/1.0.0)

## Hosted API
Follow this [link](https://ireporter256.herokuapp.com)

## Host UI Demo
This app has a UI, in HTML, CSS and Javascript. find it [here](https://manorlds-eaglespark.github.io/i_reporter/)

## AUTHOR
Anorld Mukone - [Github profile here](https://github.com/Manorlds-Eaglespark)
