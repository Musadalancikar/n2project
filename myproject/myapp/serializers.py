from rest_framework import serializers
from .models import Geo, Address, Company, Users, Posts, Comments, Albums, Photos, Todo

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ['lat', 'lng']

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer()

    class Meta:
        model = Address
        fields = ['street', 'suite', 'city', 'zipcode', 'geo']

    def create(self, validated_data):
        geo_data = validated_data.pop('geo')
        geo_instance = Geo.objects.create(**geo_data)
        address_instance = Address.objects.create(geo=geo_instance, **validated_data)
        return address_instance

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name']

class UsersSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = Users
        fields = ['id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company']

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        company_data = validated_data.pop('company')

        address_instance = AddressSerializer(data=address_data).create(validated_data=address_data)
        company_instance = CompanySerializer(data=company_data).create(validated_data=company_data)

        user_instance = Users.objects.create(address=address_instance, company=company_instance, **validated_data)
        return user_instance
    
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['user', 'id', 'title', 'body']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['post', 'id', 'name', 'email', 'body']

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = ['user', 'id', 'title']

class PhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photos
        fields = ['album', 'id', 'title', 'url', 'thumbnailUrl']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['user', 'id', 'title', 'completed']
