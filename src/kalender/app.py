from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/', methods=['POST', 'GET'])
def avaleht():
    return render_template('avaleht.html')