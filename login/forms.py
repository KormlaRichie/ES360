from django import forms

# ----user login form-----

class Userform(forms.Form):
    username = forms.CharField(
        label='Username',
         max_length=100,
         widget=forms.TextInput(
             attrs={
                 "id": "username",
                 "class": "form-control",
             }
         )
         
         )


    password = forms.CharField(
        label='Password',
        required=True,
        max_length=100,
        widget=forms.TextInput(
                attrs={
                    "type":"password",
                    "id": "password",
                    "class": "form-control",
                }
            )

     )
    
