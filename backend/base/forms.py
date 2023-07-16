from django.forms import ModelForm 
from .models import person, family, bcc_unit, user

class familyform(ModelForm):
    class Meta:
      model = family
      fields = '__all__'


class personform(ModelForm):
    class Meta:
      model = person
      fields = '__all__'

class bcc_unitform(ModelForm):
    class Meta:
      model = bcc_unit
      fields = '__all__'

class userform(ModelForm):
   class Meta:
      model = user
      fields = '__all__'
      