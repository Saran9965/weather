from django.shortcuts import render
from .forms import cityForm
from.models import city
from django.contrib import messages
import requests

def home(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={},&appid=ad7412e3c2797739b8b341bec3ca997d&units=metric'
    if request.method=='POST':
        form=cityForm(request.POST)
        if form.is_valid():
                Ncity=form.cleaned_data['Name']   # get city name
                Ccity=city.objects.filter(Name=Ncity).count() #check already there or not
                if Ccity==0:
                    res=requests.get(url.format(Ncity)).json() # get weather report in api website
                    print(res)
                    if res['cod']==200:
                         form.save()
                         messages.success(request," "+Ncity+' Added successfull')
                    else:
                         messages.error(request,'City Does Not Exists...!!!')
                else:
                     messages.error(request,'City Already Exists...!!!')

    form=cityForm()
    return render(request,'weather.html',{'form':form})