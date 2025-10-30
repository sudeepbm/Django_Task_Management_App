from django import forms


class SupportForm(forms.Form):
	"""Simple contact form for gathering support requests."""

	name = forms.CharField(
		label="Full name",
		max_length=100,
		widget=forms.TextInput(attrs={
			"placeholder": "Your name"
		}),
	)
	email = forms.EmailField(
		label="Email address",
		widget=forms.EmailInput(attrs={
			"placeholder": "you@example.com"
		}),
	)
	subject = forms.CharField(
		label="Subject",
		max_length=150,
		widget=forms.TextInput(attrs={
			"placeholder": "How can we help?"
		}),
	)
	message = forms.CharField(
		label="Message",
		widget=forms.Textarea(attrs={
			"rows": 4,
			"placeholder": "Describe your issue or question"
		}),
		min_length=10,
	)

	def clean_message(self):
		"""Ensure the message includes meaningful content."""
		message = self.cleaned_data["message"].strip()
		if len(message.split()) < 3:
			raise forms.ValidationError("Please provide a bit more detail so we can assist you effectively.")
		return message
