# NOTE: Set FLASK_SECRET_KEY, DEFAULT_USERNAME, DEFAULT_PASSWORD, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, and S3_BUCKET_NAME as environment variables before running this app.
from flask import Flask, request, render_template, flash, redirect, url_for, session
import boto3, os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

# Load AWS credentials
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'changeme')  # Use env var for secret key

# Default credentials
DEFAULT_USERNAME = os.getenv('DEFAULT_USERNAME', 'changeme')
DEFAULT_PASSWORD = os.getenv('DEFAULT_PASSWORD', 'changeme')

# AWS Configs
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION = os.getenv('AWS_REGION')
BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

# Boto3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION
)

@app.route('/', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == DEFAULT_USERNAME and password == DEFAULT_PASSWORD:
            session['user'] = username
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('upload.html', user=session['user'])

@app.route('/upload', methods=['POST'])
def upload():
    if 'user' not in session:
        return redirect(url_for('login'))
    if 'file' not in request.files:
        flash('No file part', 'danger')
        return redirect(url_for('dashboard'))
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'danger')
        return redirect(url_for('dashboard'))
    if file and file.filename.endswith('.csv'):
        filename = secure_filename(file.filename)
        try:
            s3.upload_fileobj(file, BUCKET_NAME, f"raw-zone/{filename}")
            flash(f"File '{filename}' uploaded to S3 successfully!", 'success')
        except Exception as e:
            flash(f"Upload failed: {str(e)}", 'danger')
        return redirect(url_for('dashboard'))
    else:
        flash('Only CSV files are allowed!', 'danger')
        return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) 