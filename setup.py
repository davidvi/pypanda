from setuptools import setup, find_packages

setup(name='pypanda',
    version='0.1',
    description='Passing attributes between networks for data assimilation to predict regulatory networks.',
    url='http://github.com/davidvi',
    author='David van IJzendoorn',
    author_email='d.g.p.van_ijzendoorn@lumc.nl',
    license='MIT',
    packages=['pypanda'],
    install_requires=['pandas',
    'numpy',
    'networkx',
    'matplotlib'
    ],
    scripts=['bin/pypanda'],
    zip_safe=False)
