# Django Apı

## Gereksinimler

-Python 3.8+, Django 4.2, PostgreSQL

## Açıklama

Proje bir kullanıcı detay izleme platfromunun backend çalışmasıdır. 

## Kurulum

Öncelikle gereksinimlerin yüklü olduğundan emin olun. Python, Django, rest_framework yüklememiz gerek. Proje Visual Studio Code IDE kullanılmıştır.

pip install django
pip install djangorestframework

## Uygulama

Uygulamanın içerdiği myapp uygulaması oluşturulur.
-python manage.py startapp myapp
myapp uygulamasını settings.py eklenir.

```
INSTALLED_APPS = [
    'myapp',
    'rest_framework',
]
```

ModelViewSet modeli kullanılmıştır.

```
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
```

Database olarak PostgreSQL kullanılmıştır. settings.py database kısmı buna göre düzenlenir.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name', 
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': host, 
        'PORT': port,
    }
}
```

models.py, serializers.py, urls.py, views.py dosyaları düzenlenir oluşturulur.
Proje Migration dosyası oluşturulur ve proje çalıştırılır.
```
python manage.py makemigrations
python manage.py migrate
pyhon manage.py runserver
```

<img src="https://1drv.ms/i/s!AnmeK5nvjEYzlB0HdA-lj37djKxo?e=z7fl1C" alt="fotos" width="320" height="180">

