# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='hypothesis-ros2',
      version='0.0.0',
      description='Data generators for Property Based Testing and Fuzzy Testing of ROS2 nodes.',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='http://github.com/ros-testing/hypothesis-ros2',
      author='Florian Kromer',
      author_email='florian.kromer@mailbox.org',
      python_requires='>=3.4.0',
      license='Apache License 2.0',
      packages=find_packages(),
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Security',
          'Topic :: Software Development',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Software Development :: Testing :: Acceptance',
        ],
)