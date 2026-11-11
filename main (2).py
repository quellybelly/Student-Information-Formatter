fname_messy = input('Enter your first name: ') # input first name
lname_messy = input('Enter your lastname: ') # input last name

section_messy = input('Enter your section: ') # input section name
fsub = input('Enter your favorite subject: ') # input favorite subject

print('')
print('Formatted Output:')

fname_clean = fname_messy.title().strip()
lname_clean = lname_messy.title().strip()

print(f'Name: {fname_clean} {lname_clean}')

name_code = fname_clean.upper() + ' ' + lname_clean.upper()
print(f'Name Code: {name_code}')

section_clean = section_messy.upper().strip()
print(f'Section: {section_clean}')

fsub_clean = fsub.title().strip()
print(f'Favorite Subject: {fsub_clean}')

count = len(fname_clean + lname_clean)
print(f'Character Count: {count}')

