def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"

    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"

    return wrapper


@make_bold
@make_emphasis
@make_underlined
def hello():
    return "hello world"


print(hello())  # returns "<b><em><u>hello world</u></em></b>"
