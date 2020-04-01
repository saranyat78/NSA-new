from django import forms
from .models import ConfigDiff


class ConfigForm(forms.ModelForm):

    class Meta:
        model = ConfigDiff
        fields = ["Device_1", "Device_2"]

