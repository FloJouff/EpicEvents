import sentry_sdk
from dotenv import load_dotenv
import os

load_dotenv()

SENTRY = os.getenv("SENTRY_KEY")


def init_sentry():
    sentry_sdk.init(
        dsn=SENTRY,
        traces_sample_rate=1.0,
        profiles_sample_rate=1.0,
    )
