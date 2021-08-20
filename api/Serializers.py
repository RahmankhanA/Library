from rest_framework import fields, serializers
from .models import AddVideo


class AddVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model= AddVideo
        fields=[
            'id',
            'libraryName',
            'video', 
            'coverPicture', 
           
            
            'title', 
            'description',
            'location', 
            'videoLanguage', 
            'addClass', 
            'subjectCategory'
        
        ]