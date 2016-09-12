from setuptools import setup, find_packages


version = __import__('instant').__version__

setup(
    name = 'django-instant',
    packages=find_packages(),
    include_package_data=True,
    version = version,
    description = 'Websockets for Django with Centrifugo ',
    author = 'synw',
    author_email = 'synwe@yahoo.com',
    url = 'https://github.com/synw/django-instant', 
    download_url = 'https://github.com/synw/django-instant/releases/tag/'+version, 
    keywords = ['django', 'websockets', 'centrifugo'], 
    classifiers = [
          'Development Status :: 3 - Alpha',
          'Framework :: Django :: 1.9',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
      ],
    install_requires=[
        'cent',
    ],
    zip_safe=False
)
