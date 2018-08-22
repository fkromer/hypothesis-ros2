.. _guide:

User's Guide
============

Compatibility
-------------

This section is about what has to be considered w.r.t. compatibility with
the ROS2 and Python runtime environment.

ROS2 versions
.............

`hypothesis-ros2` supports all non-alpha `ROS2 releases`_ (beginning with Ardent Apalone)
which are:

- `ROS2 Ardent Apalone`_
- `ROS2 Bouncy Bolson`_

.. _ROS2 releases: https://github.com/ros2/ros2/wiki/Releases
.. _ROS2 Ardent Apalone: https://github.com/ros2/ros2/wiki/Release-Ardent-Apalone
.. _ROS2 Bouncy Bolson: https://github.com/ros2/ros2/wiki/Release-Bouncy-Bolson

ROS2 message package versions
.............................

To keep maintenance effort as low as possible ROS2 
Currently 
Reproducible test infrastructure is critical. However the required effort to
maintain separate packages 


ROS2 build tools
................

The recommended build tool for ROS2 Ardent Apalone is `ament`_.
Beginning with ROS2 Bouncy Bolson the recommended build tool is `colcon`_ (`ROS2 design build tool`).
Both build tools may integrate with `nose` and `pytest` via the `ament` buildsystem in CMake.
`ament_cmake`_ provides integration with `nose` via `ament_cmake_nose`_
and integration with `pytest` via `ament_cmake_pytest`_ respectively.

.. _ament: https://github.com/ament
.. _ROS2 design build tool: http://design.ros2.org/articles/build_tool.html
.. _colcon: https://colcon.readthedocs.io/en/latest/
.. _ament_cmake: https://github.com/ament/ament_cmake
.. _ament_cmake_nose: https://github.com/ament/ament_cmake/tree/master/ament_cmake_nose
.. _ament_cmake_pytest: https://github.com/ament/ament_cmake/tree/master/ament_cmake_pytest

Python interpreters
...................

ROS2 requires at least Python version 3.5 (`ROS2 design changes`_).
ROS2 isn't supporting PyPy (`Will ROS2 support PyPy?`_).
All Python dependencies of `hypothesis-ros2` satisfy this requirement:

- `hypothesis` is supported and tested on `CPython 3.4+` (`hypothesis docs python versions`_).

.. _ROS2 design changes: http://design.ros2.org/articles/changes.html
.. _Will ROS2 support pypy?: https://answers.ros.org/question/291981/will-ros2-support-pypy/
.. _hypothesis docs python versions: https://hypothesis.readthedocs.io/en/latest/supported.html#python-versions

Python test frameworks (test runners)
.....................................

The *ROS2* build tools support the Python test runners *nose* and *pytest*. 
`hypothesis-ros` extends `hypothesis` which means that compatible Python test runners
depend on `hypothesis`. `Hypothesis` is compatible with (`hypothesis docs testing frameworks`_):

- `unittest` (supported, tested, no limitations),
- `pytest` (supported, tested, limitations: function based fixtures do not behave like expected),
- `nose` (supported, tested, yield based tests do not work)

.. _hypothesis docs testing frameworks: https://hypothesis.readthedocs.io/en/latest/supported.html#testing-frameworks

Configuration
-------------

This section is about what has to be considered w.r.t. configuration of *hypothesis* specifics and tests.

hypothesis settings
...................

`hypothesis` was initially designed for Python source code level testing.
Therefore the configuration of `settings` needs special care.

`deadline`: A deadline has either set to a very high value or should be disabled.

`perform_health_checks`: In case `perform_health_checks` is enabled some health checks
need to be selectively disabled with `suppress_health_check`.

`suppress_health_check`: Refer to :ref:`hypothesis health checks`.

`use_coverage`: `hypothesis` supports coverage based data generation when the tests
are executed on the Python source code level. `hypothesis-ros` does not support
coverage based data generation. Enabling it has no effect/could raise errors. 

A typical configuration of `timeout` and `deadline` in `@settings` looks like follows:

.. code-block:: python

    ...
    from hypothesis import settings, unlimited

    ...
    @settings(timeout=unlimited,
              deadline=None,
              ...)
    def test_node_does_not_crash(...):
        ...

The settings `database_file`, `database`, `buffer_size`, `derandomize`,
`max_examples`, `max_iterations`, `max_shrinks`, `min_satisfying_examples`,
`phases`, `stateful_step_count`, `strict`, usually don't need special
consideration and may be used as usual.

.. _hypothesis health checks:

hypothesis health checks
........................

`hypothesis` was initially designed for Python source code level testing.
Therefore the configuration of `health checks` (`hypothesis docs health checks`_)
needs special care. In case health checks are performed (`perform_health_checks`)
the health ckeck `too_slow` and `hung_test` need to be disabled via
`suppress_healthcheck` usually.

.. _hypothesis docs health checks: https://hypothesis.readthedocs.io/en/latest/healthchecks.html

A typical configuration of `suppress_health_check` in `@settings` looks like follows:

.. code-block:: python

    ...
    from hypothesis import settings, HealthCheck

    ...
    @settings(...,
              suppress_health_check=[HealthCheck.too_slow,
                                     HealthCheck.hung_test]
             )
    def test_node_does_not_crash(...):
        ...

The health checks `data_too_large`, `filter_too_much`, `return_value` and `large_base_example`
don't need special consideration and may be used as usual.

hypothesis example database
...........................

If a test fails `hypothesis` saves the test input into a database.
The next time `hypothesis` runs this conditions will be used first.
The configuration of the example database may be adjusted as usual
(`hypothesis docs example database`_).

.. _hypothesis docs example database: https://hypothesis.readthedocs.io/en/latest/database.html?highlight=example%20database#the-hypothesis-example-database
