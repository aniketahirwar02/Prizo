from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about_page')
def about_page():
    return render_template('about_page.html')

@app.route('/contact_page')
def contact_page():
    return render_template('contact_page.html')

@app.route('/comparsion_page')
def comparsion_page():
    return render_template('comparsion_page.html')

@app.route('/result_page')
def result_page():
    return render_template('result_page.html')

if __name__ == '__main__':
    app.run(debug=True)