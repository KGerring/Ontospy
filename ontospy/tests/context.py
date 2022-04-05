# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
Unit tests shared constants
"""


import os

dir_path = os.path.dirname(os.path.realpath(__file__))
TEST_RDF_FOLDER = dir_path + "/rdf/"


__all__ = sorted(
		[
				getattr(v, "__name__", k)
				for k, v in list(globals().items())  # export
				if (
				(
						callable(v)
						and getattr(v, "__module__", "")
						== __name__  # callables from this module
						or k.isupper()
				)
				and not str(getattr(v, "__name__", k)).startswith("__")  # or CONSTANTS
		)
		]
)  # neither marked internal


