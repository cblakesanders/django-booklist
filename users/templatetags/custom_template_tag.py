from django import template
from users.models import Profile, Relationship
from django.utils.html import format_html
from django.contrib.auth.models import User


register = template.Library()

''' 
Pass in Profile object, returns the set of books that belongs to the user
Allows the template to loop through the books. 

Need to change to allow views from accounts that aren't authenticated
'''
@register.simple_tag
def get_books(Profile):
    books = Profile.books.all()
    print(type(books))
    return books

'''
Get how many followers a profile has by counting the total times the username 
appears in the database
'''