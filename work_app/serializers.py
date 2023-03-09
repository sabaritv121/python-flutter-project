from rest_framework import serializers

from work_app.models import Workrequest, Login, Review, Youtube_link


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Login
        fields=['id','workshop_name','address','location','phone_number']





class WrequestSerializer(serializers.ModelSerializer):
    # workshop = serializers.ReadOnlyField(source= 'workshop.workshop_name')
    class Meta:
        model=Workrequest
        fields=['id','customer','workshop','name','location','date','time','status','phone_number','problem','vehicle_model']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields=["id","user","feeedback","date"]


class YoutubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Youtube_link
        fields = ["user","link","description"]