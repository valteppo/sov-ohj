# Nettikirppis

## Alku:

Django generoi ainakin tuonne nk_projects settings.py tiedostoon jotain avaimia jotka todennäköisesti ovat erit joka koneella.
Python enviromentit pitää todennäköisesti asentaa itse, laitoin ne gitignoreen.

### Ohjeet:
Tee kansio oma kansio.
Kansiossa avaa komentorivi.
Kloonaa git repo:

```git@github.com:valteppo/sov-ohj.git```

Vaihda kansio sov-ohj:

```cd sov-ohj```

Asenna folderiin nk_env komennolla

```python3 -m venv nk_env```

Aktivoi komentorivillä

```source nk_env/bin/activate```

Django ver. 4.2.16 komennolla

```pip install django==4.2.16```

Projektin pitäisi toimia.

## Superuser

superuser: admin

pw: admin

