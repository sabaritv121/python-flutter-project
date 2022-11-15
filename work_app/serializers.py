from rest_framework import serializers

from work_app.models import Workrequest, Login


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=['id','workshop_name','address','location','phone_number']





class WrequestSerializer(serializers.ModelSerializer):
    # workshop = serializers.ReadOnlyField(source= 'workshop.workshop_name')
    class Meta:
        model=Workrequest
        fields=['id','customer','workshop','name','location','date','time','status','phone_number','problem','vehicle_model']


