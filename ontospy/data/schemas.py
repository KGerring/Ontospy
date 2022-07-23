#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename = namespaces
"""






============================  =============================================================
name                          value
============================  =============================================================
ckan_harvester                ckanext.harvest.harvesters:CKANHarvester
dcat                          ckanext.dcat.plugins:DCATPlugin
dcat_json_harvester           ckanext.dcat.harvesters:DCATJSONHarvester
dcat_json_interface           ckanext.dcat.plugins:DCATJSONInterface
dcat_rdf_harvester            ckanext.dcat.harvesters:DCATRDFHarvester
dcat_xml_harvester            ckanext.dcat.harvesters:DCATXMLHarvester
euro_dcat_ap                  ckanext.dcat.profiles:EuropeanDCATAPProfile
harvest                       ckanext.harvest.plugin:Harvest
schemaorg                     ckanext.dcat.profiles:SchemaOrgProfile
structured_data               ckanext.dcat.plugins:StructuredDataPlugin
test_action_harvester         ckanext.harvest.tests.test_action:MockHarvesterForActionTests
test_harvester                ckanext.harvest.tests.test_queue:MockHarvester
test_harvester2               ckanext.harvest.tests.test_queue2:MockHarvester
test_rdf_exception_harvester  ckanext.dcat.tests.test_harvester:TestRDFExceptionHarvester
test_rdf_harvester            ckanext.dcat.tests.test_harvester:TestRDFHarvester
test_rdf_null_harvester       ckanext.dcat.tests.test_harvester:TestRDFNullHarvester
============================  =============================================================


"""
from __future__ import annotations
from collections.abc import Mapping
from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    Iterable,
    Iterator,
    List,
    Mapping,
    Optional,
    Union
)
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

import datasets
from datasets import (
    SCRIPTS_VERSION,
    config,
    get_dataset_config_info,
    get_dataset_config_names,
    get_dataset_infos,
    get_dataset_split_names,
    load_dataset,
    load_from_disk
)
from datasets.builder import BuilderConfig, DatasetBuilder
from datasets.data_files import (
    DataFilesDict,
    DataFilesList,
    Url,
    _get_data_files_patterns,
    resolve_patterns_in_dataset_repository,
    resolve_patterns_locally_or_by_urls
)
from datasets.features import ClassLabel, Features, Value
from datasets.load import (
    dataset_module_factory,
    import_main_class,
    load_dataset
)
from datasets.packaged_modules import _PACKAGED_DATASETS_MODULES
from datasets.utils.download_manager import DownloadConfig, DownloadManager
from datasets.utils.file_utils import (
    DownloadConfig,
    hash_url_to_filename,
    is_remote_url
)
from fsspec.spec import AbstractBufferedFile, AbstractFileSystem
from requests import ConnectionError, HTTPError, Session
from requests.adapters import BaseAdapter, HTTPAdapter
from requests.models import CaseInsensitiveDict, Response
#from requests.models import Response
from requests.packages.urllib3.util.retry import Retry
from requests_cache.models import (
    AnyPreparedRequest,
    AnyRequest,
    AnyResponse,
    CachedRequest,
    CachedResponse,
    Response
)
from requests_cache.session import CachedSession, CacheMixin
from requests_toolbelt.multipart import MultipartEncoder

#https://requests-cache.readthedocs.io/en/stable/
#https://requests-cache.readthedocs.io
from datetime import timedelta
from requests_cache import CachedSession
from requests_cache import CacheMixin, install_cache
from requests_html import HTMLSession, HTML

#ckan.rdf.profiles
#ckan.plugins
#datapackage
#extruct
#hdfscli
#identify-cli
#mc2skos
#ontogram
#pubs
#pyshacl
#csv2rdf
#rdf2dot
#rdfs2dot
#cm2html
#rocrate
#schema-salad-tool
#skosify
#sparqlfun
#sssom
#tableschema


session = None

class CachedHTMLSession(CacheMixin, HTMLSession):
    """
    Session with features from both CachedSession and HTMLSession
    
    >>> session = CachedHTMLSession()
    >>> response = session.get('https://github.com/')
    >>> print(response.from_cache, response.html.links)
    ...
    >>> install_cache(session_factory=CachedHTMLSession)
    >>> response = requests.get('https://github.com/')
    >>> print(response.from_cache, response.html.links)
    """
    
