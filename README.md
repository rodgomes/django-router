# django-router
Simple DSL to write Django routes/urls in a simple/textual way.

The idea is to write urls in a config file like so:
```python
some_name =>  POST ^cool_url_name/(?P<nice_regex_param>.*?)/$  your_view_module.view_name
```

Of course, regular django does not support routing by HTTP method, this will onyl work if you use a django-simple-view.

The intention of this project is just to play a little with pyparsing and at the same time write some real stuff.
