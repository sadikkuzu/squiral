# squiral
[![](https://img.shields.io/pypi/v/squiral)](https://pypi.org/project/squiral/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![](https://img.shields.io/pypi/pyversions/squiral.svg)](https://pypi.org/project/squiral/)
[![Downloads](https://pepy.tech/badge/squiral)](https://pepy.tech/project/squiral)
<br/>
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sadikkuzu/squiral/main.svg)](https://results.pre-commit.ci/latest/github/sadikkuzu/squiral/main)
[![Python lint&test](https://github.com/sadikkuzu/squiral/actions/workflows/python-package.yml/badge.svg)](https://github.com/sadikkuzu/squiral/actions/workflows/python-package.yml)
[![Publish Python Package](https://github.com/sadikkuzu/squiral/actions/workflows/python-publish.yml/badge.svg)](https://github.com/sadikkuzu/squiral/actions/workflows/python-publish.yml)
<br/>
[![Sourcegraph](https://img.shields.io/badge/view%20on-Sourcegraph-brightgreen.svg?style=for-the-badge&logo=sourcegraph)](https://sourcegraph.com/github.com/sadikkuzu/squiral)
[![codecov](https://codecov.io/gh/sadikkuzu/squiral/branch/main/graph/badge.svg?token=4KLW43HVVY)](https://codecov.io/gh/sadikkuzu/squiral)

**squ**are sp**iral**

```
Welcome to Squiral!
Here is an example:
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
```

**squiral** is a simple and lightweight Python library for generating square spiral patterns.<br/>
With **squiral**, you can easily create a wide range of square spiral designs, from simple to complex.<br/>

**squiral** is easy to use and integrate into existing projects,<br/>
making it a great tool for data visualization, computer graphics, and other applications.<br/>
With **squiral**, you can quickly and easily generate square spiral patterns<br/>
that are both beautiful and functional.<br/>
Whether you're working on a personal project or a professional one,<br/>
**squiral**'s square spiral generator is the perfect tool<br/>
for adding unique and visually striking designs to your work.

The basic idea behind printing this matrix is<br/>
to start from the middle of the matrix and then moving:<br/>
`right` >> `down` >> `left` >> `up`<br/>
and not returning to the same row again.

### Install

#### [PyPI](https://pypi.org/project/squiral/)

```shell
pip install squiral
```

#### [GitHub](https://github.com/sadikkuzu/squiral)

```shell
pip install git+https://github.com/sadikkuzu/squiral.git
```

### Usage

#### In console:

```console
buddha@dharma:~$ squiral 7
43 44 45 46 47 48 49
42 21 22 23 24 25 26
41 20  7  8  9 10 27
40 19  6  1  2 11 28
39 18  5  4  3 12 29
38 17 16 15 14 13 30
37 36 35 34 33 32 31
buddha@dharma:~$ squiral --help
usage: squiral [-h] size

positional arguments:
  size        squiral size

optional arguments:
  -h, --help  show this help message and exit
```

#### In python:

```python
>>> import squiral as sq
>>> sq.printout(sq.produce(5))
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
>>>
```
