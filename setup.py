from setuptools import setup, find_packages
requirements = (
    [
        'requests',   # For making API calls
        'redis',      # For interacting with Redis
        'psycopg2-binary',   # For PostgreSQL connections
    ]
)

setup(
    name="utilities",
    author="Sandil Tandukar",
    author_email="tan.sandil44@gmail.com",
    version="0.0.1",
    install_requires=requirements,
    packages=find_packages(include=['utilities','utilities.*'])
)