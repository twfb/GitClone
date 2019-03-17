from setuptools import setup, find_packages

setup(
    name='git-clone',
    version='1.0.5',
    description=('Git clone by downloading zip and decompressing it'),
    long_description=open('README.rst').read(),
    author='twfb',
    author_email='twfb@hotmail.com',
    maintainer='twfb',
    maintainer_email='twfb@hotmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    include_package_data=True,
    url='https://github.com/dhgdhg/git-clone/',
    classifiers=[
        'Development Status :: 4 - Beta', 'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    entry_points={
        'console_scripts': ['git-clone=git_clone.git_clone:execute'],
    })
