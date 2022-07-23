# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
Unit test stub for ontosPy

Run like this:

$ python -m ontospy.tests.test_methods


sgcontext = 'https://springernature.github.io/scigraph/jsonld/sgcontext.json'

ENDPOINT: http://dbpedia.org/sparql
JSON: json
LiMo: http://purl.org/LiMo/0.1#
RDF: rdf
TEST_RDF_FOLDER: /Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/
XML: xml
adms: http://www.w3.org/ns/adms#
article_types: http://ns.nature.com/article-types/
base: http://www.dfki.de/~cullrich/instrucionalobjects.owl
bfo: http://www.ifomis.org/bfo/1.0
bibliography: http://www.linguistics-ontology.org/bibliography/bibliography.owl#
bibo_: http://purl.org/ontology/bibo/
cito: 'http://purl.org/spar/cito/cito:'
conflict: http://purl.com/net/conflict#
crm: http://erlangen-crm.org/current/
daml: http://www.daml.org/2001/03/daml+oil#
dc: http://purl.org/dc/elements/1.1/
dcam: http://purl.org/dc/dcam/
dol: http://www.loa-cnr.it/ontologies/DOLCE-Lite#
eco: http://purl.org/obo/owl/ECO
ecrm: http://erlangen-crm.org/current/
event: http://purl.org/NET/c4dm/event.owl#
foaf: http://xmlns.com/foaf/0.1/
foafi: https://lambdamusic.github.io/ontospy-examples/index.html
frbr: http://purl.org/spar/frbr/
gn: http://www.geonames.org/ontology#
gold: http://purl.org/linguistics/gold/
gr: http://purl.org/goodrelations/v1#
jms: http://jena.hpl.hp.com/2003/08/jms#
mono: /Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/uco_monolithic.ttl
msg0: http://web.resource.org/cc/
npg: http://ns.nature.com/terms/
npgd: http://ns.nature.com/datasets/
npgg: http://ns.nature.com/graphs/
ntnames: http://semanticbible.com/2004/09/NTNames#
oa: http://www.w3.org/ns/oa#
obo_: http://purl.org/obo/owl/OBO_REL
obo_rel: http://purl.org/obo/owl/OBO_REL
oo: http://www.springernature.com/scigraph/ontologies
p1: http://dublincore.org/usage/documents/principles/#
paper: /Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/paper.jsonld
prism: http://prismstandard.org/namespaces/basic/2.1/
protege: http://protege.stanford.edu/plugins/owl/protege#
prov: http://www.w3.org/ns/prov#
rel: http://purl.org/vocab/relationship#
resume: http://www.owl-ontologies.com/resume.owl#
ro: http://www.berkeleybop.org/ontologies/obo-all/ro_bfo_bridge/ro_bfo_bridge.owl
rss: http://purl.org/rss/1.0/
sc: http://purl.org/science/owl/sciencecommons/
sci: /Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/scigraph/
sciencecommons: http://purl.org/science/owl/sciencecommons/
sgctx: https://springernature.github.io/scigraph/jsonld/sgcontext.json
sit: http://www.ontologydesignpatterns.org/cp/owl/situation.owl#
status: http://purl.org/ontology/bibo/status/
swrl: http://www.w3.org/2003/11/swrl#
swrlImport: http://www.daml.org/rules/proposal/swrl.owl#
swrlb: http://www.w3.org/2003/11/swrlb#
swrlbImport: http://www.daml.org/rules/proposal/swrlb.owl#
uo: http://suo.ieee.org#
url: https://scigraph.springernature.com/
vann: http://purl.org/vocab/vann/
vcard: http://www.w3.org/2001/vcard-rdf/3.0#
webapi: https://actions.semantify.it/vocab/
wot: http://xmlns.com/wot/0.1/

