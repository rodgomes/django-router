from django.conf.urls import patterns, url
from test_app.views import *
from router import Parser

urlpatterns = Parser.to_urls()
