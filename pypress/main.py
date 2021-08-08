from flask import Flask, render_template, request, url_for
import admin, auth

app = Flask(__name__)
app.register_blueprint(admin.admin_page)
app.register_blueprint(auth.auth_page)


@app.route('/')
def index():
    x = url_for('admin.admin')
    return f'Hello, World! {x}'



app.run('0.0.0.0', 8000, debug=True)