from rest_framework import serializers

from ..models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # exclude = ['watchlist']
        fields = '__all__'
        read_only_fields = ['watchlist']


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__' 
    
    
class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        

# class StreamPlatformSerializer(serializers.ModelSerializer):
#     # watchlist = WatchListSerializer(many=True, read_only=True) # shwoing the whole model of the related_name="watchlist" attribute
#     # watchlist = serializers.StringRelatedField(many=True, read_only=True) # showing only the __str__ attribute of the related_name="watchlist" attribute
#     # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # showing only the 'pk' of the related_name="watchlist" attribute
#     watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="movie-details")
    
#     class Meta:
#         model = StreamPlatform
#         fields = '__all__'
        

# #validators
# def name_validator(value):
#     if len(value) < 4:
#         raise serializers.ValidationError("Title is too short")
#     return value

# class WatchSerializer(serializers.ModelSerializer):
#     #custom serializer methods (like @property of Model)
#     title_length = serializers.SerializerMethodField()
#     storyline_length = serializers.SerializerMethodField()
    
#     class Meta:
#         model = WatchList
#         fields = '__all__' 
#         #fields = ['title', 'storyline']
#         #exclude = ['active']
    
#     #custom serializers getter method    
#     def get_title_length(self, object):
#         return len(object.title)
    
#     #custom serializers getter method 
#     def get_storyline_length(self, object):
#         return len(object.storyline)
    
#     # field validation
#     def validate_storyline(self, value):
#         if len(value) < 5:
#             raise serializers.ValidationError("storyline is too short")
#         return value
    
#     # object validation
#     def validate(self, data):
#         if data['title'] == data['storyline']:
#             raise serializers.ValidationError("Title and storyline should be different")
#         return data



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