from setuptools import setup, find_packages

try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = 'A Python package for formatting and printing lists'

setup(
    name='setprint',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pynput'
    ],
    author='mtur',  
    author_email='2007helloworld@gmail.com',
    description='リストの中身を整列させる関数',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mtur2007/SetPrint',
    project_urls={
        'Bug Reports': 'https://github.com/mtur2007/SetPrint/issues',
        'Source': 'https://github.com/mtur2007/SetPrint',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords='list, formatting, printing, set',
    include_package_data=True,
    zip_safe=False,
)