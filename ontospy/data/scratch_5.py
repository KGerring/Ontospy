#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename = namespaces
"""

oboInOwl: hasNarrowSynonym
	hasBroadSynonym
	hasExactSynonym
	oboInOwl:hasDefinition

#     /opt/anaconda3/envs/py39/lib/python3.9/site-packages/linkml_runtime/utils/namespaces.py
#     https://linkml.github.io/linkml-registry/
#lr = https://linkml.github.io/linkml-registry/registry/

#from linkml_registry.registry import SchemaMetadata, SchemaRegistry
#from linkml_registry.evaluate import evaluate
#from linkml_registry.utils import from_csv
#from linkml_registry.markdown_dumper import MarkdownTableDumper, MarkdownPageDumper
#jsonschema/registry.schema.json
#jsonld/registry.context.jsonld
#jsonld/registry.model.context.jsonld
#sqlddl/registry.sql
x
#<a type="application/rss+xml" href="/index.xml" title="RSS" name="RSS">
#http://xmlns.com/foaf/0.1/spec
rdfs/
#https://id.loc.gov/vocabulary/relators.json
	#/vocabulary/identifiers
	#/vocabulary/resourceTypes
	#/vocabulary/resourceComponents
	#/vocabulary/languages
	#/resources/works
	#/authorities/subjects
	#/opensearch/
	#ri="http://id.loc.gov/ontologies/RecordInfo#"
	##"http://id.loc.gov/ontologies/RecordInfo.json"
	##"http://id.loc.gov/ontologies/RecordInfo.rdf"
	#skosxl="http://www.w3.org/2008/05/skos-xl#"
	bflc="http://id.loc.gov/ontologies/bflc/"
	bf="http://id.loc.gov/ontologies/bibframe/"
	
	
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.madsrdf.ttl.json
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.madsrdf.jsonld.json
#https://id.loc.gov/download/vocabulary/relators.madsrdf.jsonld.gz
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.skosrdf.jsonld.json
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.skosrdf.ttl.json


#skos:semanticRelation
#SKOS semantic relations are links between SKOS concepts, where the link is inherent in the meaning of the linked concepts.
	#hierarchical
		#direct: narrower, broader
		#indirect: narrowerTransitive
		
# associative: skos:related, skos:relatedMatch
# skos:closeMatch, skos:exactMatch, skos:broadMatch, skos:narrowMatch and skos:relatedMatch
# skos:closeMatch is used to link two concepts that are sufficiently similar

#skos:example,skos:note,skos:definition
#http://www.w3.org/TR/skos-reference/skos-xl.rdf
##Application%20Profile
#"#Concept%20Scheme"
##Metadata%20Interoperability
#/mediawiki_wiki/Glossary/DCMI_Abstract_Model

from requests_html import HTML
from requests_html import HTMLSession, AsyncHTMLSession

sv = 'http://www.w3.org/TR/spec-variability/'
gl = "http://www.w3.org/2003/glossary/"
qa = 'http://www.w3.org/TR/qa-handbook/
'https://www.w3.org/2003/glossary/subglossary/ATAG10.rdf/'
'https://www.w3.org/2003/glossary/keyword/All/?keywords=accessible%20authoring%20practice'
'https://www.w3.org/2003/glossary/subglossary/ATAG10.rdf/20'
a = https://www.w3.org/2003/glossary/alpha



#/groups/tools/dctools2006/2MetadataGlossary.pdf
/specifications/dublin-core/usageguide/glossary/


# https://github.com/dcmi/ldci
#bibo 	http://purl.org/ontology/bibo/status/> 	The Bibliographic Ontology: Document Status
#cedslrt: 	https://ceds.ed.gov/element/000928# 	CEDS Learning Resource Type
#dc 	http://purl.org/dc/elements/1.1/ 	DCMI Metadata Element Set
#dcterms 	http://purl.org/dc/terms/ 	DCMI Metadata Terms
#loc 	http://id.loc.gov/authorities/genreForms/ 	Library of Congress Genre/Form Terms
#rdf 	http://www.w3.org/1999/02/22-rdf-syntax-ns# 	RDF 1.1 Concepts vocabulary
rdfs 	http://www.w3.org/2000/01/rdf-schema# 	The RDF Schema vocabulary
skos 	http://www.w3.org/2004/02/skos/core# 	Simple Knowledge Organization System
vs 	http://www.w3.org/2003/06/sw-vocab-status/ns# 	SemWeb Vocab Status ontology
#xsd 	http://www.w3.org/2001/XMLSchema# 	XML Schema (datatypes)

#http://purl.org/dc/terms/ 	All DCMI properties, classes and encoding schemes
#http://purl.org/dc/dcmitype/ 	Classes in the DCMI Type Vocabulary
#http://purl.org/dc/dcam/ 	Terms used in the DCMI Abstract Model
#http://purl.org/dc/elements/1.1/ 	The Dublin Core™ Metadata Element Set, Version 1.1 (original 15 elements)


#http://purl.org/dc/dcmitype/Dataset
#http://purl.org/dc/dcmitype/Service
#http://purl.org/dc/dcmitype/Software
#http://purl.org/dc/terms/DCMIType
#bibo.rdf.xml#
#http://owlapi.sourceforge.net
#"https://github.com/owlcs/owlapi/wiki"




rdfs:comment
rdfs:label
<rdfs:seeAlso>http://en.wikipedia.org/wiki/File_format</rdfs:seeAlso>
<rdfs:seeAlso>http://purl.org/biotop/biotop.owl#MachineLanguage</rdfs:seeAlso>
<rdfs:seeAlso>http://www.onto-med.de/ontologies/gfo.owl#Symbol_structure</rdfs:seeAlso>
<rdfs:seeAlso>http://www.ifomis.org/bfo/1.1/snap#Continuant</rdfs:seeAlso>
<rdfs:seeAlso>http://www.loa-cnr.it/ontologies/DOLCE-Lite.owl#quality</rdfs:seeAlso>
<rdfs:seeAlso>"http://purl.org/dc/elements/1.1/format"</rdfs:seeAlso>
<rdfs:seeAlso>http://en.wikipedia.org/wiki/List_of_file_formats</rdfs:seeAlso>
<oboInOwl:hasNarrowSynonym>File format</oboInOwl:hasNarrowSynonym>
 <oboInOwl:hasBroadSynonym>Data model</oboInOwl:hasBroadSynonym>
 <oboInOwl:hasExactSynonym>Exchange format</oboInOwl:hasExactSynonym>
 <oboInOwl:hasExactSynonym>Data format</oboInOwl:hasExactSynonym>
 oboInOwl:hasDefinition
 
 
 'http://edamontology.org/'
 'https://github.com/edamontology/edamontology'
 oboOther: 'http://purl.obolibrary.org/obo/'
 oboInOwl: http://www.geneontology.org/formats/oboInOwl#
 oboContent="http://purl.org/obo/owl/"
 oban="http://purl.org/obo/oban/"
 
 edam: http://purl.obolibrary.org/obo/edam#
 
 

oboInOwl:hasDefinition

Node (s, p, o) subjects,predicates,objects
Identifier
IdentifiedNode
URIRef
Genid
RDFLibGenid
BNode
Literal
Variable



all_nodes
namespace.RDFS.label
namespace.RDFS.comment
RDF.nil


http://edamontology.org/operation
http://edamontology.org/topic
http://edamontology.org/format
http://edamontology.org/data

http://edamontology.org/has_format
http://edamontology.org/has_function
http://edamontology.org/has_identifier
http://edamontology.org/has_input
http://edamontology.org/has_output
http://edamontology.org/has_topic

http://edamontology.org/is_format_of
http://edamontology.org/is_function_of
http://edamontology.org/is_identifier_of
http://edamontology.org/is_input_of
http://edamontology.org/is_output_of
http://edamontology.org/is_topic_of

http://edamontology.org/is_topic_of

http://edamontology.org/documentation
http://edamontology.org/example
http://purl.obolibrary.org/obo/idspace
http://purl.obolibrary.org/obo/is_metadata_tag

http://www.geneontology.org/formats/oboInOwl#hasBroadSynonym
http://www.geneontology.org/formats/oboInOwl#hasDbXref
http://www.geneontology.org/formats/oboInOwl#hasExactSynonym
http://www.geneontology.org/formats/oboInOwl#hasNarrowSynonym
http://www.geneontology.org/formats/oboInOwl#hasRelatedSynonym
http://www.geneontology.org/formats/oboInOwl#hasSubset
http://www.geneontology.org/formats/oboInOwl#inSubset

http://www.w3.org/2000/01/rdf-schema#domain
http://www.w3.org/2000/01/rdf-schema#isDefinedBy
http://www.w3.org/2000/01/rdf-schema#range
http://www.w3.org/2000/01/rdf-schema#seeAlso

"""

