from flask import Flask, render_template, jsonify
from forms import FeedbackForm

app = Flask(__name__)
@app.route('/form', methods=['GET', 'POST'])

def form():
    form = FeedbackForm()
    if form.validate_on_submit():
        with open('FeedbackForm.txt', 'a') as f:
            f.write(f'First Name: {form.first_name.data}\n')
            f.write(f'Last Name: {form.last_name.data}\n')
            f.write(f'Email: {form.email.data}\n')
            f.write(f'Phone: {form.phone.data}\n')
            f.write(f'Experience: {form.experience.data}\n')
            f.write('Improvement: ' + ', '.join(form.improvement.data) + '\n')
            f.write(f'Additional Feedback: {form.additional_feedback.data}\n')
            f.write('------\n')
        return jsonify(success=True)
    return render_template('form-page.html', form=form)

@app.route('/')
def home():
    return render_template('welc-page.html')

@app.route('/about')
def about():
    return render_template('explain-page.html')

if __name__ == '__main__':
    app.run(debug=True)