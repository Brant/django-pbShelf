from setuptools import setup, find_packages

setup(
    name = "pbshelf",
    version = "0.1",
    url = 'https://github.com/Brant/django-pbShelf',
    license = 'GPL',
    description = "Adds pbShelf static files to a django project",
    long_description = open('README.md').read(),

    author = 'Brant Steen',
    author_email = 'brant.steen@gmail.com',

    packages = find_packages(exclude=('tests', )),
    include_package_data = True,
    zip_safe = False,

    install_requires = [],

#    scripts = ["scripts/project_dj", ],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
