import pyparsing

name = Word(alphanums+"_:-")
view = Word(alphanums + "._()")
url_pattern = Word(alphas+"/$.*?^<>()_%+")
key = Word( alphanums + "._")
value = Word( alphanums + "._")
key_value = key + ":" + value
url = name + "=>" + Optional(http_method) + url_pattern + view + Optional(key_value)

class Parser(object):

    def to_urls(file_name):
        """
        Reads a router.config file, parses it and return a list of django url that can be used to concatenate
        to urlpatterns in urls.py.
        """
        pass
