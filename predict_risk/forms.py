from django import forms
from predict_risk.models import Predictions
from django.core.validators import MaxValueValidator,MinValueValidator
class Predict_Form(forms.ModelForm):
    
    # age=forms.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(3)])
    class Meta:
        model = Predictions
        fields = ('age','sex','cp','resting_bp','serum_cholesterol','fasting_blood_sugar','resting_ecg','max_heart_rate',
        'exercise_induced_angina','st_depression','st_slope','number_of_vessels','thallium_scan_results')
        widgets = {'age': forms.NumberInput(attrs={'class': 'form-control','id': 'age','oninput': 'limit_input()'}),
                   'sex': forms.Select(attrs={'class': 'form-control'}),
                   'cp': forms.Select(attrs={'class': 'form-control'}),
                   'resting_bp':forms.NumberInput(attrs={'class': 'form-control','id': 'resting_bp','oninput': 'limitinput()'}),
                   'serum_cholesterol':forms.NumberInput(attrs={'class': 'form-control','id': 'serum_cholesterol','oninput': 'liinput()'}),
                   'fasting_blood_sugar':forms.Select(attrs={'class': 'form-control'}),
                   'resting_ecg':forms.Select(attrs={'class': 'form-control'}),
                   'max_heart_rate':forms.NumberInput(attrs={'class': 'form-control','id': 'max_heart_rate','oninput': 'limiinput()'}),
                   'exercise_induced_angina':forms.Select(attrs={'class': 'form-control'}),
                   'st_depression':forms.NumberInput(attrs={'class': 'form-control','id': 'st_depression','oninput': 'liminput()'}),
                   'st_slope':forms.Select(attrs={'class': 'form-control'}),
                   'number_of_vessels':forms.Select(attrs={'class': 'form-control'}),
                   'thallium_scan_results':forms.Select(attrs={'class': 'form-control'}),
                   }