import pytest
from app import app
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
web = app.test_client()

def test_index():
    rv = web.get('/' , follow_redirects=True)
    assert rv.status_code == 404
