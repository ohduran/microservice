"""Configuration file to enforce separation of concerns."""
import os


class Config():
    """Config class to encapsulate configuration settings."""

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'such-an-impenetrable-key'
