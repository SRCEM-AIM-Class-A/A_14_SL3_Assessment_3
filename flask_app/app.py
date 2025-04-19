from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'password-3000'  # Use a secure key for production

@app.route('/')
def index():
    return redirect(url_for('greet'))

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        color = request.form.get('color')
        language = request.form.get('language')

        # Basic validation
        if not all([name, age, email, color, language]):
            flash("Please fill in all fields.")
            return redirect(url_for('greet'))

        try:
            age = int(age)
        except ValueError:
            flash("Age must be a valid number.")
            return redirect(url_for('greet'))

        return render_template(
            'greeting.html',
            name=name,
            age=age,
            email=email,
            color=color,
            language=language
        )

    return render_template('greet.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
