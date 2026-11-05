import random


def generate_email():
    return f"user{random.randint(100000, 999999)}@example.com"


def generate_invalid_email():
    return f"user{random.randint(100000, 999999)}example.com"


def generate_password():
    return f"Pass{random.randint(100000, 999999)}"


def generate_ad_title():
    return f"Книга {random.randint(1000, 9999)}"
