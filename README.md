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

![fotos](https://github.com/Musadalancikar/n2project/assets/91824791/f487a369-abd2-4f15-871b-f3fd99251a57)
![fotos1](https://github.com/Musadalancikar/n2project/assets/91824791/3e149d52-f38f-4c40-9f15-1009f82b1116)
![fotos2](https://github.com/Musadalancikar/n2project/assets/91824791/9f929a67-5bc8-430c-9102-91c71cf8bc3f)
![fotos3](https://github.com/Musadalancikar/n2project/assets/91824791/1a0cc9bb-c276-43df-97de-f2e9fd3eb269)


