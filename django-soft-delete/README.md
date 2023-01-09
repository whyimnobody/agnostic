### Django Soft Delete
Collection of code bits for soft-deleting objects in Django

From [https://adriennedomingus.com/blog/soft-deletion-in-django]()

cd into your utils folder, then download the files to the folder. Then done.

```shell
curl -o admin.py https://gitlab.com/-/snippets/2343777/raw/main/admin.py
curl -o managers.py https://gitlab.com/-/snippets/2343777/raw/main/managers.py
curl -o models.py https://gitlab.com/-/snippets/2343777/raw/main/models.py
curl -o querysets.py https://gitlab.com/-/snippets/2343777/raw/main/querysets.py
```


### Web Development Backend
A collection of services as Docker containers, for typical web development.

Includes:
- Postgres
- pgAdmin4
- Redis
- mailhog

**Don't forget to create the volume as described, or change the reference accordingly**

_But what about your actual app?_

Just edit the bloody thing, and stop asking so many questions

To replace the `app_name` variable, you can use `sed`, for example:

```shell
curl -o docker-compose.yml https://raw.githubusercontent.com/whyimnobody/agnostic/master/web-dev-backend.yml
sed -i '' 's/{{app_name}}/something_creative/' docker-compose.yml
```
