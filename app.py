import os
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
import OpenTokSDK

api_key = "1273231"        # Replace with your OpenTok API key.
api_secret = "48ed3665260f1eef16355e6754868ecb6cc90791"  # Replace with your OpenTok API secret.

opentok_sdk = OpenTokSDK.OpenTokSDK(api_key, api_secret)

session = opentok_sdk.create_session(None)

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello TokBox!'

@app.route('/hackru')
def hackru():
    return 'Hello HackRU!'

@app.route('/list')
def list():
  return render_template('list.html', navigation=[dict(href="http://google.com", caption="Google"), dict(href="http://yahoo.com", caption="Yahoo")], a_variable='hello' )

@app.route('/opentok')
def test():
  token = opentok_sdk.generate_token(session.session_id)
 # token2 = opentok_sdk.generate_token(session.session_id)
  return render_template('opentok.html', s=session.session_id, t=token)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='0.0.0.0', port=port)
