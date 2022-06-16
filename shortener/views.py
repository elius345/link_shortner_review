from django.shortcuts import render, get_object_or_404, redirect
from .models import LinkShortener

# Create your views here.
def home_view(request):
    if request.method =="POST" and 'long_url' in request.POST:
        url = request.POST.get('long_url')
        if LinkShortener.objects.filter( long_url = url).exists():
            link= LinkShortener.objects.get(long_url=url)
        else:
            link = LinkShortener(long_url=url)
            link.save()
        context = {'links':link}
        return render (request, 'index.html', context)


    template = 'index.html'
    context = {}
    return render (request, template, context)

def redirect_view(request, code):
    link = get_object_or_404(LinkShortener, code=code)
    return redirect(link.long_url)

