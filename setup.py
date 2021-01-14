from distutils.core import setup

setup(
    name='pymongo-cursor-json-encoder',
    packages=['pymongo-cursor-json-encoder'],
    version='0.1.0',
    license='MIT',
    description='Convert pymongo Cursor objects to JSON',
    author='Roger Vilà',
    author_email='rogervila@me.com',
    url='https://github.com/rogervila/pymongo-cursor-json-encoder',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz', # TODO
    keywords=['pymongo', 'cursor', 'json'],
    install_requires=[
        'isodate',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)