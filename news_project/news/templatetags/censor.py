from django import template
import re

register = template.Library()

CENSOR_WORDS = ['редиска', 'плохое', 'ругательство']  # Замените на ваши слова

@register.filter(name='censor')
def censor(text):
    if not isinstance(text, str):
        raise ValueError("Censor filter can only be applied to strings.")
    
    def replace(match):
        word = match.group()
        return word[0] + '*' * (len(word) - 1)
    
    pattern = r'\b(' + '|'.join(re.escape(word.capitalize()) + '|' + re.escape(word.lower()) for word in CENSOR_WORDS) + r')\b'
    return re.sub(pattern, replace, text)
