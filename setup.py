from setuptools import setup

setup(name='Solana Localhost Client',
      version='0.1',
      description='A module to call Rust functions over gRPC',
      url='https://github.com/SolmateDev/py-rust-translator',
      author='Joel De Jesus',
      author_email='joel@noncepad.com',
      license='MIT',
      packages=['solana-grpc-client'],
      zip_safe=False)
