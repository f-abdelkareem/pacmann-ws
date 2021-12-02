# app.py
from flask import Flask, escape, request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn='<SENTRY.IO_DSN>', integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route('/divide/<int:numerator>/by/<int:denominator>/')
def hello(numerator, denominator):
    answer = numerator / denominator
    return f'{numerator} can be divided by {denominator} {answer} times.'
