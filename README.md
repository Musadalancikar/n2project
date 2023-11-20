# Django Apı

## Gereksinimler

-Python 3.8+, Django 4.2, PostgreSQL

## Açıklama

Proje bir kullanıcı detay izleme platfromunun backend çalışmasıdır. 

## Kurulum

Öncelikle gereksinimlerin yüklü olduğundan emin olun. Python, Django, rest_framework yüklememiz gerek. Proje Visual Studio Code IDE kullanılmıştır.
```
pip install django
pip install djangorestframework
```

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

![fotos](https://github.com/Musadalancikar/n2project/assets/91824791/882f0675-a9e6-4806-9e26-bd0f5a8ad95e)
![fotos1](https://github.com/Musadalancikar/n2project/assets/91824791/eebc804c-3fcd-4e0b-8437-338313443aa6)
![fotos2](https://github.com/Musadalancikar/n2project/assets/91824791/b33e42ec-f980-407e-9ebd-5690901b275f)
![fotos3](https://github.com/Musadalancikar/n2project/assets/91824791/96abd91f-2304-4103-ad1a-ac898be53a88)



