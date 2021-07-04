# squiral
[![](https://img.shields.io/pypi/v/squiral)](https://pypi.org/project/squiral/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![](https://img.shields.io/pypi/pyversions/squiral.svg)](https://pypi.org/project/squiral/)<br/>
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/sadikkuzu/squiral/main.svg)](https://results.pre-commit.ci/latest/github/sadikkuzu/squiral/main)
[![Python lint&test](https://github.com/sadikkuzu/squiral/actions/workflows/python-package.yml/badge.svg)](https://github.com/sadikkuzu/squiral/actions/workflows/python-package.yml)
[![Publish Python Package](https://github.com/sadikkuzu/squiral/actions/workflows/python-publish.yml/badge.svg)](https://github.com/sadikkuzu/squiral/actions/workflows/python-publish.yml)

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

The basic idea behind printing this matrix is<br/>
to start from the middle of the matrix and then moving:<br/>
`right` >> `down` >> `left` >> `up`<br/>
and not returning to the same row again.

### Install

`pip install squiral`

#### Usage

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
