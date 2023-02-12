stripe-flow
===========

Development
-----------

* `cp .env.template .env`
* `docker build ./ -t rishat_test_task`
* `docker-compose up`

* If the application starts from scratch:
    * `docker exec -it rishat_app_1 /bin/bash`
    * `python manage.py migrate`
    * `python3 manage.py createsuperuser` 
    * go to the `http://localhost:7070/admin/` and create Item objects with price ids from stripe dashboard
* Else:
    * `docker exec rishat_db_1 psql -U postgres rishat < dump.sql`
    * go to the `http://localhost:7070/admin/` and update Item objects with price ids from stripe dashboard

URLS
----

* GET `/item/N/` - item page (button buy is hidden for items without `api_price_id` value)
* GET `/cart/` - check cart and buy button for redirect to stripe

API
---

* POST `/cart/add/` - add element to order
* POST `/cart/buy/` - call stripe



