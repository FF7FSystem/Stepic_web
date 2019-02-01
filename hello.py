def wsgi_app(envir,start_response):
	print('Запустился wsgi_app')
	status = '200 Ok'
	headers = [('Content-Type', 'text/plant')]
	body = [ i for i in envir['wsgi.input']]
	#envir['QUERY_STRING']
	print('В боди нахдится --- ',body)
	start_response(status,headers)
	return body