# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
Unit test stub for ontosPy

Run like this:

$ python -m ontospy.tests.test_load_local

"""


import os
import time
import unittest

from .. import *
from ..core import *
from ..core.utils import *
from .context import TEST_RDF_FOLDER

# sanity check
printDebug(f"-------------------\nOntospy {VERSION}\n-------------------")


class TestLoadOntologies(unittest.TestCase):
    def test1_load_locally(self):
        """
        Check if the ontologies in /RDF folder load ok
        """

        printDebug(
            f"""\n=================\n
		\nTEST 1: Loading all ontologies in => {TEST_RDF_FOLDER} 
		\nFor each model detailed entities descriptions are printed out.
		\n\n=================""",
            bg="blue",
            fg="white",
        )

        time.sleep(3)

        for f in os.listdir(TEST_RDF_FOLDER):
            if not f.startswith("."):
                printDebug(
                    "\n*****\nTest: loading file... > %s\n*****" % str(f), bg="green"
                )

                o = Ontospy(TEST_RDF_FOLDER + f, verbose=True)

                print("CLASS TREE")
                o.printClassTree()
                print("----------")

                # for c in o.all_classes:
                # 	c.describe()

                # for p in o.all_properties:
                # 	p.describe()

                # for s in o.all_skos_concepts:
                # 	s.describe()

                print("Success.\n")


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


if __name__ == "__main__":
    unittest.main()
