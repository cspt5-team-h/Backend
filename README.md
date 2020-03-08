# backend

![500 rooms generation](https://github.com/cspt5-team-h/backend/blob/feature/algorithm/500_rooms.png)

## API Interaction Guide
```bash
# register account
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password1":"testpassword", "password2":"testpassword"}' http://csp5.herokuapp.com/api/registration/

# login --> return token id
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"testpassword"}' http://csp5.herokuapp.com/api/login/

#initialize
curl -X GET -H 'Authorization: Token 3ae2c5c513f8441217498f1c36e9d9b0b0ecc808' http://csp5.herokuapp.com/api/adv/init/

# move
curl -X POST -H 'Authorization: Token 3ae2c5c513f8441217498f1c36e9d9b0b0ecc808' -H "Content-Type: application/json" -d '{"direction":"e"}' http://csp5.herokuapp.com/api/adv/move/

# say
curl -X POST -H 'Authorization: Token 3ae2c5c513f8441217498f1c36e9d9b0b0ecc808' -H "Content-Type: application/json" -d '{"message":"Hello, world!"}' http://csp5.herokuapp.com/api/adv/say/

# get map of the room
curl -X GET -H 'Authorization: Token 3ae2c5c513f8441217498f1c36e9d9b0b0ecc808' http://csp5.herokuapp.com/api/adv/rooms/

curl -X GET -H 'Authorization: Token dc2b4cea32402aa0ad1985355a52a05d2248e67e' http://mud-production.herokuapp.com/api/adv/rooms/

```

## Django Migrate On Heroku
```bash
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py create_world
```