#http://www.iana.org/assignments/media-types/application/ld+json
# http://edamontology.org/format_3257
#http://edamontology.org/format_3996
#https://en.wikipedia.org/wiki/Metadata_management
#https://en.wikipedia.org/wiki/Data_management
#http://en.wikipedia.org/wiki/List_of_file_formats
#http://www.iana.org/assignments/media-types/text/csv
#Namespace
#DefinedNamespaceMeta,DefinedNamespace,ClosedNamespace,NamespaceManager,split_uri,insert_trie,insert_strie,get_longest_namespace
#ruleStore = N3RuleStore(additionalBuiltins=additionalBuiltins)
#nsMgr = NamespaceManager(Graph(ruleStore))
#ruleGraph = Graph(ruleStore,namespace_manager=nsMgr)

from __future__ import annotations

import json

import pyRdfa.rdfs
import pyRdfa.rdfs.cache
import pyRdfa.rdfs.process
from linkml_runtime.linkml_model.meta import SchemaDefinition, SlotDefinition
from linkml_runtime.utils.context_utils import parse_import_map
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import URIorCURIE
from linkml_runtime.utils.namespaces import (
    Namespaces,
    base_namespace,
    default_namespace
)

from pyRdfa import (
    CACHE_DIR_VAR,
    ExecutionContext,
    content_to_host_language,
    embeddedRDF,
    preferred_suffixes,
    processURI,
    pyRdfa,
    termorcurie,
    uri_schemes
)
from pyRdfa.extras.httpheader import (
    acceptable_content_type,
    content_type,
    parse_media_type
)
from pyRdfa.host import HostLanguage, MediaTypes, default_vocabulary
from pyRdfa.host import initial_contexts as context_ids
from pyRdfa.initialcontext import initial_context as context_data
from pyRdfa.options import Options
from pyRdfa.rdfs.cache import (
    CachedVocab,
    CachedVocabIndex,
    VocabCachingInfo,
    offline_cache_generation
)
from pyRdfa.rdfs.process import MiniOWL, process_rdfa_sem, return_graph
from pyRdfa.utils import URIOpener, create_file_name, quote_URI

