from pyparsing import Word, alphanums, alphas, Optional, Literal
from django.conf import settings
from django.conf.urls import patterns, url

name = Word(alphanums+"_:-")
view = Word(alphanums + "._()")
url_pattern = Word(alphanums+"/$.*?^<>()_%+")
key = Word( alphanums + "._")
value = Word( alphanums + "._")
key_value = key + ":" + value
http_method = Literal("GET") ^ Literal("POST")
url_grammar = name('name') + "=>" + Optional(http_method('http_method')) + url_pattern('pattern') + view('view') + Optional(key_value('key_value'))

class Parser(object):

    @staticmethod
    def to_urls(file_name=None):
        """
        Reads a router.config file, parses it and return a list of django url that can be used to concatenate
        to urlpatterns in urls.py.
        """
        urlpatterns = patterns('')

        with open(settings.ROUTER_CONFIG_FILE if not file_name else file_name) as f:
            lines = f.readlines()
            for line in lines:
                if line and not line.startswith('#'):
                    values = url_grammar.parseString(line)
                    name = values.get('name')
                    pattern = values.get('pattern')
                    view = values.get('view')
                    key_value = values.get('key_value')
                    if view and pattern:
                        if key_value:
                            urlpatterns += patterns('', url(pattern, view,{key_value[0]:key_value[2]}, name=name))
                        else:
                            urlpatterns += patterns('', url(pattern, view, name=name))

                    else:
                        raise ValueError('A url should have at least a view and a pattern')
        return urlpatterns
