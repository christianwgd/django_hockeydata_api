import json
from django.conf import settings
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def get_hd_attr(key, default=None):
    hd_settings = getattr(settings, 'HOCKEYDATA', {})
    return hd_settings.get(key, default)


@register.inclusion_tag('hockeydata_api/include/hockeydata_widget.html')
def hockeydata_widget(domNode, widgetName, divisionId=None, *args, **kwargs):
    options = kwargs
    options['domNode'] = domNode
    options['widgetName'] = widgetName
    if divisionId:
        options['divisionId'] = divisionId
    else:
        options['error'] = 'DivisionId not provided.'

    apiKey = get_hd_attr('API_KEY', '')
    sport = get_hd_attr('SPORT')
    if sport is None:
        options['error'] = 'HOCKEYDATA_SPORT not found in settings'
    else:
        options['apiKey'] = apiKey
        options['sport'] = sport

    return {'options': json.dumps(options)}


@register.simple_tag
def hockeydata_css(*args, **kwargs):
    url = get_hd_attr('STATIC', '')
    if url is None:
        return mark_safe('Error: No HOCKEYDATA_STATIC in settings provided!')
    default_css = get_hd_attr('DEFAULT_CSS', '')

    if default_css is not None:
        css_links = '<link href="{url}css/?{default}" rel="stylesheet">\n'.format(
            url=url, default=default_css)
    else:
        css_links = '<link href="{url}css/?los_template_default" rel="stylesheet">\n'.format(
            url=url)

    widgets = '?{widget}'.format(widget=args[0])
    for widget in args[1:]:
        widgets += '&{widget}'.format(widget=widget)
    css_links += '<link href="{url}css/{widgets}" rel="stylesheet" >'.format(
        url=url, widgets=widgets)
    return mark_safe(css_links)


@register.simple_tag
def hockeydata_js(*args, **kwargs):
    sport = get_hd_attr('SPORT')
    if sport is None:
        return mark_safe('Error: No HOCKEYDATA_SPORT in settings provided!')
    i18n = get_hd_attr('I18N')
    i18n_opt = ''
    if i18n is not None:
        i18n_opt = '&{i18n}'.format(i18n=i18n)

    url = get_hd_attr('STATIC')
    if url is None:
        return mark_safe('Error: No HOCKEYDATA_STATIC in settings provided!')

    widgets = '?{widget}'.format(widget=args[0])
    for widget in args[1:]:
        widgets += '&{widget}'.format(widget=widget)

    js_template = '<script src="{url}js/{widgets}&los_configuration_{sport}{i18n}"></script>'
    js = js_template.format(url=url, widgets=widgets,
                            sport=sport, i18n=i18n_opt)
    return mark_safe(js)
