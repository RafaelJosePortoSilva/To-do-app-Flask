from setuptools import setup, find_packages

requires = [
        'flask',
        'flask-sqlalchemy',
        'psycopg2'
        ]

setup(
        name='flask_todo',
        version='0.0',
        description='A todo list',
        author='Rafael',
        author_email='rafaelporto.dev@gmail.com',
        keywords='web flask',
        packages=find_packages(),
        include_package_data=True,
        install_requires=requires
        )
