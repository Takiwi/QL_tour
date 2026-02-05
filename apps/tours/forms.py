from django import forms
from .models.tours import Tour

class TourAdminForm(forms.ModelForm):
    # Định nghĩa 2 ô nhập số thủ công
    lat_input = forms.FloatField(label="Latitude", required=False)
    lon_input = forms.FloatField(label="Longitude", required=False)

    class Meta:
        model = Tour
        fields = '__all__'