import re
def is_valid_email(addr:str)->bool:
    if re.match(r'^[a-zA-Z0-9.]+@[a-zA-Z0-9\-]+.[a-zA-Z0-9]+$', addr):
        return True
    else:
        return False

def name_of_email(addr:str)->str:
    if re.match(r'<?(\w+\s?\w+)>?\s?(\w)*@(\w+\.\w+)', addr):
        return re.match(r'<?(\w+\s?\w+)>?\s?(\w)*@(\w+\.\w+)', addr).group(1)

assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft-163.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')