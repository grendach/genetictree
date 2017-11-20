from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Expense, Income, Category

def index(request):
    all_categories = Category.objects.all()
    return render(request, 'wallet/index.html', {'all_categories': all_categories})

'''
    #### Mixed Python and HTML togather, below is the batter way to create viwes functions

    html = ''
    for category in all_categories:
        url = '/wallet/' + str(category.id)+'/'
        html += '<a href ="' + url + '">' + str(category.category_name) + '</a><br>'
    return HttpResponse(html)
'''


def category_detail(request, category_id):

   #return HttpResponse("<h2> details of category id: " + str(category_id) + "</h2>")


    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404("Category doesn't exist")
    return render(request, 'wallet/category_detail.html', {'category': category})

