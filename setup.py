from setuptools import setup

setup(
    name='mstat',
    version='0.1',
    packages=['mstat', 'mstat.fstat'],
    url='',
    license='MIT',
    author='ds',
    author_email='diman.no2@gmail.com',
    description='REST API',
    install_requires=[
        'numpy'
    ],
    entry_points={
        'console_scripts': ['rest-server=mstat.server:__main__']
    }
)
