from setuptools import setup, find_packages

import russian_names as module


setup(
    name='russian-names',
    version=module.__version__,
    author=module.__author__,
    author_email='strmatvey@gmail.com',
    license='MIT',
    description='Russian names generator',
    long_description=open('./README.rst').read(),
    keywords='russian names generator',
    url='https://github.com/cybermatt/russian-names',
    packages=find_packages(exclude=['tests']),
    package_data={'russian_names': ['_data.zip']},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Text Processing',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Mocking',
        'Natural Language :: Russian',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
