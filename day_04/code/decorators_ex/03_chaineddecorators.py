
def italic(func):
    def wrapper(s):
        return "<i>" + func(s) + "</i>"
    return wrapper

def bold(func):
    def wrapper(s):
        return "<b>" + func(s) + "</b>"
    return wrapper

@bold
@italic
def message(s):
    return str(s)

print(message('Hello Oracle!'))
