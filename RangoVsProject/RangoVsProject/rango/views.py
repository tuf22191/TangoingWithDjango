# Create your views here.
from django.http import HttpResponse
import django
from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})




def add_page(request, category_name_slug):
    categor = 9
    print "this is working"
    try:
        categor = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        categor = None
            
    if request.method =='POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if categor:
                page =form.save(commit=False)
                page.category= categor
                page.views=0
                page.save()
                #return index(request)
                return category(request, category_name_slug)
        else:
                print form.errors
    else:
        form=PageForm()
    context_dictionary ={}
    context_dictionary['category_slug']= category_name_slug
    context_dictionary['form'] = form
    return render(request, 'rango/add_page.html', context_dictionary) 

def category(request, category_name_slug):

    context_dict={}
    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages=Page.objects.filter(category=category)
        context_dict['pages']= pages
        context_dict['category']=category
        context_dict['category_slug'] = category_name_slug
    except Category.DoesNotExist:
        pass
        
    return render(request, 'rango/category.html', context_dict) 



#def index(request):
#    #s=django.get_version()
#    #dictionary
#    context_dict={'boldmessage': "I am bold font from the context"}
#    return render(request, 'rango/index.html', context_dict)
##HttpResponse("Yo what is up!? " + s + "  <a href=\"about\">Link </a>")
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary which will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    try:
        
        page_list=Page.objects.order_by('-views')[:5]
        context_dict['topPages']=page_list

    except Category.DoesNotExist:
        pass
    
    # Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


def anotherFunc(response):
    return HttpResponse("Another page!")

def getAboutPage(request):
    dictionary = {'something': "something"}
    return HttpResponse(render(request, 'rango/about.html', dictionary))

    
    #return HttpResponse("<img src=\"/staticmedia/images/writers-desk-with-cappuccino.jpg\" alt=\"Picture of notebook and other things\"/> The getAboutPage was called.  <a href=\" /rango/ \">BackToIndex </a>")



####ALL URLS use the urls.py functionality