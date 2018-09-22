from setuptools import setup, find_packages

version = __import__('instant').__version__

setup(
    name='django-instant',
    packages=find_packages(),
    include_package_data=True,
    version=version,
    description='Websockets for Django with Centrifugo ',
    author='synw',
    author_email='synwe@yahoo.com',
    url='https://github.com/synw/django-instant',
    download_url='https://github.com/synw/django-instant/releases/tag/' + version,
    keywords=['django', 'websockets', 'centrifugo'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'cent<3.0',
        'django-cors-headers',
    ],
    zip_safe=False
)
