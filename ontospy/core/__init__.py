# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
# /Users/kristen/_tmp/Ontospy/ontospy/core/__init__.py

import logging
import os
import sys

from ..VERSION import VERSION
from ..VERSION import __version__
from .ontospy import Ontospy
from .utils import printDebug

logging.basicConfig()

try:
    from configparser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser

try:
    import pickle
except ImportError:
    import pickle as cPickle

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass


# ===========
# ***
# TESTING FLAG : DISABLE CACHING SO TO FORCE RECONSTRUCTION OF GRAPH EACH TIME
# ***
# ===========

GLOBAL_DISABLE_CACHE = False

# ===========
#
# STATIC VARIABLES AND PATHS
#
# ===========

# python package installation
_dirname, _filename = os.path.split(os.path.abspath(__file__))

# local repository constants
ONTOSPY_LOCAL = os.path.join(os.path.expanduser("~"), ".ontospy")

ONTOSPY_LOCAL_CACHE = ONTOSPY_LOCAL + "/.cache/" + VERSION
ONTOSPY_LOCAL_CACHE_TOP = ONTOSPY_LOCAL + "/.cache/"

ONTOSPY_LIBRARY_DEFAULT = ONTOSPY_LOCAL + "/models/"

BOOTSTRAP_ONTOLOGIES = [
    "http://xmlns.com/foaf/spec/",
    "http://purl.org/dc/terms/",
    "http://rdfs.org/sioc/ns#",
    "http://www.w3.org/2008/05/skos#",
    "http://rdfs.org/ns/void#",
    "http://purl.org/goodrelations/v1",
    "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl",
    "http://www.ifomis.org/bfo/1.1",
    #
    # "http://topbraid.org/schema/schema.ttl",
    # "http://www.cidoc-crm.org/rdfs/cidoc_crm_v6.0-draft-2015January.rdfs",
    # "http://purl.uniprot.org/core/",
    # "http://purl.org/spar/cito/",
    # "http://ns.nature.com/terms/",
    # '/Users/kristen/_tmp/Ontospy/ontospy/tests/rdf/scigraph/articles.dds.ttl'
]

# sample endpoints
BOOTSTRAP_ENDPOINTS = [
    "http://dbpedia.org/sparql",
    "http://data.semanticweb.org/sparql",
    "http://linkedgeodata.org/sparql",
    "http://sparql.data.southampton.ac.uk/",
]


import rdflib.namespace, rdflib.extras, rdflib.plugins, rdflib.tools
    #tools
from ontospy.core import actions
from ontospy.core import entities
from ontospy.core import manager
from ontospy.core import namespaces
from ontospy.core import ontospy
from ontospy.core import rdf_loader
from ontospy.core import sparql_helper
from ontospy.core import utils

from ontospy.core.actions import (SOURCE, action_analyze, action_bootstrap,
                                  action_cache_reset, action_erase,
                                  action_import, action_import_folder,
                                  action_jsonld_playground, action_listlocal,
                                  action_reveal_library, action_serialize,
                                  action_update_library_location,
                                  action_visualize, action_webimport,
                                  actions_delete,)
from ontospy.core.entities import (OntoClass, OntoProperty, OntoSKOSConcept,
                                   OntoShape, Ontology, RdfEntity,)
from ontospy.core.manager import (del_pickled_ontology, do_pickle_ontology,
                                  get_home_location, get_localontologies,
                                  get_or_create_home_repo,
                                  get_pickled_ontology, get_random_ontology,
                                  rename_pickled_ontology,)
from ontospy.core.ontospy import (Ontospy,)
from ontospy.core.rdf_loader import (RDFLoader, test,)
from ontospy.core.sparql_helper import (DEFAULT_LANGUAGE, SparqlHelper,)
from ontospy.core.utils import (DEFAULT_LANGUAGE, NAMESPACES_DEFAULT,
                                addQuotes, bcolors, entityComment, entityLabel,
                                firstEnglishStringInList, firstStringInList,
                                get_files_with_extensions, guess_fileformat,
                                inferMainPropertyType, inferNamespacePrefix,
                                inferURILocalSymbol, isBlankNode, is_http,
                                joinStringsInList, list_chunks, niceString2uri,
                                playSound, pprint2columns, pprinttable,
                                printBasicInfo, printDebug, printGenericTree,
                                printInfo, remove_duplicates, safe_str,
                                save_anonymous_gist, shellPrintOverview,
                                slugify, sortByNamespacePrefix,
                                sort_uri_list_by_name, split_list, truncate,
                                try_sort_fmt_opts, uri2niceString,)

__all__ = ['DEFAULT_LANGUAGE', 'NAMESPACES_DEFAULT', 'OntoClass',
           'OntoProperty', 'OntoSKOSConcept', 'OntoShape', 'Ontology',
           'Ontospy', 'RDFLoader', 'RdfEntity', 'SOURCE', 'SparqlHelper',
           'action_analyze', 'action_bootstrap', 'action_cache_reset',
           'action_erase', 'action_import', 'action_import_folder',
           'action_jsonld_playground', 'action_listlocal',
           'action_reveal_library', 'action_serialize',
           'action_update_library_location', 'action_visualize',
           'action_webimport', 'actions', 'actions_delete', 'addQuotes',
           'bcolors', 'del_pickled_ontology', 'do_pickle_ontology', 'entities',
           'entityComment', 'entityLabel', 'firstEnglishStringInList',
           'firstStringInList', 'get_files_with_extensions',
           'get_home_location', 'get_localontologies',
           'get_or_create_home_repo', 'get_pickled_ontology',
           'get_random_ontology', 'guess_fileformat', 'inferMainPropertyType',
           'inferNamespacePrefix', 'inferURILocalSymbol', 'isBlankNode',
           'is_http', 'joinStringsInList', 'list_chunks', 'manager',
           'namespaces', 'niceString2uri', 'ontospy', 'playSound',
           'pprint2columns', 'pprinttable', 'printBasicInfo', 'printDebug',
           'printGenericTree', 'printInfo', 'rdf_loader', 'remove_duplicates',
           'rename_pickled_ontology', 'safe_str', 'save_anonymous_gist',
           'shellPrintOverview', 'slugify', 'sortByNamespacePrefix',
           'sort_uri_list_by_name', 'sparql_helper', 'split_list', 'test',
           'truncate', 'try_sort_fmt_opts', 'uri2niceString', 'utils']
