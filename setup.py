from setuptools import setup

setup(name='southwest',
    version='0.2',
    description='Schedule southwest check in(s)',
    url='http://github.com/harshays/southwest',
    author='Harshay',
    author_email='harshay.rshah@gmail.com',
    license='MIT',
    packages=['southwest'],
    install_requires=['selenium'],
    entry_points = {
        'console_scripts': \
         ['southwest=southwest.console_scripts:southwest_help',
          'southwest.checkin=southwest.console_scripts:southwest_check_in',
          'southwest.checkins=southwest.console_scripts:southwest_check_ins']
    }
)

