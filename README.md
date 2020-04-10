# CoronaCircles
This is an open-source project meant to bring people together at this difficult time with the corona virus.
For the future it is planned to exist independently from the corona pandemic, but for now the project is sticked to this topic.

## The target
Since many people are looking for social contact without needing to be in person, but still beeing close together,
we brang this project to life for exactly those people. We want to achieve this by letting people crate a so called 
"Corona Circle" which ultimately is nothing more than a Jitsi Meeting room to communicate via Video or just by Audio.

## Project details
This project is based on django-cms, which basically is nothing more than an wrapper around django.
This project also is written in Python 3.7, so don't expect it to work with other Python versions.

## Models / DB-Tables
- UserProfile
    - ID
    - username
    - emailadress
- Event
    - ID
    - scheduled datetime
    - name/title
    - participants (user ID's as csv)
    - description

visualized: https://dbdiagram.io/d/5e905d1c39d18f5553fd673f


