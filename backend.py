from bottle import route, run, request, hook, response
from calc_path import calc_path_2_ORCIDs as calc_path
import os, json

@hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'GET'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@route('/')
def form():
	return '''
	<html><body>
	<form action='/path' method='get'>
		<div>
			<input id='first' name='first' type='text' />
		</div>
		<div>
			<input id='second' name='second' type='text' />
		</div>
		<input value='Submit' type='submit' />
	</form>
	</body></html>'''

@route('/path')
def find_path():
	first = request.query['first']
	second = request.query['second']
	return json.dumps(calc_path(node1=first, node2=second))

# Boilerplate to start Bottle
port = int(os.environ.get('PORT', 5000))
run(host='0.0.0.0', port=port, server='paste')