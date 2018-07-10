from django import forms

class SurveyForm(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=254)
    comment = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        comment = cleaned_data.get('comment')
        if not name and not comment:
            raise forms.ValidationError('Please input values into all fields')