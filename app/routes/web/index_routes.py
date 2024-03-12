"""Index routes."""
from flask import Blueprint, render_template

index = Blueprint('index', __name__, template_folder='templates')

@index.route('/')
def home():
    """Render website's home page."""
    return render_template('index.html')
