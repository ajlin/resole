from setuptools import setup
params = dict(
    name= 'resole',
    version = '',
    packages = [''],
    url = '',
    license = '',
    author = 'Alex Lin',
    author_email = 'alex@thewanderapp.com',
    description = 'Resole Beta order form'
)


'''
# copy requirements.txt to setup params
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

params['install_requires'] = requirements
'''

setup(**params)