from setuptools import setup, find_packages

try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = 'A Python package for formatting and printing lists'

setup(
    name='setprint',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pynput'
    ],
    author='mtur',  
    author_email='2007helloworld@gmail.com',
    description='A Python package for organizing and visualizing list hierarchies.',
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
    keywords=[
        "list",                 # リスト
        "nested list",          # ネストされたリスト（入れ子構造のリスト）
        "hierarchy",            # 階層構造
        "tree structure",       # ツリー構造
        "data visualization",   # データの可視化
        "data organization",    # データの整理
        "Python utilities",     # Pythonのユーティリティ
        "list visualization",   # リストの可視化
        "nested data",          # 入れ子データ
        "structured data"       # 構造化データ
    ],
    include_package_data=True,
    zip_safe=False,
)
