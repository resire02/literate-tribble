from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/<string:weblink>')
def move(weblink=None):
    title = weblink.replace('.html','')
    title = title[0].upper() + title[1:].lower()
    return render_template(weblink, title=title)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # write_to_file(data)
            return redirect('thankyou.html')
        except Exception:
            return '500 Internal Server Error'
    else:
        return 'nooo'
    

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as csvdata:
        ema, sub, msg= data['email'], data['subject'], data['message']
        csvwriter = csv.writer(csvdata, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow([ema, sub, msg])
    return


def write_to_file(data:dict):
    with open('database.txt', mode='a') as database:
        ema, sub, msg= data['email'], data['subject'], data['message']
        database.write(f'[{ema}] [{sub}]: {msg}\n')
    return

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
