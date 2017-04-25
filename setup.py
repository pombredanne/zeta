try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

# Dojo version 1.4.1
# Highchart version 1.2.5

# TODO : provide the license parameter to setup().
#   1. Requires freetype2

_entry_points = \
"""
[paste.app_factory]
main = zeta.config.middleware:make_app

[paste.app_install]
main = pylons.util:PylonsInstaller

[paste.filter_app_factory]
gzip = zeta.lib.gzipper:make_gzip_middleware
"""

classifiers = open('CLASSIFIERS.txt').readlines()
dependancies = [
    #"AuthKit==0.4.5",
    "Beaker==1.5.4",
    "bzr==2.2b3",
    "decorator==3.2.0",
    "FormEncode==1.2.2",
    "Mako==0.3.4",
    "mercurial==1.6.4",
    #"multigate==0.1",
    "MySQL_python==1.2.2",
    "nose==0.11.3",
    "Paste==1.7.5.1",
    "PasteDeploy==1.3.4",
    "PasteScript==1.7.3",
    "ply==3.3",
    "Pygments==1.3.1",
    "Pylons==0.10rc1",
    "python_openid==2.2.5",
    "pytz",
    "recaptcha_client==1.0.5",
    "Routes==1.12.3",
    "setuptools==0.6c9",
    "simplejson==2.1.1",
    "skimpyGimpy==1.4",
    "SQLAlchemy==0.6.1",
    "Tempita==0.4",
    "WebError==0.10.2",
    "WebHelpers==1.0rc1",
    "WebOb==1.0",
    "WebTest==1.2.1",
    #"zwiki-zeta==0.91",
]

setup(
    name= 'zeta',
    version= '0.71b1',
    packages= find_packages(exclude=['ez_setup', 'zeta.tests.*']),
    description= 'SCM and Project Collaboration Suite',
    long_description= open('DESCRIPTION.rst').read()

    author= 'R Pratap Chakravarthy',
    author_email= 'prataprc@discoverzeta.com',
    url= 'http://discoverzeta.com',

    install_requires=dependancies

    include_package_data= True,
    test_suite          = 'nose.collector',
    package_data        = { 'zeta.model.upgradescripts' : [ '*' ],
                            'zeta' : ['i18n/*/LC_MESSAGES/*.mo']
                          },
    zip_safe            = False,

    entry_points        = _entry_points,
)
