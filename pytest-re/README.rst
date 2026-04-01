=========
pytest-re
=========

.. image:: https://img.shields.io/pypi/v/pytest-re.svg
    :target: https://pypi.org/project/pytest-re
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/pytest-re.svg
    :target: https://pypi.org/project/pytest-re
    :alt: Python versions

.. image:: https://github.com/sauravk90/pytest-re/actions/workflows/main.yml/badge.svg
    :target: https://github.com/sauravk90/pytest-re/actions/workflows/main.yml
    :alt: See Build Status on GitHub Actions

Re-run pytest tests from JUnit XML reports.

Why this exists
---------------

CI systems often keep JUnit XML artifacts, but pytest's built-in ``--last-failed``
only works when the local ``.pytest_cache`` from the original run is still
available. ``pytest-re`` closes that gap by selecting tests directly from a
JUnit XML report.

Features
--------

* Re-run only the tests referenced by one or more JUnit XML reports.
* Filter which XML statuses should be selected with ``--from-xml-status``.
* Strip a known classname prefix with ``--from-xml-prefix`` when reports were
  generated with ``--junit-prefix``.
* Works with standard pytest JUnit XML and xdist-generated JUnit XML reports.

Installation
------------

Install from PyPI::

    pip install pytest-re

Usage
-----

Generate a JUnit XML report from a normal pytest run::

    pytest --junitxml=report.xml

Re-run only failed and errored tests from that report::

    pytest --from-xml report.xml

Select a different set of XML statuses::

    pytest --from-xml report.xml --from-xml-status=passed

Use multiple reports at once::

    pytest --from-xml shard-a.xml shard-b.xml

If the report was generated with a classname prefix, strip it during mapping::

    pytest --junitxml=report.xml --junit-prefix=ci
    pytest --from-xml report.xml --from-xml-prefix=ci

How matching works
------------------

``pytest-re`` reads each ``<testcase>`` entry from the JUnit XML report, maps it
back to a pytest node ID, and deselects everything else during collection.

When multiple reports contain the same test case, ``pytest-re`` keeps the worst
observed status using this order:

* ``error``
* ``failed``
* ``skipped``
* ``passed``

Notes
-----

* The plugin targets pytest-generated JUnit XML and nearby variants.
* If a testcase from the XML cannot be mapped to a collected pytest item, the
  run continues and reports how many XML cases were unmatched.
* Parametrized tests are supported as long as their parameterized names are
  present in the XML report.

Contributing
------------

Run the test suite with::

    tox

License
-------

Distributed under the terms of the `MIT`_ license, ``pytest-re`` is free and
open source software.

Issues
------

If you encounter any problems, please `file an issue`_ with a detailed
description and, if possible, the JUnit XML snippet that triggered the issue.

.. _`MIT`: https://opensource.org/licenses/MIT
.. _`file an issue`: https://github.com/sauravk90/pytest-re/issues
