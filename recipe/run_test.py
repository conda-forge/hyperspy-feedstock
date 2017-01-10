#!/usr/bin/python
"""Run nosetests after setting ETS toolkit to "null"."""

if __name__ == '__main__':
    import sys
    from nose import run_exit
    from traits.etsconfig.api import ETSConfig
    import os
    from subprocess import call
    call("python setup.py build_ext --inplace",
          shell=True)
    ETSConfig.toolkit = "null"
    import matplotlib
    matplotlib.use("Agg")

    sys.argv.append('hyperspy.tests')
    sys.exit(run_exit())
