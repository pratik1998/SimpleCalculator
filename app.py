from flask import Flask, request

# create app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # show html form
        return '''
	    <html>
	    <head>
	    </head>
	    <body>
	    Enter your Expression:<br>
            <form method="post">
                <input type="text" name="expression" />
                <input type="submit" value="Calculate" />
            </form>
	    </body>
	    </html>
        '''
    elif request.method == 'POST':
        # calculate result
        expression = request.form.get('expression')
        result = eval(expression)
        return 'result: %s' % result

if __name__ == "__main__":
    # app.run(debug=True, threaded=True)
    app.run(threaded=True, host="0.0.0.0", port=5000)
