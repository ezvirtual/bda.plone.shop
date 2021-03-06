import os
from setuptools import setup
from setuptools import find_packages


version = '0.5dev'
shortdesc = "Shop Solution for Plone"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'CHANGES.rst')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.rst')).read()


setup(
    name='bda.plone.shop',
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    author='BlueDynamics Alliance',
    author_email='dev@bluedynamics.com',
    license='GNU General Public Licence',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['bda', 'bda.plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Plone',
        'archetypes.schemaextender',
        'bda.plone.orders',
        'plone.api',
        'plone.app.registry',
        'plone.app.users',
        'collective.z3cform.datagridfield',
    ],
    extras_require={
        'test': [
            'Products.ATContentTypes',
            'plone.app.dexterity',
            'plone.app.testing [robot]',
            'plone.app.robotframework [debug]',
            'plone.app.contenttypes',
        ]
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
