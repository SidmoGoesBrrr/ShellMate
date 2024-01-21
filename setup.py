from setuptools import setup, find_packages

setup(
    name='ShellMate',  
    version='1.0.2', 
    author='Siddhant', 
    author_email='siddhant@zodevelopers.com', 
    description='ShellMate: A GPT-Powered CLI Tool for Explaining and Finding Shell Commands', 
    long_description=open('readme.md').read(),  
    long_description_content_type='text/markdown',  
    url='https://github.com/SidmoGoesBrrr/ShellMate',  
    packages=find_packages(), 
    install_requires=[
        'openai',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'shellmate=shellmate_module.main:main', 
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)