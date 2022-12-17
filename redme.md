# Django Streaming Test


En este repositorio se encuentra todo el código fuente de la prueba técnica que estoy<br/>
realizando para el puesto de Python Backend Developer en [alternova](https://alternova.co/) .

La prueba técnica consiste en la creación de una API de una plataforma de streaming.

Para este proyecto estoy utilizando:

* [Django](https://www.djangoproject.com/) Como framework base
* [Django rest Framework (DRF)](https://www.django-rest-framework.org/) para la creacion de la api
* [AWS](https://aws.amazon.com/) para desplegar el proyecto en un servidor

### Instalación

Para ejecutar el proyecto correctamente es indispensable tener `pip3` instalado en tu computador.
```
$ https://github.com/SirRiuz/movies-backend/
$ cd movies-backend
$ pip3 install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```
Tambien puedes ir a [LIVE DEMO](http://44.204.19.35:9000/api/v1/auth/login/) y hacer uso del proyecto desplegado en amazon,
es más fácil porque<br/> no tienes que instalar nada, solo tienes que realizar las peticiones y listo.
<br/>

## Endpoints

Estas son todas las rutas que me permitem interactuar con los `Items`. [Live demo](http://44.204.19.35:9000/api/v1/auth/login/)

Method | HTTP request | Description | Payload
 ------------- | ------------- | -------------|-------------
**POST** | [/auth/login/](http://44.204.19.35:9000/api/v1/auth/login/) | Permite autenticar un usuario | `email` `password`
**POST** | [/auth/register/](http://44.204.19.35:9000/api/v1/auth/register/)| Permite crear un nuevo usuario | `username` `email` `password`
**GET** | [/random-item/](http://44.204.19.35:9000/api/v1/random-item/)| Devuelme un item aleatorio
**GET** | [/items/](http://44.204.19.35:9000/api/v1/items/)| Devuelme un listado con todos los items | `?order_by=name` Permite organizar los item por su nombre <br/><br/>  `?order_by=rate` Permite organizar los item por su puntuacion <br/> <br/> `?q=foo` Permite filtrar items por su nombre
**GET** | [/items-views/](http://44.204.19.35:9000/api/v1/items-views/)| Devuelme un listado con todos los items marcados como visto
**GET** | [/item/:id/](http://44.204.19.35:9000/api/v1/item/1/)| Devuelve los datos de un solo item en espesifico
**POST** | [/items/:id/view/](http://44.204.19.35:9000/api/v1/item/1/view/)| Permite marcar un item como visto
**POST** | [/items/:id/rating/](http://44.204.19.35:9000/api/v1/item/1/rating/)| Permite puntuar un item en espesifico | `score` Numero de puntiacion. Este va del 1 al 5
