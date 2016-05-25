from setuptools import setup, find_packages

setup(
    name="Mountain King",
    version="0.0.7",
    packages=find_packages(),
    install_requires=['PyQt5>=5.6'],
    author="T-Dimov",
    description="Project for 'Programming with Python' course at FMI",
    license="GNU GPL v2",
    keywords="programming python course project",
    url="https://github.com/T-Dimov/Mountain-King",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: MacOS X',
        'Environment :: Other Environment',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Games/Entertainment :: Simulation'
    ]
)
