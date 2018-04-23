from setuptools import setup

setup(name='django_hockeydata_api',
      version='0.1',
      description='A Django package for simple use of Hockeydata Javascript API',
      url='https://git.wgdnet.de/cwiegand/django_hockeydata_api.git',
      author='Christian Wiegand',
      author_email='christianwgd@gmail.com',
      license='BSD',
      packages=['hockeydata_api'],
      install_requires=[
          "django >= 1.11",
      ],
      zip_safe=False)