def base_session():
    global session
    session = CachedSession(
        'demo_cache',
        use_cache_dir=True,                # Save files in the default user cache dir
        cache_control=True,                # Use Cache-Control headers for expiration, if available
        expire_after=timedelta(days=1),    # Otherwise expire responses after one day
        allowable_methods=['GET', 'POST'], # Cache POST requests to avoid sending the same data twice
        allowable_codes=[200, 400],        # Cache 400 responses as a solemn reminder of your failures
        ignored_parameters=['api_key'],    # Don't match this param or save it in the cache
        match_headers=True,                # Match all request headers
        stale_if_error=True,               # In case of request errors, use stale cache data if possible
)

class marc:
    niso = "http://www.niso.org"
    marcxml = 'https://www.loc.gov/marcxml'
    base = 'https://www.loc.gov/marc'
    classification = f'{base}/classification'
    bibliographic = f'{base}/bibliographic'
    holdings = f'{base}/holdings'
    community = f'{base}/community'
    specifications = f'{base}/specifications/'
    ex = f'{classification}/examples.html'
    ecc = f'{classification}/eccdmulti.html'
    lang = f'{base}/languages/'
    co = f'{base}/organizations/orgshome.html'
    relators = f'{base}/relators'
    concise = f'{base}/concise/'
    bi_l = f'{bibliographic}/lite/'
    standards =  f'{base}/standards/'
    vl = f'{standards}/valuelist/'
    sl = f'{standards}/sourcelist/'
    mods = 'https://www.loc.gov/mods/'
    mads = 'https://www.loc.gov/standards/mads/'
    

resp = 'https://www.w3.org/Tools/respec/respec-w3c'
'https://www.w3id.org/dpv/primer'


#https://github.com/w3c/respec-web-services/blob/main/static/docs/src.html
#https://www.w3.org/2001/02pd/rec54#, 'content-location=rec54.rdf'
#http://www.w3.org/2001/02pd


#http://www.w3.org/2000/10/swap
#http://www.w3.org/2000/10/swap
#https://www.w3.org/2000/10/swap/pim/contact.rdf
#https://www.w3.org/2000/10/swap/pim/doc.rdf
#https://www.w3.org/2000/10/swap/pim/email.rdf
#https://www.w3.org/2000/10/swap/pim/exif.rdf
#https://www.w3.org/2000/10/swap/pim/ical.rdf
#https://www.w3.org/2000/10/swap/pim/qif.rdf
#https://www.w3.org/2000/10/swap/util/sniffSchema.rdf
#https://www.w3.org/2001/02pd/rec54.rdf
#https://www.w3.org/2001/02pd/rec54.n3
#https://www.w3.org/2001/02pd/rdfs.n3

class csvw:
    """
    
    """
    #'https://w3c.github.io/csvw/use-cases-and-requirements'
    #'https://w3c.github.io/csvw/csv2json/'
    #'https://w3c.github.io/csvw/csv2rdf/'
    #'https://w3c.github.io/csvw/metadata/'
    #'https://w3c.github.io/csvw/primer/'
    #'https://w3c.github.io/csvw/syntax/'
    #'https://w3c.github.io/csvw/use-cases-and-requirements/'

#https://w3c.github.io/did-rubric/
#https://w3c.github.io/dxwg/connegp/
connegp = 'https://w3c.github.io/dx-connegp/'

#https://w3c.github.io/dxwg/dcat/
#https://w3c.github.io/dxwg/dcat/
#https://w3c.github.io/dxwg/dcat/

#https://w3c.github.io/dxwg/prof/
#https://w3c.github.io/dx-prof/

#https://w3c.github.io/dxwg/ucr/
#https://w3c.github.io/dxwg/profiles/


#https://w3c.github.io/its2req/
#https://w3c.github.io/lpf/
#https://w3c.github.io/microdata-rdf/
#https://w3c.github.io/microdata/
#https://w3c.github.io/poe/vocab/


#http://jigsaw.w3.org/rdfpic/
#http://nwalsh.com/docbook/procdiagram/index.html
#http://rdfig.xmlhack.com/index.html
#http://rdfviz.org/
#http://www.graphviz.org/doc/info/attrs.html
#http://www.research.att.com/sw/tools/graphviz/dotguide.pdf


#http://www.w3.org/2001/sw/BestPractices/
#http://lists.w3.org/Archives/Public/spec-prod/
entry="http://www.w3.org/2006/time-entry#"
scv="http://purl.org/NET/scovo#"
time="http://www.w3.org/2006/time#"
intervals = 'http://reference.data.gov.uk/def/intervals/'

