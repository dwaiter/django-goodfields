from django import template
from django.conf import settings
from django.template.loader import render_to_string

validate = (hasattr(settings, 'GOODFIELDS_VALIDATE') and settings.GOODFIELDS_VALIDATE)
register = template.Library()

class GoodfieldNode(template.Node):
    def __init__(self, field, field_type, label=None, cls='', validation=None):
        self.field = template.Variable(field)
        self.field_type = field_type.strip('\'"')
        self.label = label.strip('\'"') if label else None
        self.cls = cls.strip('\'"')
        self.validation = validation
    
    def render(self, context):
        field = self.field.resolve(context)
        f = field.form
        initial = field.data if f.data else f.initial.get(field.name, '')
        label = self.label or field.label
        
        template = "goodfields/fields/%s.html" % self.field_type
        
        return render_to_string(template, {
            'field': field,
            'initial': initial,
            'label': label,
            'class': self.cls,
            'validation': self.validation,
            'validate': validate,
        })
    


@register.tag
def goodfield(parser, token):
    """Render good form fields."""
    
    bits = token.split_contents()
    tag_name = bits.pop(0)
    
    if len(bits) < 2:
        raise template.TemplateSyntaxError(
            u"'%s' tag requires at least a field and field type." % tag_name
        )
    
    field = bits.pop(0)
    field_type = bits.pop(0)
    
    bits, kwargs = iter(bits), { 'validation': {} }
    
    for bit in bits:
        if bit == 'label':
            kwargs['label'] = bits.next()
        if bit == 'class':
            kwargs['cls'] = bits.next()
        if bit == 'email':
            kwargs['validation']['email'] = True
        if bit == 'pattern':
            kwargs['validation']['pattern'] = {
                're': bits.next().strip('"'),
                'message': bits.next().strip('"'),
            }
    
    return GoodfieldNode(field, field_type, **kwargs)

