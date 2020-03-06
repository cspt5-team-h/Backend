# backend

# Django Migrate On Heroku
```bash
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py create_world
```

# API Interaction Guide
```bash
# register account
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' http://csp5.herokuapp.com/api/registration/

# login --> return token id
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' http://csp5.herokuapp.com/api/login/

#initialize
curl -X GET -H 'Authorization: Token 3ae2c5c513f8441217498f1c36e9d9b0b0ecc808' http://csp5.herokuapp.com/api/adv/init/

# move
curl -X POST -H 'Authorization: Token 3ae2c5c513f8441217498f1c36e9d9b0b0ecc808' -H "Content-Type: application/json" -d '{"direction":"n"}' http://csp5.herokuapp.com/api/adv/move/

# say
curl -X POST -H 'Authorization: Token 3ae2c5c513f8441217498f1c36e9d9b0b0ecc808' -H "Content-Type: application/json" -d '{"message":"Hello, world!"}' http://csp5.herokuapp.com/api/adv/say/
```