#http://www.w3.org/2004/03/thes-tf/primer/
u = 'http://www.ukat.org.uk/thesaurus/concept/1750'
th = 'http://www.ukat.org.uk/thesaurus'
#http://www.w3.org/TR/swbp-skos-core-guide
#http://www.w3.org/2004/02/skos/core/spec/"
#http://spdx.org/rdf/terms

#https://www.w3.org/TR/dx-prof/rdf/prof.ttl #http://www.w3.org/ns/dx/prof
#https://www.w3.org/2017/dxwg/wiki/ProfileContext

schemastore = 'https://json.schemastore.org/schema-catalog.json'
wdrs = 'http://www.w3.org/2007/05/powder-s#'
dbp_defs = "http://dbpedia.org/ontology/data/definitions.ttl"
jsod = "http://dbpedia.org/data3/data/definitions.ttl.jsod"
atom = "http://dbpedia.org/data3/data/definitions.ttl.atom"
drdf = "http://dbpedia.org/data3/data/definitions.ttl.rdf"

dbo = "http://dbpedia.org/ontology/"
#http://mappings.dbpedia.org/index.php/OntologyProperty:


ns1 = 'http://www.openlinksw.com/'
ns5 = 'http://dbpedia.org/ontology/School/'
mads_xsl = 'https://www.loc.gov/standards/mads/v2/mads-2-1.xsd'


cwl = 'https://w3id.org/cwl/view'

wsdl_rdf = 'http://www.w3.org/ns/wsdl-rdf#'

solid = 'http://www.w3.org/ns/solid/terms#'
r2rml = 'http://www.w3.org/ns/r2rml#'
odrl = ('http://www.w3.org/ns/odrl/2/', 'http://www.w3.org/ns/odrl/2/ODRL22.ttl')
ontolex = 'http://www.w3.org/ns/lemon/ontolex#'
ldp= 'http://www.w3.org/ns/ldp#'
dprof = 'https://www.w3.org/TR/dx-prof/rdf/prof.ttl'
uwa = 'http://www.w3.org/2007/uwa/context/common.owl#'
genont = 'http://www.w3.org/2006/gen/ont#'
nif="http://persistence.uni-leipzig.org/nlp2rdf/ontologies/nif-core#"
itsrdf="http://www.w3.org/2005/11/its/rdf#"
ui="http://www.w3.org/ns/ui#"
flow = "http://www.w3.org/2005/01/wf/flow#"
role="http://www.w3.org/2005/01/wai-rdf/GUIRoleTaxonomy#"
rddl = 'http://www.w3.org/2003/g/data-view#'
'http://www.w3.org/2000/08/w3c-synd/'
'http://www.w3.org/2001/sw-grddl-wg/'
dcextract = 'http://www.w3.org/2000/06/dc-extract/dc-extract.xsl'
p3prdfv1 = 'http://www.w3.org/2002/01/p3prdfv1#' #p3prdfv1.xml
bookmark = 'http://www.w3.org/2002/01/bookmark#'
annotation_ns = 'http://www.w3.org/2000/10/annotation-ns#'

#http://www.re3data.org/schema/3-0#

rda = 'http://www.rdaregistry.info/'
provbook = 'http://www.provbook.org/ns/#'
virtrdf = 'http://www.openlinksw.com/virtrdf-data-formats'

#http://www.ontotext.com/owlim/lucene#
#http://www.lido-schema.org/
#http://www.bigdata.com/rdf#
#http://wiktionary.dbpedia.org/terms/
#http://wikipedia.no/rdf/
#http://wifo-ravensburg.de/semanticweb.rdf#

metadataregistry = 'http://metadataregistry.org/vocabulary/list.html'


nkos = 'http://w3id.org/nkos#'
nkos_rdf = 'http://nkos.dublincore.org/nkos.rdf'
nkostype = 'http://nkos.dublincore.org/nkostype/nkostype.rdf'
nkos_ap = 'https://nkos.dublincore.org/nkos-ap.html'
lov = 'http://lov.okfn.org/dataset/lov'


biolink = ('http://w3id.org/biolink/vocab/',
          'https://biolink.github.io/biolink-model/docs/')

