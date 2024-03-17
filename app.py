from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone_num=request.form.get("phone")
    email = request.form.get('email')
    job_role=request.form.get("job")
    uploaded_file = request.files['file']
    # Process and store the data/file as needed

    uploaded_file.save("./{}".format(uploaded_file.filename))
    return render_template('submit.html')


if __name__ == '__main__':
    app.run(debug=True)
    
