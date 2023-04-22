#Python Script to handle logging in and creating accounts.

import pandas as pd
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def confirmSetup():
    pass