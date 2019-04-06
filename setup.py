from setuptools import setup

setup(name='django_hockeydata_api',
      version='0.0.2',
      description='A Django package for simple use of Hockeydata Javascript API',
      url='https://git.wgdnet.de/cwiegand/django_hockeydata_api.git',
      author='Christian Wiegand',
      author_email='christianwgd@gmail.com',
      license='BSD',
      long_description=open('README.rst').read(),
      packages=['hockeydata_api', ],
      include_package_data=True,
      install_requires=[
      ],
      zip_safe=False,
      classifiers=[
          "Development Status :: 3 - Alpha",
          'Framework :: Django',
          "License :: OSI Approved :: BSD License",
      ],)
