from flask import Flask, render_template, request
app = Flask(__name__)

from FutureContract import FutureContract
from un1 import DBSession


@app.route('/', methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        variety = request.form['variety']
        return render_template('contract.html', contracts = DBSession().query(FutureContract).filter(FutureContract.交易品种 == variety).first().to_dict())

    return render_template('contract.html', contracts = DBSession().query(FutureContract).first().to_dict())

if __name__ == '__main__':
    app.run(host='0.0.0.0')