getty = 'http://vocab.getty.edu/ontology#'
vivoweb = 'http://vivoweb.org/ontology/core#'
study_protocol="http://purl.org/net/OCRe/study_protocol.owl#"
geopolitical="http://aims.fao.org/aos/geopolitical.owl#"
vitro="http://vitro.mannlib.cornell.edu/ns/vitro/0.7#"
obo="http://purl.obolibrary.org/obo/"
statistics="http://purl.org/net/OCRe/statistics.owl#"
doap="http://usefulinc.com/ns/doap#"
# #Project
lov_voc = 'https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/list'
#http://topbraid.org/tosh#
#http://swtmp.gitlab.io/vocabulary/templates.owl#
#http://sites.wiwiss.fu-berlin.de/suhl/bizer/d2r-server/config.rdf#
reg="http://metadataregistry.org/uri/profile/regap/"

#http://rdf-vocabulary.ddialliance.org/xkos#
#http://purl.org/rss/1.0/modules/content/
#http://purl.org/linked-data/sdmx#

# http://protege.stanford.edu/plugins/owl/dc/protege-dc.owl#
#http://lexvo.org/ontology#
#http://identifiers.org/


#http://id.loc.gov/vocabulary/relators/
#http://id.loc.gov/vocabulary/iso639-1/
#http://id.loc.gov/vocabulary/graphicMaterials/
#http://edamontology.org/
dcx = 'http://dublincore.org/dcx/'
xrd = 'http://docs.oasis-open.org/ns/xri/xrd-1.0#'
#http://bioentity.io/vocab/
bio2rdf = 'http://bio2rdf.org/core#'
bibliograph = 'http://bibliograph.net/schemas/'

#http://bibframe.org/vocab/        #www.loc.gov/bibframe/implementation,www.loc.gov/bibframe/docs
marc2bibframe2 = 'https://github.com/lcnetdev/marc2bibframe2'
bibframe2marc = 'https://github.com/lcnetdev/bibframe2marc'


#http://assemblee-virtuelle.github.io/grands-voisins-v2/thesaurus.ttl#
oc = 'https://w3id.org/oc/corpus/context.json'
wdrs = 'http://www.w3.org/2007/05/powder-s#'
adms = 'http://www.w3.org/ns/adms'
'http://www.w3.org/ns/adms.rdf'
'http://www.w3.org/ns/adms.ttl'
'http://www.w3.org/TR/vocab-adms'
'http://www.w3.org/TR/vocab-dcat/'




#'http://www.w3.org/2001/sw/DataAccess/tests/test-query#'
#https://linkml.github.io/linkml-registry/registry/

#http://www.sparontologies.net/ontologies/fr
#http://bibliontology.com
#http://www.w3.org/ns/oa.ttl
#http://www.openannotation.org/spec/core/
#http://www.openannotation.org/spec/tutorial/
#http://www.w3.org/community/openannotation/wiki/Cookbook

#http://www.openannotation.org/spec
#https://www.w3.org/TR/annotation-model/
#https://www.w3.org/TR/annotation-vocab/
#https://www.w3.org/TR/annotation-protocol/
#https://www.w3.org/TR/annotation-vocabulary/

#https://github.com/sparontologies/cito
#http://purl.org/spar/cito.ttl
#http://purl.org/spar/cito.json
#https://w3id.org/spar/cito

#https://w3id.org/oc/index/api/v1
#https://w3id.org/oc/index

#https://specs.frictionlessdata.io/

#http://www.w3.org/ns/csvw#; http://www.w3.org/ns/csvw.jsonld
#http://www.w3.org/TR/tabular-metadata

#https://www.w3.org/2002/01/tr-automation/
#https://id.loc.gov/ontologies/madsrdf/v1.json
mi = 'https://www.dublincore.org/resources/glossary/metadata_interoperability/'
#https://www.dublincore.org/resources/glossary/



#https://www.w3.org/TR/skos-reference/#schemes
skos = 'http://www.w3.org/TR/skos-reference/skos.rdf'
#https://www.loc.gov/standards/mods/modsrdf/v1/modsrdf.owl
#http://www.w3.org/TR/skos-reference/
#http://www.w3.org/2008/05/skos-xl
#http://www.w3.org/TR/skos-ucr
#http://www.w3.org/TR/swbp-vocab-pub/


#http://www.w3.org/2001/sw/DataAccess/tests/test-manifest
#http://www.w3.org/2000/10/rdf-tests/rdfcore/Manifest.rdf

_test="http://www.w3.org/2000/10/rdf-tests/rdfcore/testSchema.rdf"

#https://www.w3.org/Consortium/siteindex.html
#http://www.w3.org/2001/sw/DataAccess/tests/test-dawg#
#ttps://www.dublincore.org/resources/glossary/competency_index/  #https://dcmi.github.io/ldci

sru = "http://www.loc.gov/standards/sru/"

