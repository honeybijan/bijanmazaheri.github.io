# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template('homepage2.html')  # render a template

@app.route('/xcrank')
def xcranking():
    return render_template('xcrank.html')  # render a template

@app.route('/2019D1Men')
def xcd1men():
    return render_template('d1men2019.html')  # render a template

@app.route('/2019D1Women')
def xcd1women():
    return render_template('d1women2019.html')  # render a template

@app.route('/2019D3Men')
def xcd3men():
    return render_template('d3men2019.html')  # render a template

@app.route('/2019D3Women')
def xcd3women():
    return render_template('d3women2019.html')  # render a template

@app.route('/vfatregional')
def vfatregional():
    return render_template('vfatregional.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()