from django import forms
from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
				"user_id",
				"gcm_id",
		]