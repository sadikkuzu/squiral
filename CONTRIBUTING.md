# Contributor’s Guide

This project is a community effort, and everyone is welcome to contribute. We're thrilled that you're interested in contributing.

This document lays out guidelines and advice for contributing to this project. If you’re thinking of contributing, please start by reading this document and getting a feel for how contributing to this project works.

## Getting Started

Before you begin, make sure you have set up your [development environment](README.md) and read our [code of conduct](CODE_OF_CONDUCT.md).


## Code Contributions

When contributing code, you’ll want to follow this checklist:
1. Fork the repository on GitHub and clone it to your local system.

2. Run the tests to confirm they all pass on your system. If they don’t, you’ll need to investigate why they fail. If you’re unable to diagnose this yourself, raise it as a bug report by following the guidelines in this document: Bug Reports.

3. Make your change and write tests that demonstrate your bug or feature. Ensure that they pass.

4. Send a GitHub Pull Request to the main repository’s main branch. [GitHub Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) are the expected method of code collaboration on this project.

The following sub-sections go into more detail on some of the points above.

## Code Review

Contributions will not be merged until they’ve been code reviewed. You should implement any code review feedback unless you strongly object to it. If you object to the code review feedback, you should make your case clearly and calmly. After doing so, the feedback is judged to still apply, you must either apply the feedback or withdraw your contribution.

## Code Style

Squiral uses a collection of tools to ensure the code base has a consistent style as it grows. We using a tool called [pre-commit](https://pre-commit.com/). It can be installed locally and run over your changes prior to opening a PR, and will also be run as part of the CI approval process before a change is merged.
You can find the full list of formatting requirements specified in the [.pre-commit-config.yaml](.pre-commit-config.yaml) at the top level directory of Squiral.

## Bug Reports

Bug reports are hugely important! Before you raise one, please check through the open and closed GitHub issues to confirm that the bug hasn’t been reported before. Duplicate bug reports are a massive drain on the time of other contributors and should be avoided as much as possible.

If you find a bug or want to request a new feature, please [open an issue](https://github.com/sadikkuzu/squiral/issues) and follow the [format of the issue](.github/workflows/ISSUE_TEMPLATE/BUG_REPORT.md).

## Pull Request Template

When you create a PR, please use the following [template](.github/workflows/ISSUE_TEMPLATE/PULL_REQUEST_TEMPLATE.md)
