from django.http import HttpResponse
from django.shortcuts import render

html_content = """
<html>
    <title>To-Do lists</title>
    <h1>To-Do list</h1>
    <input id="new_todo" placeholder="Enter a to-do item"></input>
</html>
"""

def home_page(request):
    return HttpResponse(html_content)