from django import forms
class WeightForm(forms.Form):
    weight=forms.FloatField(label="Enter your weight")
    
class WeightEditForm(forms.Form):
    weight = forms.FloatField(label="Update weight")


class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