In [776]: print(box.Box(S).to_toml())
TEST_RDF_FOLDER = "/Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/"
paper = "/Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/paper.jsonld"
sci = "/Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/scigraph/"
mono = "/Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/uco_monolithic.ttl"
ENDPOINT = "http://dbpedia.org/sparql"
p1 = "http://dublincore.org/usage/documents/principles/#"
crm = "http://erlangen-crm.org/current/"
ecrm = "http://erlangen-crm.org/current/"
jms = "http://jena.hpl.hp.com/2003/08/jms#"
article_types = "http://ns.nature.com/article-types/"
npgd = "http://ns.nature.com/datasets/"
npgg = "http://ns.nature.com/graphs/"
npg = "http://ns.nature.com/terms/"
prism = "http://prismstandard.org/namespaces/basic/2.1/"
protege = "http://protege.stanford.edu/plugins/owl/protege#"
conflict = "http://purl.com/net/conflict#"
LiMo = "http://purl.org/LiMo/0.1#"
event = "http://purl.org/NET/c4dm/event.owl#"
dcam = "http://purl.org/dc/dcam/"
dc = "http://purl.org/dc/elements/1.1/"
gr = "http://purl.org/goodrelations/v1#"
gold = "http://purl.org/linguistics/gold/"
eco = "http://purl.org/obo/owl/ECO"
obo_ = "http://purl.org/obo/owl/OBO_REL"
obo_rel = "http://purl.org/obo/owl/OBO_REL"
bibo_ = "http://purl.org/ontology/bibo/"
status = "http://purl.org/ontology/bibo/status/"
rss = "http://purl.org/rss/1.0/"
sc = "http://purl.org/science/owl/sciencecommons/"
sciencecommons = "http://purl.org/science/owl/sciencecommons/"
cito = "http://purl.org/spar/cito/cito:"
frbr = "http://purl.org/spar/frbr/"
discourse_relationships = "http://purl.org/swan/2.0/discourse-relationships/"
rel = "http://purl.org/vocab/relationship#"
vann = "http://purl.org/vocab/vann/"
ntnames = "http://semanticbible.com/2004/09/NTNames#"
uo = "http://suo.ieee.org#"
msg0 = "http://web.resource.org/cc/"
ro = "http://www.berkeleybop.org/ontologies/obo-all/ro_bfo_bridge/ro_bfo_bridge.owl"
daml = "http://www.daml.org/2001/03/daml+oil#"
swrlImport = "http://www.daml.org/rules/proposal/swrl.owl#"
swrlbImport = "http://www.daml.org/rules/proposal/swrlb.owl#"
base = "http://www.dfki.de/~cullrich/instrucionalobjects.owl"
gn = "http://www.geonames.org/ontology#"
bfo = "http://www.ifomis.org/bfo/1.0"
bibliography = "http://www.linguistics-ontology.org/bibliography/bibliography.owl#"
dol = "http://www.loa-cnr.it/ontologies/DOLCE-Lite#"
sit = "http://www.ontologydesignpatterns.org/cp/owl/situation.owl#"
resume = "http://www.owl-ontologies.com/resume.owl#"
oo = "http://www.springernature.com/scigraph/ontologies"
vcard = "http://www.w3.org/2001/vcard-rdf/3.0#"
swrl = "http://www.w3.org/2003/11/swrl#"
swrlb = "http://www.w3.org/2003/11/swrlb#"
adms = "http://www.w3.org/ns/adms#"
oa = "http://www.w3.org/ns/oa#"
prov = "http://www.w3.org/ns/prov#"
foaf = "http://xmlns.com/foaf/0.1/"
wot = "http://xmlns.com/wot/0.1/"
webapi = "https://actions.semantify.it/vocab/"
foafi = "https://lambdamusic.github.io/ontospy-examples/index.html"
url = "https://scigraph.springernature.com/"
sgctx = "https://springernature.github.io/scigraph/jsonld/sgcontext.json"
JSON = "json"
RDF = "rdf"
XML = "xml"

