# junyi08.com's source code
This project is [junyi08.com](http://junyi08.com)'s source code
#run
Go to the root of source code(contain `manage.py`),and create `env.json` file.

env.json's content:
```
{
	"env":"dev", // if it's production, change it to other word
	"SECRET_KEY":"Your secret key"
}
```
run `python manage.py migrations&&python manage.py migrate` to create database
`python manage.py create superuser`to create manager

Finally, run `python manage.py runserver` and view at [127.0.0.1:8000](http://127.0.0.1:8000)!

For more information visit django's website