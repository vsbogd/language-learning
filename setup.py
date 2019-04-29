from setuptools import setup

setup(name='opencog-ull',
      version='1.0.0',
      description='Unsupervised Language Learning Toolkit',
      author='SingularityNET',
      url='http://github.com/singnet/language-learning',
      # install_requirements=['tqdm>=4.28.1'],
      namespace_packages=['ull'],
      packages=['ull.common',
                'ull.grammar_tester',
                'ull.grammar_learner',
                'ull.text_parser',
                'ull.parse_evaluator',
                'ull.pipeline',
                'ull.dash_board',
                'ull.link_grammar'],
      package_dir={'ull.common': 'src/common',
                   'ull.grammar_tester': 'src/grammar_tester',
                   'ull.grammar_learner': 'src/grammar_learner',
                   'ull.text_parser': 'src/text_parser',
                   'ull.parse_evaluator': 'src/parse_evaluator',
                   'ull.pipeline': 'src/pipeline',
                   'ull.dash_board': 'src/dash_board',
                   'ull.link_grammar': 'src/link_grammar'
                   },
      scripts=['src/cli_scripts/grammar-tester',
               'src/cli_scripts/parse-evaluator',
               'src/cli_scripts/ull-cli',
               'src/cli_scripts/dict-transformer',
               'src/cli_scripts/token-counter',
               'src/cli_scripts/sentence-counter'
               ],
      platform='any',
      license='MIT',
      classifiers=[
          'Development Status :: 1 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Software Development :: Bug Tracking',
          ],
      long_description=open('README.md').read()
      )