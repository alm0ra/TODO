## TODO

**TODO API Guide**
----
  Returns json data about a single user.

* **URLS**

    *`Get Token to Auth`             `POST`                 /api-token-auth/
    *`Return Task's List`            `GET`                  /task-list/
    *`Return Done Task's List`       `GET`                  /done-list/
    *`get Details, Update, Delete`   `GET` `PUT` `DELETE`   /task-detail/<str:pk>
    *`Create a Task`                 `POST`                 /task-create/
    *`Make a Task Done`              `GET`                  /move-done/<str:pk>
    *`Make a Task UnDone`            `GET`                  /move-task/<str:pk>


* **Method:**

  `GET`|`POST`|`PUT`|`DELETE`
  
#### How Generate Token

* **Get Token Key**

```bash
$ curl -X POST -H "Content-Type: application/json" \
    -d '{"username": <your-user-name>, "password": "<your-password>"}' \
    http://127.0.0.1:8001/api/api-token-auth/
```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{"token":"ce821f60a5bb332a8bd9537b2008bbdd4729d908"}`
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `{"non_field_errors":["Unable to log in with provided credentials."]}`



#### Examples(Get Task List)

* **Send Get Request**

```bash
curl -X GET -H "Authorization:Token <insert-yourtoken>" \
    http://127.0.0.1:8001/api/task-list/
```

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[{"title":"Task1","status":false},...]`
 
* **Error Response:**

  * **Code:** 401 Unauthorized <br />
    **Content:** `{"detail": "Invalid token."}`

  * **Code:** 401 Unauthorized <br />
    **Content:** `{"detail": "Invalid token."}`
    or 
    **Content:** `{"detail": "Authentication credentials were not provided."}`
