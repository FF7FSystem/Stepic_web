def wsgi_app(envir,start_response):
    print('Запустился wsgi_app')
    status = '200 Ok'
    headers = [('Content-Type', 'text/plain')]
    body = [bytes(i + '\n', 'ascii') for i in envir['QUERY_STRING'].split('&')]
    print('В боди нахдится --- ',body)
    start_response(status,headers)
    return body