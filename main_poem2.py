from flask import Flask,request,render_template,session,redirect,url_for,flash #,abort,send_from_directory
import json


app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def main():
    print('Start main !', request.remote_addr)
    return render_template('main_poem2.html')

@app.route('/AJAX_GET_Result', methods = ['GET', 'POST'])
def AJAX_GET_Result():
    print('Start AJAX_GET_Result !')
    # yloption = request.args.get('yloption') #, type=None) # HTTP GET 방식
    yloption = request.form.get('yloption',  type=str)     # HTTP POST 방식
    print('AJAX_GET_Result yloption :', request.remote_addr, type(yloption), yloption)
    for x in json.loads(yloption):
        print(x, x[-1])
    yloption2 = [x[-1] for x in json.loads(yloption)]
    print(yloption2, max(yloption2))

    return json.dumps(yloption2) # String(json)으로 변환해서 전송

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)