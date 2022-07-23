# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
Python and RDF Utils for Ontospy

Copyright (c)  __Michele Pasin__ <http://www.michelepasin.org>. All rights reserved.

"""
import rdflib
from .utils import *
from . import utils as ut

DEFAULT_LANGUAGE = "en"
yago_endpoint = 'https://yago-knowledge.org/sparql/query'
dbpedia_endpoint = 'http://dbpedia.org/sparql'
triply =  'https://api.triplydb.com/queries/academy/sparql-html/run'

#extruct.extract


# rdf.plugins.store,
# rdf.plugins.serializer,
# rdf.plugins.resultserializer,
# rdf.plugins.resultparser,
# rdf.plugins.queryresult,
# rdf.plugins.queryprocessor,
# rdf.plugins.parser

INV = '/Users/kristen/repos/_tmp/linkml/docs/objects.inv'

#databricks_cli.cli:cli
#datapackage.__main__:cli
#datasets.commands.datasets_cli:main


#deepdiff.commands:cli
#extruct.tool:main

#genson.cli:main

#isort.main:identify_imports_main
#isort.main:main

#json_flattener.cli:main

#jsonpath_ng.bin.jsonpath:entry_point
#jsonschema.cli:main

#jupytext.cli:jupytext

#kgx.cli:cli


###### jsonschema

#linkml.generators.golrgen:cli
#linkml.generators.jsonldcontextgen:cli
#linkml.generators.jsonldgen:cli
#linkml.generators.jsonschemagen:cli
#linkml.generators.linkmlgen:cli
#linkml.generators.namespacegen:cli
#linkml.generators.owlgen:cli
#linkml.generators.prefixmapgen:cli
#linkml.generators.projectgen:cli
#linkml.generators.pythongen:cli
#linkml.generators.rdfgen:cli
#linkml.generators.shaclgen:cli
#linkml.generators.shexgen:cli
#linkml.generators.sparqlgen:cli
#linkml.generators.sqlalchemygen:cli
#linkml.generators.sqltablegen:cli
#linkml.generators.sssomgen:cli
#linkml.generators.yamlgen:cli
#linkml.generators.yumlgen:cli
#linkml.utils.converter:cli
#linkml.utils.execute_tutorial:cli
#linkml.utils.sqlutils:main

#linkml.validators.jsonschemavalidator:cli
#linkml.validators.sparqlvalidator:cli
#linkml_dataops.changer.jsonpatch_changer:cli
#linkml_dataops.generators.apigenerator:cli
#linkml_dataops.generators.pyapigenerator:cli
#linkml_runtime.utils.comparefiles:cli
#linkml.reporting.model

#linkml.validators.sparqlvalidator sparqljson2dict, _make_result, SparqlDataValidator,
#if endpoint_url is not None: results = validator.validate_endpoint(endpoint_url, limit=limit, named_graphs=named_graph)
#input_format = _get_format(input, input_format)
#results = validator.validate_file(input, format=input_format)
#output_format = _get_format(output, output_format, default='json')
#dumper = get_dumper(output_format)


#mlflow.cli:cli
#netCDF4.utils:ncinfo
#ontogram.cli:main


#pyfiglet:main

#pyglossary.ui.main:main #/opt/anaconda3/envs/py39/lib/python3.9/site-packages/pyglossary/ui/main.py
#pyjsg.parser_impl.generate_python:generate
#shexeval pyshex.shex_evaluator:evaluate_cli, pytaxonomies.script:main
#ray.ray_operator.operator:main
#ray.scripts.scripts:main, ray.serve.scripts:cli, ray.tune.scripts:cli

#repoze.sendmail.queue:run_console
#rnc2rng.__main__:main


#schema_salad.main:main
#schema_salad.makedoc:main
#skosify.cli:main,
# splitter.splitter:main,
# sqlparse.__main__:main,
# sssom.cli:main
# tldextract.cli:main,
# tuna.cli:main, uncompyle6.bin.uncompile:main_bin
#userpath.cli:userpath
#xml2rfc.run:main

#xmlschema.resources.XMLResource, LazyXPath2Parser, LazySelector, normalize_url, is_url, is_local_scheme, is_remote_url
#is_local_url, url_path_is_file, normalize_locations, fetch_resource, fetch_schema_locations, fetch_schema, fetch_namespaces

#xmlschema.helpers.get_namespace

#xmlschema.documents

#xmlschema.cli:json2xml, xmlschema.cli:xml2json, xmlschema.cli:validate

from requests_cache import _utils, mongodb, redis, patcher, session
#CACHE_NAME_KWARGS
#ALL_METHODS
#BACKEND_CLASSES
#BACKEND_KWARGS
#DO_NOT_CACHE
#CacheMixin, uninstall_cache, install_cache, CachedSession
#SERIALIZERS
#requests_cache.install_cache('demo_cache')



#cache_name: Cache prefix or namespace, depending on backend
#backend: Cache backend name or instance = ['sqlite', 'filesystem', 'mongodb', 'gridfs', 'redis', 'dynamodb', 'memory']
#cache = init_backend(cache_name, backend, **kwargs)


#http://vocabulary.semantic-web.at/PoolParty/sparql/OpenData
#http://lod.springer.com/sparql
#http://ldf.fi/ww1lod/sparql
#http://dbpedia.org/sparql
#http://kbpedia.org/ontologies/kko#WrittenInfo


#skos:prefLabel
#application/sparql-results+xml
#application/sparql-results+json
#text/x-html+tr
#text/x-html+tr
#sd:resultFormat
#sd:supportedLanguage
#text/cxml
#application/odata+json
#application/x-ld+json
#application/ld+json
#application/x-nice-microdata
#text/x-html-script-ld+json
#text/x-html-nice-turtle
#application/microdata+json
#sd:Service

from datasets import SCRIPTS_VERSION, config, load_dataset, load_from_disk
#from datasets.filesystems import *
#from .utils import *
#naming
#info
#formatting
#arrow_dataset
#Dataset
#concatenate_datasets
#data_files
#dataset_dict
#iterable_dataset
#BuilderConfig
#DatasetBuilder
#DatasetDict
#ClassLabel
#Features
#TranslationVariableLanguages
#DatasetInfo
#MetricInfo
#packaged_modules
#load
#inspect
#get_dataset_config_names
#et_dataset_infos
#get_dataset_split_names
#list_datasets,list_metrics,load_dataset,load_dataset_builder
#doc_utils,info_utils,file_utils,py_utils,download_manager,streaming_download_manager
#DownloadConfig,relative_to_absolute_path,flatten_nest_dict,as_sufficient_disk_space,
#map_nested





class SparqlHelper:
    """
    Class containing a bunch of useful RDF queries.

    Tip:the sparql query returns always a `rdflib.plugins.sparql.processor.SPARQLResult` instance;
    calling the list method on it transforms it into a list of tuples/triples

    Eg
    [(rdflib.term.URIRef(u'http://www.w3.org/2006/time'))]

    Hence, when a list is returned, the URI/entity is extracted with index [0]
    """

    def __init__(self, rdfgraph: rdflib.Graph, sparql_endpoint=False):
        super(SparqlHelper, self).__init__()
        self.rdflib_graph = rdfgraph
        self.sparql_endpoint = sparql_endpoint

        # Bind a few prefix, namespace pairs for easier sparql querying
        self.rdflib_graph.bind("rdf", rdflib.namespace.RDF)
        self.rdflib_graph.bind("rdfs", rdflib.namespace.RDFS)
        self.rdflib_graph.bind("owl", rdflib.namespace.OWL)
        self.rdflib_graph.bind("skos", rdflib.namespace.SKOS)
        self.rdflib_graph.bind("dc", "http://purl.org/dc/elements/1.1/")
        self.rdflib_graph.bind("vann", "http://purl.org/vocab/vann/")
        self.rdflib_graph.bind("void", "http://rdfs.org/ns/void#")
        self.rdflib_graph.bind("xsd", "http://www.w3.org/2001/XMLSchema#")
        self.rdflib_graph.bind("sh", "http://www.w3.org/ns/shacl#")

    # ..................
    # ONTOLOGY
    # ..................

    def getOntology(self):
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
               WHERE {
                  ?x a owl:Ontology
               }"""
        )
        return list(qres)

    # ..................
    # RDF/OWL CLASSES
    # ..................

    def getAllClasses(self, hide_base_schemas=True, hide_implicit_types=True):
        """
        * hide_base_schemas: by default, obscure all RDF/RDFS/OWL/XML stuff
        * hide_implicit_types: don't make any inference based on rdf:type declarations
        """
        query = """SELECT DISTINCT ?x ?c
                 WHERE {
                         {
                             { ?x a owl:Class }
                             union
                             { ?x a rdfs:Class }
                             union
                             { ?x rdfs:subClassOf ?y }
                             union
                             { ?z rdfs:subClassOf ?x }
                             union
                             { ?y rdfs:domain ?x }
                             union
                             { ?y rdfs:range ?x }
                             %s
                         } .

                         OPTIONAL { ?x a ?c } 
                         # get the type too if available

                    %s

                 }
                 ORDER BY  ?x
                 """

        BIT_BASE_SCHEMAS = """FILTER(
                     !STRSTARTS(STR(?x), "http://www.w3.org/2002/07/owl")
                     && !STRSTARTS(STR(?x), "http://www.w3.org/1999/02/22-rdf-syntax-ns")
                     && !STRSTARTS(STR(?x), "http://www.w3.org/2000/01/rdf-schema")
                     && !STRSTARTS(STR(?x), "http://www.w3.org/2001/XMLSchema")
                     && !STRSTARTS(STR(?x), "http://www.w3.org/XML/1998/namespace")
                     && (!isBlank(?x))
                      ) ."""
        BIT_IMPLICIT_TYPES = """union
                             { ?y rdf:type ?x }"""

        if hide_base_schemas == False:  # ..then do not filter out XML stuff
            BIT_BASE_SCHEMAS = ""
        if hide_implicit_types == True:  # .. then do not add extra clause
            BIT_IMPLICIT_TYPES = ""

        query = query % (BIT_IMPLICIT_TYPES, BIT_BASE_SCHEMAS)

        # printDebug(query)

        qres = self.rdflib_graph.query(query)
        return list(qres)

    def getClassInstances(self, aURI):
        aURI = aURI
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
                 WHERE {
                     { ?x rdf:type <%s> }
                     FILTER (!isBlank(?x))
                 } ORDER BY ?x
                 """
            % (aURI)
        )
        return list(qres)

    def getClassDirectSupers(self, aURI):
        aURI = aURI
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
                 WHERE {
                     { <%s> rdfs:subClassOf ?x }
                     FILTER (!isBlank(?x))
                 } ORDER BY ?x
                 """
            % (aURI)
        )
        return list(qres)

    # ..................
    # RDF PROPERTIES
    # ..................

    def getAllProperties(self, hide_implicit_preds=True):
        query = """SELECT ?x ?c WHERE {
                        {
                            { ?x a rdf:Property }
                             UNION
                             { ?x a owl:ObjectProperty }
                             UNION
                             { ?x a owl:DatatypeProperty }
                             UNION
                             { ?x a owl:AnnotationProperty }
                             %s
                        } .
                        OPTIONAL  {?x a ?c}
                        FILTER(!isBlank(?x)
                       ) .
                    } ORDER BY	?c ?x
                 """

        BIT_IMPLICIT_PREDICATES = """union
                             { ?a ?x ?b }"""
        if hide_implicit_preds:
            BIT_IMPLICIT_PREDICATES = ""
        query = query % BIT_IMPLICIT_PREDICATES
        # printDebug(query)
        qres = self.rdflib_graph.query(query)
        return list(qres)

    def getPropDirectSupers(self, aURI):
        aURI = aURI
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
                 WHERE {
                     { <%s> rdfs:subPropertyOf ?x }
                     FILTER (!isBlank(?x))
                 } ORDER BY ?x
                 """
            % (aURI)
        )
        return list(qres)

    # ..................
    # SKOS
    # ..................

    def getSKOSInstances(self):
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
                 WHERE {
                     { ?x rdf:type skos:Concept }
                     FILTER (!isBlank(?x))
                 } ORDER BY ?x
                 """
        )
        return list(qres)

    def getSKOSDirectSupers(self, aURI):
        aURI = aURI
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
                 WHERE {
                         {
                             { <%s> skos:broader ?x }
                             UNION
                             { ?x skos:narrower <%s> }
                         }
                     FILTER (!isBlank(?x))
                 } ORDER BY ?x
                 """
            % (aURI, aURI)
        )
        return list(qres)

    # ..................
    # SHACL SHAPES
    # ..................

    def getShapes(self):
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
               WHERE {
                        { ?x a sh:Shape }
                        union
                        { ?x a sh:NodeShape }
                        union
                        { ?x a sh:PropertyShape }
                    } """
        )
        # printDebug(list(qres))
        # sys.exit(0)
        return list(qres)

    # ..................
    # UTILS
    # ..................

    def entityTriples(self, aURI):
        """Builds all triples for an entity
        Note: if a triple object is a blank node (=a nested definition)
        we try to extract all relevant data recursively (does not work with
        sparql endpoins)
        """

        aURI = aURI
        qres = self.rdflib_graph.query(
            """CONSTRUCT {<%s> ?y ?z }
                 WHERE {
                     { <%s> ?y ?z }
                 }
                 """
            % (aURI, aURI)
        )
        lres = list(qres)

        def recurse(triples_list):
            """uses the rdflib <triples> method to pull out all blank nodes info"""
            out = []
            for tripl in triples_list:
                if isBlankNode(tripl[2]):
                    # print "blank node", str(tripl[2])
                    temp = [
                        x for x in self.rdflib_graph.triples((tripl[2], None, None))
                    ]
                    out += temp + recurse(temp)
                else:
                    pass
            return out

        if self.sparql_endpoint:
            return lres
        else:
            try:
                return lres + recurse(lres)
            except:
                printDebug("Error extracting blank nodes info", "important")
                return lres

    # ..................
    # UNUSED OR LEGACY
    # ..................

    def getClassInstancesCount(self, aURI):
        aURI = aURI
        qres = self.rdflib_graph.query(
            """SELECT (COUNT(?x) AS ?count )
                 WHERE {
                     { ?x rdf:type <%s> }
                     FILTER (!isBlank(?x))
                 } ORDER BY ?x
                 """
            % (aURI)
        )
        try:
            return int(list(qres)[0][0])
        except:
            printDebug("Error with <getClassInstancesCount>")
            return 0

    def getClassDirectSubs(self, aURI):
        """
        2015-06-03: currenlty not used, inferred from above
        """
        aURI = aURI
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
                 WHERE {
                     { ?x rdfs:subClassOf <%s> }
                     FILTER (!isBlank(?x))
                 }
                 """
            % (aURI)
        )
        return list(qres)

    def getClassAllSupers(self, aURI):
        """
        note: requires SPARQL 1.1
        2015-06-04: currenlty not used, inferred from above
        """
        aURI = aURI
        try:
            qres = self.rdflib_graph.query(
                """SELECT DISTINCT ?x
                     WHERE {
                         { <%s> rdfs:subClassOf+ ?x }
                         FILTER (!isBlank(?x))
                     }
                     """
                % (aURI)
            )
        except:
            printDebug(
                "... warning: the 'getClassAllSupers' query failed (maybe missing SPARQL 1.1 support?)"
            )
            qres = []
        return list(qres)

    def getClassAllSubs(self, aURI):
        """
        note: requires SPARQL 1.1
        2015-06-04: currenlty not used, inferred from above
        """
        aURI = aURI
        try:
            qres = self.rdflib_graph.query(
                """SELECT DISTINCT ?x
                     WHERE {
                         { ?x rdfs:subClassOf+ <%s> }
                         FILTER (!isBlank(?x))
                     }
                     """
                % (aURI)
            )
        except:
            printDebug(
                "... warning: the 'getClassAllSubs' query failed (maybe missing SPARQL 1.1 support?)"
            )
            qres = []
        return list(qres)

    def getPropAllSupers(self, aURI):
        """
        note: requires SPARQL 1.1
        2015-06-04: currenlty not used, inferred from above
        """
        aURI = aURI
        try:
            qres = self.rdflib_graph.query(
                """SELECT DISTINCT ?x
                     WHERE {
                         { <%s> rdfs:subPropertyOf+ ?x }
                         FILTER (!isBlank(?x))
                     }
                     """
                % (aURI)
            )
        except:
            printDebug(
                "... warning: the 'getPropAllSupers' query failed (maybe missing SPARQL 1.1 support?)"
            )
            qres = []
        return list(qres)

    def getPropAllSubs(self, aURI):
        """
        note: requires SPARQL 1.1
        2015-06-04: currenlty not used, inferred from above
        """
        aURI = aURI
        try:
            qres = self.rdflib_graph.query(
                """SELECT DISTINCT ?x
                     WHERE {
                         { ?x rdfs:subPropertyOf+ <%s> }
                         FILTER (!isBlank(?x))
                     }
                     """
                % (aURI)
            )
        except:
            printDebug(
                "... warning: the 'getPropAllSubs' query failed (maybe missing SPARQL 1.1 support?)"
            )
            qres = []
        return list(qres)

    def getSKOSDirectSubs(self, aURI):
        """
        2015-08-19: currenlty not used, inferred from above
        """
        aURI = aURI
        qres = self.rdflib_graph.query(
            """SELECT DISTINCT ?x
                 WHERE {
                         {
                             { ?x skos:broader <%s> }
                             UNION
                             { <%s> skos:narrower ?s }
                         }
                     FILTER (!isBlank(?x))
                 }
                 """
            % (aURI, aURI)
        )
        return list(qres)


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
