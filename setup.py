try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

 config = {
    'description': 'onchainjobs.io',
    'author': 'Tim Siwula',
    'url': 'https://onchainjobs.io',
    'download_url': 'Where to download it.',
    'author_email': 'github@timsiwula.com',
    'version': '0.0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'onchainjobs'
}

setup(**config)
