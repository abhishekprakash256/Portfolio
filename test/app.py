from flask import Flask, render_template

# Import Bootstrap extension
from flask_bootstrap import Bootstrap

app = Flask(__name__)
# Initialize Bootstrap
bootstrap = Bootstrap(app)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
