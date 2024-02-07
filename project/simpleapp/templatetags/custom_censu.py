from django import template

register = template.Library()

censura = ['видео', 'картинке', 'навстречу', 'цифровых']

@register.filter()
def censor(value):
    some_string = ''
    for cens in value.split():
        if cens in censura:
            some_string += cens[0] + '*' * (len(cens) -1) + " "
        else:
            some_string += cens + ' '

    return some_string.strip()
