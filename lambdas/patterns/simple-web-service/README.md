# simple-web-service


## My Favorite movies

A sample API to record favorite movies. To be consumed by a front end etc.

Note: this is only for domo purposes. DO NOT USE IN PRODUCTION.

```
┌──────────┐   ┌─────────────┐   ┌────────────┐   ┌────────────┐
│          │   │             │   │            │   │            │
│  Client  ├───▶ API Gateway ├───▶   Lambda   ├───▶ DyanamoDb  │
│          │   │             │   │   (CRUD)   │   │            │
│          │   │             │   │            │   │            │
└──────────┘   └─────────────┘   └────▲───────┘   └────────────┘
                                      │                         
                           ┌──────────┴─────────┐               
                           │  Role To Use DDB   │               
                           └────────────────────┘               
```

## Deploy

```bash
sam build 
sam deploy --guided
```

## Endpoints available:

GET /movies: get a list of movies

GET /movies/<id>: get a movie

POST /movies: create a new movie
 - title: str
 - year: int
 
POST /movies/<id>: update a movie
 - title: str
 - year: int
 
DELETE /movies/<id>: delete a movie