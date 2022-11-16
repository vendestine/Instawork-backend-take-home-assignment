## How to setup the project

1. Install python and mysql on your machine.
2. Locate to the project by terminal or open the project by an IDE such as Pycharm and so on.
3. Execute the following commands：
```
pip install django
pip install djangorestframework
pip install pymysql
```
4. Config the mysql in settings.py
The default is 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'member',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
You can modify the NAME, USER, and PASSWORD according to your mysql config environment.

5. Create the database and table in the mysql or you can use the command to migrate automatically:
```
python manage.py migrate 
```


## How to run the project
```
python manage.py runserver 9000 
```

## How to test the project

### for linux

List members
```
curl --location --request GET 'http://127.0.0.1:9000/users'
```

Add a team member
```
curl --location --request POST 'http://127.0.0.1:9000/users' \
--header 'Content-Type: application/json' \
--data-raw '{"userId": 4, "firstName": "David", "lastName": "Jones", "phone": "+15101234567", "emailId": "test@test.com", "role": "admin"}'
```

Edit a team member
```
curl --location --request PUT 'http://127.0.0.1:9000/users/4' \
--header 'Content-Type: application/json' \
--data-raw '{"userId": 4, "firstName": "David", "lastName": "Jones", "phone": "+15101234567", "emailId": "test@test.com", "role": "regular"}'
```

Delete a team member
```
curl --location --request DELETE 'http://127.0.0.1:9000/users/4'
```

### for windows

List members
```
curl --location --request GET "http://127.0.0.1:9000/users"
```

Add a team member
```
curl --location --request POST "http://127.0.0.1:9000/users" ^
--header "Content-Type: application/json" ^
--data-raw "{\"userId\": 4, \"firstName\": \"David\", \"lastName\": \"Jones\", \"phone\": \"+15101234567\", \"emailId\": \"test@test.com\", \"role\": \"admin\"}"
```

Edit a team member
```
curl --location --request PUT "http://127.0.0.1:9000/users/4" ^
--header "Content-Type: application/json" ^
--data-raw "{\"userId\": 4, \"firstName\": \"David\", \"lastName\": \"Jones\", \"phone\": \"+15101234567\", \"emailId\": \"test@test.com\", \"role\": \"regular\"}"
```

Delete a team member
```
curl --location --request DELETE "http://127.0.0.1:9000/users/4"
```
