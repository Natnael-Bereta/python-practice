fav_language = {'Nati': 'python',
                'Beki': '',
                'Lemi': 'Java',
                'Kiya': 'python',
                'Sifen': 'C++',
                'Umeran': ''}
for name, lang in fav_language.items():
    if lang == '':
        print(f'{name}, you should take the poll.')
    else:
        print(f'{name}, thank you for taking the poll!')