
from flask import Flask
import sentry_sdk
# sentry_sdk.init("https://b1f9d8cecd2e460a98c23f835cb0ba37@sentry.io/1729069")
# division_by_zero = 1 / 0
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://b1f9d8cecd2e460a98c23f835cb0ba37@sentry.io/1729069",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

if __name__ == "__main__":
    app.run()

