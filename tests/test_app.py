import pytest
from app import app
import flask

app = Flask(__name__)
app.config['DEBUG'] = True
web = app.test_client()

def test_index():
    rv = web.get('/' , follow_redirects=True)
    assert rv.status_code == 404
