from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
from .forms import ConfigForm


@login_required(login_url='login')
def ConfigPage(request):
    if request.method == 'POST':
        form = ConfigForm(request.POST)
        if form.is_valid():
            device1 = request.POST.get('Device_1')
            print(device1)
            device2 = request.POST.get('Device_2')

            token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1ODI3ODEzLCJqdGkiOiJmNTg1MDlmYTdlNWQ0ZDE0OTQxZDc4Mjk5MTg3ZjM1NyIsInVzZXJfaWQiOjl9.GD9J8j72Q9hdn9NqG2FWxyJF_6Rimd0LLisTxl2Fs9w"
            url = "http://127.0.0.1:8000/api/sampleAPI1/"

            response = requests.get(url, headers={'Authorization': 'Bearer {}'.format(token)}).json()
            print(response)


    # config_diff= {
    #     'Config Difference':response[device1]
    # }

    return render(request, 'config.html', {})
