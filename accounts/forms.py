from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Enter your name to proceed"}))

    def clean(self):
        name = self.cleaned_data.get('name', '')
        if not name:
            msg = forms.ValidationError("Name cannot be empty. Please enter your name to proceed")
            self.add_error("name", msg)
        return self.cleaned_data
