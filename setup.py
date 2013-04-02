from setuptools import setup, find_packages

version = '0.1'

setup(name='jap.skel',
      version=version,
      description="skeleton package",
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[],
      keywords="",
      author="",
      author_email="",
      url="",
      license="",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        ],
      entry_points={
            'console_scripts': [
            ],
      },
      extras_require={
          'test' : ["pytest",
                  "pytest-cov",
                  "pytest-capturelog",
       	         ],
      }
      )
