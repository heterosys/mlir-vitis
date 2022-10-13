"""MLIR toolchain to import and export Vitis HLS LLVM (.ll) files.
See:
https://github.com/heterosys/mlir-vitis
"""

from setuptools import find_packages, setup

with open('README.md', encoding='utf-8') as f:
  long_description = f.read()

setup(
    name='mlir-vitis',
    version='0.1',
    description='MLIR toolchain to import and export Vitis HLS LLVM (.ll) files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/heterosys/mlir-vitis',
    author='Jason Lau',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: System :: Hardware',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'click>=7.1.2',
    ],
    entry_points={
        'console_scripts': [
            'mlir-to-vitis=mlir-to-vitis.main:entry_point',
            'vitis-to-mlir=vitis-to-mlir.main:entry_point'
        ],
    },
    include_package_data=True,
)