#http://www.w3.org/2007/08/pyRdfa/vocab#
#http://www.w3.org/2007/08/pyRdfa/vocab#VocabCachingInfo
from pyshex.prefixlib import PrefixLibrary, known_prefixes, standard_prefixes
import pyshex.utils.rdf_namespace as rns
from rdflib.namespace import Namespace
from linkml_runtime.utils.yamlutils import YAMLRoot

#id: http://w3id.org/sssom/schema/
#linkml: 'https://w3id.org/linkml/''
#linkml_runtime.utils.schemaview.SchemaView
#linkml_runtime.linkml_model.meta.TypeDefinition
#default_curi_maps'

#read_sssom_table
#skos:broadMatch, owl:subClassOf
#skos:exactMatch owl:equivalentClass
#skos:closeMatch
#skos:narrowMatch inverseOf(owl:subClassOf)
#owl:differentFrom dbpedia-owl:different

SCHEMA_YAML = '/opt/anaconda3/envs/py39/lib/python3.9/site-packages/sssom/sssom.yaml'
linkml_types = 'https://w3id.org/linkml/types.yaml'


class Example:
	value: str
	description: str
	
#URIOpener
#'Accept' : 'text/html;q=0.8, application/xhtml+xml;q=0.8, text/turtle;q=1.0, application/rdf+xml;q=0.9'
#content.content_type == MediaTypes.turtle
#vocabs = set()
#from pyRdfa import RDFA_VOCAB
#v_graph = CachedVocab(uri, options).graph


	
	


