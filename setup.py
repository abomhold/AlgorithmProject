from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension("c_graph", ["c_graph.pyx"], include_dirs=['.']),
    Extension("c_hk", ["c_hk.pyx"], include_dirs=['.'])
]

setup(
    name='algorithms',
    ext_modules=cythonize(extensions)
)
