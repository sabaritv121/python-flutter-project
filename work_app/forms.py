from django.contrib.auth.forms import UserCreationForm

from work_app.models import Login


class Userregister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Login
        fields = ('username','password1','password2','user_name','address','phone_number')


class MechanicRegister(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Login
        fields = ('id','username','password1','password2','workshop_name','address','phone_number','location','min_wage')