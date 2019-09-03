try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
  name = 'LootGameBotApi',         # How you named your package folder (MyLib)
  packages = ['C:\\Users\\uni\\Desktop\\ApiLoot'],   # Chose the same as "name"
  version = '0.14',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python wrapper per le API di LootBot',   # Give a short description about your library
  author = 'Alessio Balderi',                   # Type in your name
  author_email = 'balderialessio@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Anatras',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Anatras/LootBotApiPython/archive/0.13.tar.gz',    # I explain this later on
  keywords = ['LootBot', 'API', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)