ri="http://id.loc.gov/ontologies/RecordInfo.rdf"

#http://www.w3.org/ns/prov.ttl #Activity; http://www.w3.org/ns/prov.owl
#http://id.loc.gov/resources/hubs.rdf
#http://id.loc.gov/resources/instances.rdf
#http://id.loc.gov/resources/works.rdf
#https://lds-downloads.s3.amazonaws.com/vocabulary/relators.skosrdf.jsonld.json

#https://id.loc.gov/vocabulary/relators.skos.json
#https://id.loc.gov/vocabulary/relators.madsrdf.json
#https://id.loc.gov/vocabulary/relators.json
#https://id.loc.gov/vocabulary/marcgt.json
# cs="http://www.w3.org/2003/06/sw-vocab-status/ns#
#https://id.loc.gov/vocabulary/nationalbibschemes.json
#https://id.loc.gov/vocabulary/nationalbibschemes.madsrdf.json
#https://id.loc.gov/vocabulary/nationalbibschemes.skos.json

#http://www.w3.org/2004/02/skos/core#ConceptScheme
#http://id.loc.gov/ontologies/premis.json
#https://id.loc.gov/ontologies/madsrdf/v1.json
#https://id.loc.gov/ontologies/bibframe.json
#https://id.loc.gov/ontologies/bflc.json

#http://id.loc.gov/vocabulary/resourceTypes.json
#https://id.loc.gov/vocabulary/relators.json
#https://id.loc.gov/resources/instances.json

#http://id.loc.gov/authorities/subjects.rdf
#http://id.loc.gov/authorities/subjects.nt
#http://id.loc.gov/authorities/subjects
#http://id.loc.gov/authorities/subjects.json

bflc="http://id.loc.gov/ontologies/bflc/"


#http://bibliograph.net/schemas/
jldctx = 'application/x-json+ld+ctx'

class bio2rdf:
    rep = "http://github.com/bio2rdf/bio2rdf-scripts/wiki/Query-repository"
    dl = "http://download.bio2rdf.org"
    data = "http://download.bio2rdf.org/files/release/3/release.html"
    about = "http://github.com/bio2rdf/bio2rdf-scripts/wiki"
    
class mod:
    xsl = 'https://www.loc.gov/standards/mods/modsrdf/xsl-files/modsrdf.xsl'
    primer = 'http://www.loc.gov/standards/mods/modsrdf/primer.html'

modsrdf = 'http://www.loc.gov/standards/mods/modsrdf/index.html'
modsx = 'http://www.loc.gov/standards/mods/mods.xsd'

bibframe = 'https://id.loc.gov/ontologies/bibframe.rdf'

modsrdf = 'http://www.loc.gov/mods/modsrdf/v1/modsrdf.owl'
classSchemes="http://id.loc.gov/vocabulary/classSchemes/"
targetAudiences="http://id.loc.gov/vocabulary/targetAudiences/"
madsrdf="http://www.loc.gov/mads/rdf/v1#"
j="http://www.loc.gov/mods/rdf/"
identifiers="http://id.loc.gov/vocabulary/identifiers/"
access="http://id.loc.gov/vocabulary/access#"
note="http://id.loc.gov/vocabulary/note#"
resourceTypes="http://id.loc.gov/vocabulary/resourceTypes/"
abstract="http://id.loc.gov/vocabulary/abstract#"
ri="http://id.loc.gov/ontologies/RecordInfo#"
cs = 'http://id.loc.gov/ontologies/ClassificationSchemes'
rt = 'http://id.loc.gov/ontologies/ResourceTypes'
css = 'http://purl.org/vocab/changeset/schema'
change = 'http://vocab.org/changeset/'
roles = 'http://id.loc.gov/ontologies/Roles'

mads = 'http://www.loc.gov/standards/mads/rdf/v1.rdf' #Metadata Authority
bf="http://id.loc.gov/ontologies/bibframe/"
bflc="http://id.loc.gov/ontologies/bflc/"
iso25964 = 'https://www.niso.org/schemas/iso25964'
reg = 'http://purl.org/linked-data/registry#'
reg_ = "https://raw.githubusercontent.com/ukgovld/registry-core/master/src/main/vocabs/registryVocab.ttl"

ldp = 'http://www.w3.org/ns/ldp'
#http://www.w3.org/ns/ldp#, 'http://www.w3.org/ns/ldp.html', 'ldp.ttl',
rdfa = 'http://www.w3.org/ns/rdfa#'