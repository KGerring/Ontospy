# !/usr/bin/env python
#  -*- coding: UTF-8 -*-


"""
>python tools/matcher.py data/schemas/npgcore_latest.ttl data/schemas/foaf.rdf

Loaded 630 triples
started scanning...
----------
Ontologies found: 1
Classes found...: 15
Properties found: 67
Annotation......: 7
Datatype........: 26
Object..........: 34
Loaded 3478 triples
started scanning...
----------
Ontologies found: 1
Classes found...: 64
Properties found: 253
Annotation......: 36
Datatype........: 133
Object..........: 84
----------
Matching...
Person ==~== Term: npg:Person
<Class *http://www.w3.org/2000/10/swap/pim/contact#Person*>
...<Class *http://ns.nature.com/terms/Person*>
Document ==~== Term: npg:Document
<Class *http://xmlns.com/foaf/0.1/Document*>
...<Class *http://ns.nature.com/terms/Document*>
Document ==~== Term: npg:DocumentAsset
<Class *http://xmlns.com/foaf/0.1/Document*>
...<Class *http://ns.nature.com/terms/DocumentAsset*>
Organization ==~== Term: npg:Organization
<Class *http://xmlns.com/foaf/0.1/Organization*>
...<Class *http://ns.nature.com/terms/Organization*>
Person ==~== Term: npg:Person
<Class *http://xmlns.com/foaf/0.1/Person*>
...<Class *http://ns.nature.com/terms/Person*>
PersonalProfileDocument ==~== Term: npg:Document
<Class *http://xmlns.com/foaf/0.1/PersonalProfileDocument*>
...<Class *http://ns.nature.com/terms/Document*>


"""


import csv
import optparse
import os
import time
from difflib import SequenceMatcher

import rdflib

from .. import main
from ..core.utils import *

USAGE = "ontospy-match foaf.rdf bibo.owl -o output.csv"
MATCHER_VERSION = 0.2


# from ontospy import ontospy


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def matcher(
    graph1,
    graph2,
    confidence=0.5,
    output_file="matching_results.csv",
    class_or_prop="classes",
    verbose=False,
):
    """
    takes two graphs and matches its classes based on qname, label etc..
    @todo extend to properties and skos etc..
    """

    printDebug("----------\nNow matching...")

    f = open(output_file, "wt")
    counter = 0

    try:
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(("name 1", "name 2", "uri 1", "uri 2"))

        # a) match classes

        if class_or_prop == "classes":

            for x in graph1.all_classes:
                l1 = str(x.bestLabel(qname_allowed=True))

                for y in graph2.all_classes:
                    l2 = str(y.bestLabel(qname_allowed=True))

                    if similar(l1, l2) > confidence:
                        counter += 1
                        row = [l1, l2, x.uri, y.uri]
                        writer.writerow(
                            [s.encode("utf8") if type(s) is str else s for s in row]
                        )
                        if verbose:
                            print(("%s ==~== %s" % (l1, l2)))

        # b) match properties

        elif class_or_prop == "properties":

            for x in graph1.all_properties:
                l1 = str(x.bestLabel(qname_allowed=True))

                for y in graph2.all_properties:
                    l2 = str(y.bestLabel(qname_allowed=True))

                    if similar(l1, l2) > confidence:
                        counter += 1
                        row = [l1, l2, x.uri, y.uri]
                        writer.writerow(
                            [s.encode("utf8") if type(s) is str else s for s in row]
                        )
                        if verbose:
                            print(("%s ==~== %s" % (l1, l2)))

    finally:
        f.close()

    printDebug("%d candidates found." % counter)


def parse_options():
    """
    parse_options() -> opts, args

    Parse any command-line options given returning both
    the parsed options and arguments.

    https://docs.python.org/2/library/optparse.html

    """

    parser = optparse.OptionParser(usage=USAGE, version=ontospy.VERSION)

    parser.add_option(
        "-o",
        "--outputfile",
        action="store",
        type="string",
        default="",
        dest="outputfile",
        help="The name of the output csv file.",
    )

    parser.add_option(
        "-v",
        "--verbose",
        action="store_true",
        default=False,
        dest="verbose",
        help="Verbose mode: prints results on screen too.",
    )

    opts, args = parser.parse_args()

    return opts, args


import click

@click.command()
@click.option('-o', '--outputfile', default="", help = "The name of the output csv file.")
@click.option('-v', '--verbose', default=False,
              help="Verbose mode: prints results on screen too.")
def _main(outputfile, verbose): pass


def main():
    """command line script"""

    print(("Ontospy " + ontospy.VERSION))
    ontospy.get_or_create_home_repo()

    opts, args = parse_options()

    if len(args) < 2:
        printDebug("Please provide two arguments, or use -h for more options.")
        sys.exit(0)

    var = eval(input("Match classes or properties? [c|p, c=default]:"))
    if var == "c":
        class_or_prop = "classes"
    elif var == "p":
        class_or_prop = "properties"
    else:
        class_or_prop = "classes"

    print(class_or_prop)

    var = eval(input("Degree of confidence? [1-10, 5=default]: "))
    try:
        confidence = int(var)
        if not (confidence <= 10 and confidence >= 1):
            confidence = 5
    except:
        confidence = 5

    print(confidence)
    confidence = confidence / (10 * 1.0)  # transform in decimal

    sTime = time.time()

    # automatically name the file unless a name is provided with -o option
    if not opts.outputfile:
        try:
            opts.outputfile = "%s_%s_matching_%s.csv" % (
                os.path.splitext(args[0])[0].split("/")[-1],
                os.path.splitext(args[1])[0].split("/")[-1],
                class_or_prop,
            )

        except:
            opts.outputfile = f"ontospy_matching_{class_or_prop}.csv"

    g1 = ontospy.Ontospy(args[0])
    g2 = ontospy.Ontospy(args[1])

    matcher(g1, g2, confidence, opts.outputfile, class_or_prop, opts.verbose)

    # finally:
    # print(some stats....)
    eTime = time.time()
    tTime = eTime - sTime
    printDebug("-" * 10)
    printDebug("Time:	   %0.2fs" % tTime)


if __name__ == "__main__":
    import sys

    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
