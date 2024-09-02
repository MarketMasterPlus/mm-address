# mm-address/app/utils.py
import re

def validate_cep(cep):
    """ Validate Brazilian CEP format (XXXXX-XXX) """
    pattern = re.compile(r'^\d{5}-\d{3}$')
    return pattern.match(cep) is not None
