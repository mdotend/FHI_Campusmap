# FHI Campusmap
This project contains a web application, that displays the area of the FHI campus in Berlin, Germany and offers the possibility to add eadible plants on the grounds.
The type of plants can be specified and assigned with further informations, pictures etc.
The project uses the django webserver with an dockerized postgres db and the core functionality is based on the leaflet project.

## Preparation
under fhi/fhi an .env file has to be created and must contain the following values

POSTGRES_PASSWORD=<POSTGRES_PASSWORD><br>
DJANGO_SECRET=<DJANGO_SECRET>
