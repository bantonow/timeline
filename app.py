from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# About route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Services route
@app.route('/services')
def services():
    return render_template('services.html')

# Drag-and-Drop route
@app.route('/drag-and-drop')
def drag_and_drop():
    return render_template('drag_and_drop.html')


if __name__ == '__main__':
    app.run(debug=True)