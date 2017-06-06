from distutils.core import setup

setup(
    name='brutekrag',
    packages=['brutekrag'],
    version='0.3.0',
    description='Penetration tests on SSH servers using brute force or dictionary attacks',
    author='Jorge Matricali',
    author_email='jorgematricali@gmail.com',
    license='MIT',
    url='https://github.com/jorge-matricali/brutekrag',
    download_url='https://github.com/jorge-matricali/brutekrag/archive/v0.3.0.tar.gz',
    scripts=['bin/brutekrag'],
    keywords=['ssh', 'brute force', 'ethical hacking', 'pentesting', 'dictionary attack', 'penetration test'],
    classifiers=(
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ),
    install_requires=['paramiko>=1.8.0',
                      'argparse>=1.2.2']
)
