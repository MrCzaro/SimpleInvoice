from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import CustomUser



class CustomAuthenticationForm(AuthenticationForm):
    class Meta: 
        model = CustomUser
        fields = ["email", "password"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Email address"
        self.fields["username"].widget.attrs.update({"class" : FORM_CLASS})
        self.fields["password"].label = "Password"
        self.fields["password"].widget.attrs.update({"class" : FORM_CLASS})
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "password1", "password2"]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Username"
        self.fields["username"].widget.attrs.update({"class" : FORM_CLASS})
        self.fields["email"].label = "Email address"
        self.fields["email"].widget.attrs.update({"class" : FORM_CLASS})
        self.fields["password1"].label = "Password"
        self.fields["password1"].widget.attrs.update({"class" : FORM_CLASS})
        self.fields["password2"].label = "Confirm password"
        self.fields["password2"].widget.attrs.update({"class" : FORM_CLASS})
