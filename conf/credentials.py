import os


def get_env_credentials():

    wc_key = os.environ.get('WC_KEY')
    wc_secret = os.environ.get('WC_SECRET')

    #if not wc_key or not wc_secret:
     #   raise Exception("API Credentials are not added in ENV")
    #else:
    return {'wc_key': wc_key, 'wc_secret': wc_secret}