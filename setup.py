# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

version = '0.1.dev0'

long_description = (open('README.md').read())

setup(name='affinitic.zmq',
      version=version,
      description="send sms",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Framework :: Buildout",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Topic :: Software Development :: Code Generators",
      ],
      keywords='sms affinitic',
      author='Affinitic',
      author_email='info@affinitic.be',
      url='https://github.com/affinitic/affinitic.zmq',
      license='GPL',
      packages=find_packages(),
      namespace_packages=['affinitic'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      'pyzmq',
      ],
      extras_require=dict(),
      entry_points="""
      [console_scripts]
      zmq_server = affinitic.smsutils.zmq_server:main
      zmq_client = affinitic.smsutils.zmq_client:main
      """,

      )