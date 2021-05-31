from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = __import__('instant').__version__

setup(
    name='django-instant',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Websockets for Django with Centrifugo ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-instant',
    download_url='https://github.com/synw/django-instant/releases/tag/' + version,
    keywords=['django', 'websockets', 'centrifugo'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'cent',
        'PyJWT'
    ],
    zip_safe=False
)
