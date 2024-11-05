from django import forms
from .models import TouristDestination

WEATHER_CHOICES = [
    ('sunny', 'Sunny'),
    ('cloudy', 'Cloudy'),
    ('rainy', 'Rainy'),
    ('snowy', 'Snowy'),
    ('windy', 'Windy'),
]

INDIAN_STATES = [
    ('andhra_pradesh', 'Andhra Pradesh'),
    ('arunachal_pradesh', 'Arunachal Pradesh'),
    ('assam', 'Assam'),
    ('bihar', 'Bihar'),
    ('chhattisgarh', 'Chhattisgarh'),
    ('goa', 'Goa'),
    ('gujarat', 'Gujarat'),
    ('haryana', 'Haryana'),
    ('himachal_pradesh', 'Himachal Pradesh'),
    ('jharkhand', 'Jharkhand'),
    ('karnataka', 'Karnataka'),
    ('kerala', 'Kerala'),
    ('madhya_pradesh', 'Madhya Pradesh'),
    ('maharashtra', 'Maharashtra'),
    ('manipur', 'Manipur'),
    ('meghalaya', 'Meghalaya'),
    ('mizoram', 'Mizoram'),
    ('nagaland', 'Nagaland'),
    ('odisha', 'Odisha'),
    ('punjab', 'Punjab'),
    ('rajasthan', 'Rajasthan'),
    ('sikkim', 'Sikkim'),
    ('tamil_nadu', 'Tamil Nadu'),
    ('telangana', 'Telangana'),
    ('tripura', 'Tripura'),
    ('uttar_pradesh', 'Uttar Pradesh'),
    ('uttarakhand', 'Uttarakhand'),
    ('west_bengal', 'West Bengal'),
]
class TouristDestinationForm(forms.ModelForm):
    weather = forms.ChoiceField(choices=WEATHER_CHOICES, required=False)
    location_state = forms.ChoiceField(choices=INDIAN_STATES, required=False)
    class Meta:
        model = TouristDestination
        fields = '__all__'
