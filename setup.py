from setuptools import setup

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
    'functools',
    ],
    zip_safe=False)
