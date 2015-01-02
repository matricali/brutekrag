from distutils.core import setup

setup(
  name='brutekrag',
  packages=['brutekrag'],
  version='0.1.1',
  description='brute force OpenSSH using dictionary attack',
  author='Jorge Matricali',
  author_email='jorgematricali@gmail.com',
  license='MIT',
  url='https://github.com/jorge-matricali/brutekrag',
  download_url='https://github.com/jorge-matricali/brutekrag/archive/v0.1.1.tar.gz',
  scripts=['bin/brutekrag'],
  keywords=['ssh', 'brute force', 'ethical hacking', 'pentesting'],
  classifiers=[],
)
