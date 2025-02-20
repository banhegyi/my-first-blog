from django.shortcuts import render

# Create your views here.
# Attila szúrta be az alábbi függvényt 2025.02.11-én

def post_list(request):
    return render(request, 'blog/post_list.html', {})