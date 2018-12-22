# iReporter API
[![Build Status](https://travis-ci.com/Manorlds-Eaglespark/i_reporter_api.svg?branch=ft-tests)](https://travis-ci.com/Manorlds-Eaglespark/i_reporter_api)       [![Coverage Status](https://coveralls.io/repos/github/Manorlds-Eaglespark/i_reporter_api/badge.svg?branch=develop)](https://coveralls.io/github/Manorlds-Eaglespark/i_reporter_api?branch=develop)      [![Maintainability](https://api.codeclimate.com/v1/badges/081ad690f6cad3b3ca9d/maintainability)](https://codeclimate.com/github/Manorlds-Eaglespark/i_reporter_api/maintainability)

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

* Install all the dependencies
  
  ```pip install requirements.txt```

* Switch to the appropriate branch and follow along.


# Heroku API Endpoints

* GET /api/v1/red-flags       - Fetch all red-flag records.
* GET /api/v1/red-flags/<red-flag-id>       - Fetch a specific red-flag record.
* POST /api/v1/red-flags      - Create a red-flag record.
* PATCH /api/v1/red-flags/<red-flag-id>/location       - Edit the location of a specific red-flag record.
* PATCH /api/v1/red-flags/<red-flag-id>/comment       - Edit the comment of a specific red-flag record.
* DELETE /api/v1/red-flags/<red-flag-id>          - Delete a specific red flag record.

# Hosted API
https://ireporter256.herokuapp.com

### AUTHOR
* [Anorld Mukone](https://github.com/Manorld-Eaglespark)
