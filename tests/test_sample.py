#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import logging
import os

import diskcache
import kanilog
import pytest
import ring
import stdlogging
from add_parent_path import add_parent_path

with add_parent_path():
    import ring_pandas_df


logger = kanilog.get_module_logger(__file__, 0)


def setup_module(module):
    pass


def teardown_module(module):
    pass


def setup_function(function):
    pass


def teardown_function(function):
    pass


storage = diskcache.Cache("/tmp/.diskcache")


@ring.disk(storage)
def cached_func(df):
    return df


def test_func():
    import pandas as pd

    df = pd.DataFrame()
    assert hasattr(df, "__ring_key__")
    cached_func(df)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    kanilog.setup_logger(
        logfile="/tmp/%s.log" % (os.path.basename(__file__)), level=logging.INFO
    )
    stdlogging.enable()

    pytest.main([__file__, "-k test_", "-s"])
