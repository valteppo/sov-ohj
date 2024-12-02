# Nettikirppis

### Alku:

Django generoi ainakin tuonne nk_projects settings.py tiedostoon jotain avaimia jotka todennäköisesti ovat erit joka koneella.
Python enviromentit pitää todennäköisesti asentaa itse, laitoin ne gitignoreen.

Asenna folderiin nk_env komennolla

```python3 -m -venv nk_env```

Aktivoi komentorivillä

```source nk_env/bin/activate```

Django ver. 4.2.16 komennolla

```pip install django==4.2.16```

Django projekti nimellä nk_project

```django-admin startproject nk_project .```

Database

```python manage.py migrate```

Nettikirppis sivuston main app

```python manage.py startapp nettikirppis```