ex = [{'value': 'owl:sameAs',
       'description': 'The subject and the object are instances (owl individuals), and the two instances are the same.'},
      {'value': 'owl:equivalentClass',
       'description': 'The subject and the object are classes (owl class), and the two classes are the same.'},
      {'value': 'owl:equivalentProperty',
       'description': 'The subject and the object are properties (owl object, data, annotation properties), and the two properties are the same.'},
      {'value': 'rdfs:subClassOf',
       'description': 'The subject and the object are classes (owl class), and the subject is a subclass of the object.'},
      {'value': 'rdfs:subPropertyOf',
       'description': 'The subject and the object are properties (owl object, data, annotation properties), and the subject is a subproperty of the object.'},
      {'value': 'skos:relatedMatch',
       'description': 'The subject and the object are associated in some unspecified way.'},
      {'value': 'skos:closeMatch',
       'description': 'The subject and the object are sufficiently similar that they can be used interchangeably in some information retrieval applications.'},
      {'value': 'skos:exactMatch',
       'description': 'The subject and the object can, with a high degree of confidence, be used interchangeably across a wide range of information retrieval applications.'},
      {'value': 'skos:narrowMatch',
       'description': 'From the SKOS primer: A triple skos:narrower (and skos:narrowMatch) asserts that , the object of the triple, is a narrower concept than , the subject of the triple.'},
      {'value': 'skos:broadMatch',
       'description': 'From the SKOS primer: A triple skos:broader (and skos:broadMatch) asserts that , the object of the triple, is a broader concept than , the subject of the triple.'},
      {'value': 'oio:database_cross_reference',
       'description': 'Two terms are related in some way. The meaning is frequently consistent across a single set of mappings. Note this property is often overloaded even where the terms are of a different nature (e.g. interpro2go)'},
      {'value': 'rdfs:seeAlso',
       'description': 'The subject and the object are associated in some unspecified way. The object IRI often resolves to a resource on the web that provides additional information.'}]

#"https://github.com/w3c/wpub/tree/master/experiments"
#"https://github.com/w3c/wpub/tree/master/experiments/manifest_script"
#"https://github.com/w3c/wpub/tree/master/experiments/html-schema-org-json-ld"
#"https://github.com/w3c/wpub/tree/master/experiments/separate_manifest"
#"https://github.com/w3c/wpub/tree/master/experiments/w3c_rec"
#"https://github.com/iherman/WPManifest","https://iherman.github.io/WPManifest/webview/"
#"https://github.com/w3c/wpub/tree/master/experiments/toc_generator","https://w3c.github.io/wpub/experiments/toc_generator/"
#"https://github.com/w3c/wpub/edit/main/experiments/README.md
#https://w3c.github.io/wpub/experiments/w3c_rec/simple-canonical.jsonld

# 'http://www.w3.org/2007/rif#',

#   http://www.hixie.ch/specs/pingback/pingback
#   prelo: http://www.w3.org/TR/preload/
#   res http://www.w3.org/TR/resource-hints/
#   web: http://www.w3.org/TR/webmention/
#       https://tools.ietf.org/html/
#       https://www.w3.org/ns/assignments/reg#

am = 'https://www.iana.org/assignments/media-types/application/manifest+json'

