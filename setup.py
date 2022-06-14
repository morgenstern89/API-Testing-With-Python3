from setuptools import setup, find_packages



setup(name='apidemotest',
      version='1.0',
      description="Practice API Testing",
      author="Sarah Yoon",
      author_email="sar.yoon89@gmail.com",
      url='https://supersqa.com',
      packages=find_packages(),
      zip_safe=False,
      intstall_requires=[
            "pytest",
            "pytest-html",
            "requests",
            "requests-oauthlib",
            "PyMySQL",
            "WooCommerce",
      ]
      )