"""


import os
import sys
import time
import unittest

from .. import *
from ..core import *
from ..core.utils import *
from .context import TEST_RDF_FOLDER

# sanity check
printDebug(f"-------------------\nOntospy {VERSION}\n-------------------")

class SampleCustomEntity(ontospy.RdfEntity):
    def __init__(
        self,
        uri,
        rdftype=None,
        namespaces=None,
        ext_model=False,
        pref_title="qname",
        pref_lang="en",
    ):
        super(SampleCustomEntity, self).__init__(
            uri, rdftype, namespaces, ext_model, pref_title, pref_lang
        )

    def __repr__(self):
        return "<SampleCustomEntity *%s*>" % (self.uri)

    def disjointWith(self):
        """
        Example: pull out disjoint with statements
        """
        pred = "http://www.w3.org/2002/07/owl#disjointWith"
        return self.getValuesForProperty(pred)

class TestMethods(unittest.TestCase):

    printDebug(
        f"""\n=================\n
	\nTEST Methods: checking specific ontospy methods 
	\n\n=================""",
        bg="blue",
        fg="white",
    )

    time.sleep(3)

    # load sample ontologies

    f = TEST_RDF_FOLDER + "pizza.ttl"
    printDebug("\n*****\n ..loading local ontology > %s\n*****" % str(f), "important")
    o = Ontospy(f, verbose=True, pref_title="label")

    f = TEST_RDF_FOLDER + "multilingual.ttl"
    printDebug("\n*****\n ..loading local ontology > %s\n*****" % str(f), "important")
    o2 = Ontospy(f, verbose=True, pref_title="qname", pref_lang="en")

    def test0(self):
        """
        Class methods
        """
        printDebug(
            "\n=================\nTEST 0: Checking the <class> displays", bg="green"
        )

        for c in self.o.all_classes:
            print(("URI: ", c.uri))
            print(("RDFTYPE: ", c.rdftype))
            print(("BEST LABEL: ", c.bestLabel()))
            print(("TITLE: ", c.title))
            print("===")

        printDebug("Test completed succesfully.\n", "green")

    def test1(self):
        """
        Instances method
        """
        printDebug(
            "\n=================\nTEST 1: Checking the <instances> method", bg="green"
        )

        for c in self.o.all_classes:
            # c.describe()
            if c.instances:
                print(("CLASS: " + c.uri + " " + c.title))
                print("INSTANCES: ")
                for el in c.instances:
                    print((el.uri, el.qname))
                    print(
                        (
                            el.getValuesForProperty(
                                "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                            )
                        )
                    )

        printDebug("Test completed succesfully.\n", "green")

    def test2(self):
        """
        getValuesForProperty
        """
        printDebug(
            "\n=================\nTEST 2: Checking the <getValuesForProperty> method",
            bg="green",
        )

        for c in self.o.all_classes[:3]:
            print("CLASS: ")
            print((c.uri, c.qname, c.title))
            print("RDF:TYPE VALUES: ")
            print(
                (
                    c.getValuesForProperty(
                        "http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
                    )
                )
            )

        printDebug("Test completed succesfully.\n", "green")

    def test3(self):
        """
        build_entity_from_uri
        """
        printDebug(
            "\n=================\nTEST 3: Checking the <build_entity_from_uri> method",
            bg="green",
        )

        e = self.o.build_entity_from_uri(
            "http://www.co-ode.org/ontologies/pizza/pizza.owl#Germany"
        )
        print(("URI: ", e))
        print(("RDFTYPE: ", e.rdftype))
        print(("BEST LABEL: ", e.bestLabel()))
        print(("TITLE: ", e.title))
        print("RDF SOURCE: ")
        print((e.rdf_source()))
        printDebug("Test completed succesfully.\n", "green")

    def test4(self):
        """
        build_entity_from_uri - SampleCustomEntity
        """
        printDebug(
            "\n=================\nTEST 4: Checking the <build_entity_from_uri> method using a SampleCustomEntity class ",
            bg="green",
        )

        e = self.o.build_entity_from_uri(
            "http://www.co-ode.org/ontologies/pizza/pizza.owl#FruttiDiMare",
            SampleCustomEntity,
        )
        print(("URI: ", e))
        print(("RDFTYPE: ", e.rdftype))
        print(("BEST LABEL: ", e.bestLabel()))
        print(("TITLE: ", e.title))
        print("OWL DISJOINT WITH: ")
        print(("\n".join([x for x in e.disjointWith()])))
        printDebug("Test completed succesfully.\n", "green")

    def test5(self):
        """
        Pref label and pref language parameters
        """

        printDebug(
            "\n=================\nTEST 5-1: pref_title=qname / pref_lang=en", bg="green"
        )
        for c in self.o2.all_classes:
            print(("URI: ", c.uri))
            print(("RDFTYPE: ", c.rdftype))
            print(("BEST LABEL: ", c.bestLabel()))
            print(("TITLE: ", c.title))
            print("===")

        printDebug(
            "\n=================\nTEST 5-2: pref_title=label / pref_lang=it", bg="green"
        )
        for c in self.o2.all_classes:
            print(("URI: ", c.uri))
            print(("RDFTYPE: ", c.rdftype))
            print(("BEST LABEL: ", c.bestLabel()))
            print(("TITLE: ", c.title))
            print("===")

        printDebug(
            "\n=================\nTEST 5-3: pref_title=label / pref_lang=es", bg="green"
        )
        for c in self.o2.all_classes:
            print(("URI: ", c.uri))
            print(("RDFTYPE: ", c.rdftype))
            print(("BEST LABEL: ", c.bestLabel()))
            print(("TITLE: ", c.title))
            print("===")

        printDebug("Test completed succesfully.\n", "green")

    print("Success.\n")



#'https://github.com/biolink/ontobio.git'
#'https://github.com/w3c/feedvalidator.git'


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