class swrl:
	_base =         'https://www.w3.org/Submission/SWRL/'
	root =          'https://www.w3.org/Submission/SWRL'
	example611 =    'https://www.w3.org/Submission/SWRL/example6.1-1.owl'
	example612 =    'https://www.w3.org/Submission/SWRL/example6.1-2.owl'
	ex613 =         'https://www.w3.org/Submission/SWRL/example6.1-3.owl'
	swrlb =         'http://www.w3.org/2003/11/swrlb'
	rdf_schema =    'https://www.w3.org/Submission/SWRL/swrl.rdf'
	owl_onto =      'https://www.w3.org/Submission/SWRL/swrl.owl'
	
	
class xmlowl:
	sc = 'http://www.w3.org/2003/OWL-XMLSchema'
	exslt = "http://exslt.org/common"
	owls = "http://www.w3.org/2003/05/owl-xml"
	oi = 'http://www.w3.org/TR/owl-ref/#imports-def'
	
	


# http://www.w3.org/2003/11/swrlb
owlxml2rdf = "http://www.w3.org/TR/owl-xmlsyntax/owlxml2rdf.xsl"
_owl_xml2rdf = '/Users/kristen/Downloads/owlxml2rdf.xsl'
rif = 'http://www.w3.org/2007/rif'
fn = 'http://www.w3.org/2005/xpath-functions'
pred = 'http://www.w3.org/2007/rif-builtin-predicate'
func = 'http://www.w3.org/2007/rif-builtin-function'
xscd = 'http://www.w3.org/2009/xmlschema-ref'


#service_names_port_numbers.csv

# "http://www.w3.org/2003/11/swrlx"
# "http://www.w3.org/2003/11/ruleml"
# "http://www.w3.org/Submission/2004/SUBM-SWRL-20040521/swrlx.xsd"

#owlx/schema/owl1-dl.xsd, swrlx.xsd,
# ruleml = "http://www.w3.org/Submission/2004/SUBM-SWRL-20040521/ruleml.xsd"
#'http://www.w3.org/2003/OWL-XMLSchema'

owlx =  'http://www.w3.org/2003/05/owl-xml'
OIO = 'http://www.geneontology.org/formats/oboInOwl#'

BIBO = 'http://purl.org/ontology/bibo/'
event = "http://purl.org/NET/c4dm/event.owl#"
status = 'http://purl.org/ontology/bibo/status/'
degrees = 'http://purl.org/ontology/bibo/degrees/'

oslc = 'http://open-services.net/ns/core#'
sshs = 'http://shex.io/shex-semantics'
shextest = 'https://shexspec.github.io/shexTest/'
#https://shexspec.github.io/ns/shex.html
shex = 'https://www.w3.org/ns/shex'


pav1 = 'http://swan.mindinformatics.org/ontologies/1.2/pav/' #Provenance, Authoring and Versioning
#http://pav-ontology.github.io/pav/
#LODE/jquery.js
#"http://www.essepuntato.it/lode/owlapi/http://purl.org/pav/2.2
#https://github.com/pav-ontology/pav/
'http://eelst.cs.unibo.it/apps/LODE/source?url=http://purl.org/pav/2.3'
#pav.rdf.xml
#For resources based on other resources, PAV allows specification of direct retrieval (pav:retrievedFrom), import through transformations (pav:importedFrom) and sources that were merely consulted (pav:sourceAccessedAt). These aspects can also define the agents responsible using pav:retrievedBy, pav:importedBy and pav:sourceAccessedBy
#PAV specializes terms from W3C PROV-O (prov:) and DC Terms (dcterms:), however these ontologies are not OWL imported as PAV can be used independently. The "is defined by" links indicate where those terms are included from. See http://www.w3.org/TR/prov-o and http://dublincore.org/documents/2012/06/14/dcmi-terms/ for more details. See http://purl.org/pav/mapping/dcterms For a comprehensive SKOS mapping to DC Terms

