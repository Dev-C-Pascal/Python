def task(stri):
    tmp=stri.split('а')
    if tmp[-1]=='':
        return list(map(lambda x : x+'а5',tmp))
    else:
        return list(map(lambda x : x+'а5',tmp[0:-1]))+[tmp[-1]]
    
print(task('строка символов будет преобразована в набор строк'))