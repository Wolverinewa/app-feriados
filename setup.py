from setuptools import setup

setup(
   name='app-feriados',
   version='1.0',
   description='Instruct test',
   author='Willian',
   author_email='wolverinewa@gmail.com',
   packages=['app-feriados'],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
)