#rdflib_nquads-2013-12-22T192234.ttl
#MF = Namespace("http://www.w3.org/2001/sw/DataAccess/tests/test-manifest#")
#UP = Namespace("http://www.w3.org/2009/sparql/tests/test-update#")
#Namespace("http://www.w3.org/2001/sw/DataAccess/tests/test-query#")

#skosprovider.providers.VocabularyProvider

#http://www.w3.org/2003/06/sw-vocab-status/ns#


'application/sparql-query'

oslc_core = 'http://open-services.net/ns/core#'
oslc_cm = 'http://open-services.net/ns/cm#'
trs = 'http://open-services.net/ns/core/trs#'
trspatch = 'http://open-services.net/ns/core/trspatch#'

'/.well-known/oslc/sp-catalog', ' /.well-known/oslc/rootservices.xml'
osl = 'https://github.com/oslc-op/oslc-specs/blob/master/specs/core/core-vocab.ttl'
OSLC = Namespace('http://open-services.net/ns/core#') #Content-Type
SKOS_THES = Namespace('http://purl.org/iso25964/skos-thes#')

xpath_functions = 'http://www.w3.org/2005/xpath-functions'
schema_for_json = 'https://www.w3.org/TR/xpath-functions/schema-for-json.xsd'
lin = 'https://html.spec.whatwg.org/multipage/links.html'
#'https://html.spec.whatwg.org/multipage/text-level-semantics.html'
#https://html.spec.whatwg.org/multipage/references.html
xh11d="http://www.w3.org/1999/xhtml/datatypes/"
XHTML_NAMESPACE = 'http://www.w3.org/1999/xhtml'
ns = [('ctag', 'http://commontag.org/ns#'),
      ('cc', 'http://creativecommons.org/ns#'),
      ('og', 'http://ogp.me/ns#'),
      ('dc11', 'http://purl.org/dc/elements/1.1/'),
      ('dc', 'http://purl.org/dc/terms/'),
      ('dcterms', 'http://purl.org/dc/terms/'),
      ('gr', 'http://purl.org/goodrelations/v1#'),
      ('qb', 'http://purl.org/linked-data/cube#'),
      ('rev', 'http://purl.org/stuff/rev#'),
      ('v', 'http://rdf.data-vocabulary.org/#'),
      ('void', 'http://rdfs.org/ns/void#'),
      ('sioc', 'http://rdfs.org/sioc/ns#'),
      ('schema', 'http://schema.org/'),
      ('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'),
      ('xhv', 'http://www.w3.org/1999/xhtml/vocab#'),
      ('rdfs', 'http://www.w3.org/2000/01/rdf-schema#'),
      ('xsd', 'http://www.w3.org/2001/XMLSchema#'),
      ('owl', 'http://www.w3.org/2002/07/owl#'),
      ('ical', 'http://www.w3.org/2002/12/cal/icaltzd#'),
      ('grddl', 'http://www.w3.org/2003/g/data-view#'),
      ('skos', 'http://www.w3.org/2004/02/skos/core#'),
      ('time', 'http://www.w3.org/2006/time#'),
      ('vcard', 'http://www.w3.org/2006/vcard/ns#'),
      ('wdr', 'http://www.w3.org/2007/05/powder#'),
      ('wdrs', 'http://www.w3.org/2007/05/powder-s#'),
      ('rif', 'http://www.w3.org/2007/rif#'),
      ('skosxl', 'http://www.w3.org/2008/05/skos-xl#'),
      ('xml', 'http://www.w3.org/XML/1998/namespace'),
      ('foaf', 'http://xmlns.com/foaf/0.1/'),
      ('as', 'https://www.w3.org/ns/activitystreams#'),
      ('duv', 'https://www.w3.org/ns/duv#')]

