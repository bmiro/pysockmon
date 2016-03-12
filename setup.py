# -*- coding: utf-8 -*-

from setuptools import setup                                                                         
 
INSTALL_REQUIRES = [
    'click'
]
 
setup(
    name='pysockmon',
    version='0.0.1',
    packages=['pysockmon'],
    include_package_data=True,
    url=u"",
    license='GPLv3',
    install_requires=INSTALL_REQUIRES,
    entry_points="""
        [console_scripts]
        pysockmon=pysockmon.pysockmon:pysockmon
    """,
    author=u"Bartomeu Miro Mateu",
    author_email=u"pysockmon at rtom dot eu",
    description=u"Kind of socket response size monitor"
)

