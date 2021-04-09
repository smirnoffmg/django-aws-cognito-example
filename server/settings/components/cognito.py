from server.settings.components import config

COGNITO_USER_POOL_ID = config("COGNITO_USER_POOL_ID")
COGNITO_APP_ID = config("COGNITO_APP_ID")
COGNITO_APP_SECRET = config("COGNITO_APP_SECRET")
COGNITO_DOMAIN = config("COGNITO_DOMAIN")

AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = config("AWS_DEFAULT_REGION")

COGNITO_CREATE_UNKNOWN_USERS = True

# that's from django-allauth settings
SITE_ID = 1

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = "email"

SOCIALACCOUNT_STORE_TOKENS = True

SOCIALACCOUNT_PROVIDERS = {
    "amazon_cognito": {
        "DOMAIN": f"https://{COGNITO_DOMAIN}.auth.{AWS_DEFAULT_REGION}.amazoncognito.com",
        "APP": {
            "client_id": COGNITO_APP_ID,
            "secret": COGNITO_APP_SECRET,
        },
        "SCOPE": ["email", "profile", "openid"],
    }
}
