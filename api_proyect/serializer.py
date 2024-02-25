from rest_framework import serializers 
from .models import Programmer  
 
# Archive for convert the Models the Python to list of JSON 
 
class ProgrammerSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Programmer 
        fields = '__all__'