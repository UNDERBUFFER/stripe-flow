stripe-flow
===========

Development
-----------

* `cp .env.template .env` and change values for yourself
* `docker build ./ -t rishat_test_task` build image
* `docker-compose up` start

* If the application starts from scratch:
    * `docker exec -it stripeflow_app_1 /bin/bash`
    * `python manage.py migrate`
    * `python3 manage.py createsuperuser` 
    * go to the `http://localhost:7070/admin/` and create Item objects with price ids from stripe dashboard
* Else:
    * `docker exec stripeflow_db_1 psql -U postgres rishat < dump.sql`
    * `docker exec -i stripeflow_db_1 /bin/bash -c "PGPASSWORD=toor psql --username postgres rishat" < ~/dump.sql`
    * go to the `http://localhost:7070/admin/` and update Item objects with price ids from stripe dashboard

* `ngrok http 7070 --log=stdout > ngrok.log &`

URLS
----

* GET `/item/N/` - item page (button buy is hidden for items without `api_price_id` value)
* GET `/cart/` - check cart and buy button for redirect to stripe
* API POST `/cart/add/` - add element to order
* API POST `/cart/buy/` - call stripe

Restore
-------
* `docker exec -i stripeflow_db_1 /bin/bash -c "PGPASSWORD=toor pg_dump --username postgres rishat" > ./dump.sql`



