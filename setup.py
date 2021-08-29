from setuptools import setup, find_packages

setup(
    name='vesla_pymvc',
    description='Some MVC utils for python projects',
    version='1.1.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    packages=find_packages(),
    install_requires=[
        'Cerberus',
    ],
    url='https://github.com/filipealvesdef/vesla-pymvc',
    zip_safe=False,
)
