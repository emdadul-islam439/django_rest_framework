from rest_framework import serializers
from ..models import Movie

#validators
def name_validator(value):
    if len(value) < 4:
        raise serializers.ValidationError("Name is too short")
    return value

class MovieSerializer(serializers.ModelSerializer):
    #custom serializer methods (like @property of Model)
    name_length = serializers.SerializerMethodField()
    description_length = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = '__all__' 
        #fields = ['name', 'description']
        #exclude = ['active']
    
    #custom serializers getter method    
    def get_name_length(self, object):
        return len(object.name)
    
    #custom serializers getter method 
    def get_description_length(self, object):
        return len(object.description)
    
    # field validation
    def validate_description(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Description is too short")
        return value
    
    # object validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description should be different")
        return data



# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_validator])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # field validation
#     def validate_description(self, value):
#         if len(value) < 5:
#             raise serializers.ValidationError("Description is too short")
#         return value
    
#     # object validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and description should be different")
#         return data