# context_processors.py
from .models import Category,Product



def menu_links(request):
    # Perform any necessary logic or data retrieval
    links=Category.objects.all()
    
    # Return a dictionary with the data to be included in the context
    return dict(links=links)