class dublin:
	"""
	https://www.dublincore.org/specifications/bibo/bibo/
	https://www.dublincore.org/
	https://www.dublincore.org/groups/tools/dctools2006/2MetadataGlossary.pdf
	https://www.dublincore.org/index.xml
	https://www.dublincore.org/resources/glossary/
	https://www.dublincore.org/resources/glossary/metadata_interoperability/
	https://www.dublincore.org/resources/lrmi/
	https://www.dublincore.org/resources/metadata-basics/
	https://www.dublincore.org/resources/userguide/
	https://www.dublincore.org/schemas/xmls/
	https://www.dublincore.org/specifications/
	https://www.dublincore.org/specifications/bibo/
	https://www.dublincore.org/specifications/bibo/bibo/bibo.rdf.xml
	https://www.dublincore.org/specifications/dublin-core/
	https://www.dublincore.org/specifications/dublin-core/dces/
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_abstract_model.ttl
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_elements.ttl
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.nt
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.rdf
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_type.ttl
	https://www.dublincore.org/specifications/dublin-core/usageguide/glossary/
	https://www.dublincore.org/specifications/lrmi

	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/BibliographicResource/
	https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/FileFormat/
	
	
	https://www.dublincore.org/specifications
	"""


class spdx:
	"""
	https://spdx.dev/license-list/matching-guidelines/
	http://www.linuxfoundation.org/terms
	https://spdx.dev/specifications/
	https://spdx.org/
	https://spdx.dev/owl-ontology-20-specification/
	https://spdx.dev/owl-ontology-21-specification/
	https://spdx.dev/spdx-specification-21-web-version/
	http://purl.org/linked-data/cube#
	http://www.w3.org/2006/vcard/ns#
	
	
	
	
	
	
	
	"""
	spec = 'https://spdx.dev/specifications/'
	_ids = 'https://spdx.dev/ids'


earl = 'http://www.w3.org/ns/earl#'

"""
#jsonld/registry.context.jsonld
#jsonld/registry.model.context.jsonld
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.madsrdf.jsonld
#https://id.loc.gov/download/vocabulary/relators.madsrdf.jsonld
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.skosrdf.jsonld
#https://w3c.github.io/wpub/experiments/w3c_rec/simple-canonical.jsonld
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.madsrdf.ttl
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.skosrdf.ttl
osl = 'https://github.com/oslc-op/oslc-specs/blob/master/specs/core/core-vocab.ttl
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_abstract_model.ttl
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_elements.ttl
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl
https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_type.ttl
#adms 	http://www.w3.org/ns/adms# 	Asset Description Metadata Schema
#http://www.w3.org/ns/rdfa#
#'http://www.w3.org/ns/ldp#'
#'http://www.w3.org/ns/oa#',
r2rml = 'http://www.w3.org/ns/r2rml#'
#http://www.w3.org/ns/dx/prof/
#http://www.w3.org/ns/shacl#
shex_ttl =  'http://www.w3.org/ns/shex.ttl'
shex_json = 'http://www.w3.org/ns/shex.jsonld'
ldp = 'http://www.w3.org/ns/ldp#'
sfn = 'http://www.w3.org/ns/sparql#'
FORMATS = Namespace('http://www.w3.org/ns/formats/')
HYDRA = Namespace('http://www.w3.org/ns/hydra/core#')
('csvw', 'http://www.w3.org/ns/csvw#'),
('dcat', 'http://www.w3.org/ns/dcat#'),
('dqv', 'http://www.w3.org/ns/dqv#'),
('ldp', 'http://www.w3.org/ns/ldp#'),
('ma', 'http://www.w3.org/ns/ma-ont#'),
('oa', 'http://www.w3.org/ns/oa#'),
('odrl', 'http://www.w3.org/ns/odrl/2/'),
('org', 'http://www.w3.org/ns/org#'),
('prov', 'http://www.w3.org/ns/prov#'),
('rr', 'http://www.w3.org/ns/r2rml#'),
('rdfa', 'http://www.w3.org/ns/rdfa#'),
('sosa', 'http://www.w3.org/ns/sosa/'),
('sd', 'http://www.w3.org/ns/sparql-service-description#'),
('ssn', 'http://www.w3.org/ns/ssn/'),


"""