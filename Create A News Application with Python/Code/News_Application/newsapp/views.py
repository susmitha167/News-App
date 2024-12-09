from django.shortcuts import render
import requests
API_KEY = 'cfa2fb1ad96c4f7ea4414f19aaead9ea'

# Create your views here.

def home(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
  
    if country:
        if country == 'India' or country == 'india':
            country = 'in'
        elif country == 'USA' or country == 'usa' :
            country = 'us'
        else:
            country = 'in' and 'us'
        

   
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif category:
         url = f'https://newsapi.org/v2/top-headlines?category={category}&country=in&country=us&apiKey={API_KEY}'
         response = requests.get(url)
         data = response.json()
         articles = data['articles']
    else:
        url = f'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']

    context={'articles':articles}
    return render(request,'index.html',context)
