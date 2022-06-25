data = input().split(' : ')
print('Short:', '; '.join(sorted(list(map( str.lower, filter(lambda x : len(x) < 4, data))))))
print('Long:', '; '.join(sorted(list(filter(lambda x : len(x) > 7, data)), reverse = True)))
print('With letter:', '; '.join(list(map(str.capitalize, filter(lambda x : 'w' in x.lower(), data)))))