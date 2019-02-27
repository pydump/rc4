import os.path
import setuptools

root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='rc4',
    version='3.7.2',
    url='https://github.com/pydump/rc4',
    license='MIT',
    author='mohanson',
    author_email='mohanson@outlook.com',
    description='RC4 algorithm by pure Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['rc4']
)
