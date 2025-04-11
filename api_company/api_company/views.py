from django.http import HttpResponse

def home_page(request):
    print("home page requested")
    people = [
        'Vishal',
        'Shivani'
    ]
    return HttpResponse("<h1>This is home page</h1>")