#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename = namespaces
from __future__ import annotations

from html import unescape, escape

from html2txt.parsers import (
    ETreeHTMLParser,
    HTMLParser,
    etreehtmlparser,
    parser,
    xmlfragmentparser
)
from html2txt.parsers.common import escape_html, escape_url
from rdflib import RDF, Graph, Namespace

#blis
#bioregistry

DCAT =       Namespace('http://www.w3.org/ns/dcat#')
R3D =        Namespace('http://www.re3data.org/schema/3-0#')
SI =        'http://www.w3.org/Consortium/siteindex.html'
specberus = 'http://www.w3.org/pubrules/js/specberus.js'
fixup =     'http://www.w3.org/scripts/TR/2016/fixup.js'

okfn = 'http://index.okfn.org/'
lod = 'http://lod-cloud.net/'
#https://lod-cloud.net/datasets
#https://lod-cloud.net/lod-data.json
#https://lod-cloud.net/add-dataset
#http://www.w3.org/DesignIssues/LinkedData.html
#http://lod-cloud.net

lov = 'http://lov.okfn.org'
pav = 'http://purl.org/pav/'
gtfs = 'http://vocab.gtfs.org/terms#' 'http://vocab.gtfs.org/gtfs.ttl'
iso = 'http://www.niso.org/schemas/iso25964/'
ldqd = 'https://www.w3.org/2016/05/ldqd#'
#https://github.com/owlcs/owlapi/
#http://fairreviews.linkeddata.es/def/core/ontology.ttl #https://w3id.org/fr/def/core

#http://purl.org/spar/fabio/Manifestation

#https://w3id.org/fr/def/core#
#http://www.sparontologies.net/uptake

#http://purl.org/spar/cito.xml. http://purl.org/spar/cito.ttl, http://purl.org/spar/cito.json, http://purl.org/spar/cito.html

#http://xmlns.com/foaf/spec/
#http://patterns.dataincubator.org/book/qualified-relation.html
#http://schema.theodi.org/odrs
#http://ns.inria.fr/l4lod/v2/l4lod_v2.html
#http://ns.inria.fr/l4lod/v1/l4lod_v1.html
#http://ns.inria.fr/l4lod/v1/l4lod_v1.rdf'
#http://ns.inria.fr/l4lod/v2/l4lod_v2.rdf

#http://schema.theodi.org/odrs/index.ttl
#http://vocab.org/waiver/terms/declaration
#http://vocab.org/waiver/terms/.html

vann = 'http://vocab.org/vann'
#http://www.w3.org/2011/gld/
#http://www.w3.org/ns/dcat
#http://xmlns.com/foaf/0.1
#https://w3c.github.io/dxwg/dcat/rdf/dcat-schema.ttl

#https://w3id.org/
#https://www.w3.org/TR/vocab-dcat
#https://www.w3.org/TR/vocab-duv/
#'http://www.w3.org/TR/vocab-org/
#http://www.w3.org/TR/vocab-data-cube/
#http://www.w3.org/TR/vocab-adms/
#http://www.w3.org/2007/05/powder-s
#http://www.w3.org/ns/adms.ttl
#https://www.w3.org/TR/vocab-duv/
#https://www.w3.org/TR/tabular-metadata
#https://www.w3.org/TR/sdw-bp/
#https://www.w3.org/TR/prov-o/
#https://www.w3.org/2004/01/pp-impl/68239/status

#https://www.w3.org/TR/odrl-model/
#https://www.w3.org/TR/ld-bp/#VOCABULARIES
#http://www.w3.org/ns/duv
#https://www.w3.org/TR/dwbp/dwbp-example.ttl
#https://www.w3.org/TR/dwbp/diff
#https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.11
#http://purl.org/dc/terms/title
#http://purl.org/spar/fabio

dd = 'https://ddialliance.org/'

CASRAI = 'https://casrai.org/rdm-glossary/'

xkos = 'https://github.com/linked-statistics/xkos/blob/master/xkos.html'
xk = 'http://purl.org/linked-data/xkos'
dd = 'http://rdf-vocabulary.ddialliance.org/discovery.ttl'
#http://www.essepuntato.it/lode/owlapi/ https://raw.github.com/linked-statistics/disco-spec/master/discovery.ttl

#https://www.dublincore.org/specifications/bibo/
#http://www.w3.org/TR/annotation-html/
#https://www.w3.org/TR/annotation-vocab/
#http://www.w3.org/TR/annotation-protocol/
#http://www.w3.org/TR/annotation-model/

#https://www.w3.org/annotation/v1/annotation_frame.jsonld  #http://www.w3.org/ns/anno.jsonld
#https://www.w3.org/annotation/v1/collection_frame.jsonld [http://www.w3.org/ns/anno.jsonld ,http://www.w3.org/ns/ldp.jsonld]
#https://www.w3.org/annotation/v1/page_frame.jsonld
#http://www.w3.org/ns/anno.jsonld

#https://w3id.org/lode
#http://www.essepuntato.it/graffoo
#http://www.sparontologies.net
#http://www.sparontologies.net/examples
#http://www.sparontologies.net/ontologies

#datacite,fivestars,fr,frapo,frbr,pro,scoro
#http://purl.org/spar/biro.ttl
#http://purl.org/spar/cito.ttl
#http://purl.org/cerif/frapo.ttl
#http://purl.org/spar/fabio
#http://purl.org/spar/frbr
#http://purl.org/spar/frbr -> https://sparontologies.github.io/frbr/current/frbr.html
#http://purl.org/vocab/frbr/core#

#http://prismstandard.org/namespaces/basic/2.0/
#http://www.niso.org/apps/group_public/project/

frbr = 'http://purl.org/spar/frbr/'
core = 'http://purl.org/vocab/frbr/core#'
tvc = 'http://www.essepuntato.it/2012/04/tvc/'
co = 'http://purl.org/co/'
owlapi = 'http://www.semanticweb.org/owlapi#'
cio = 'http://purl.org/spar/cito/'
datacite = 'http://purl.org/spar/datacite/'
cerif = 'http://purl.org/cerif/'
cwerro = 'http://purl.org/cerif/cerro/'
foaf = 'http://xmlns.com/foaf/0.1/'
frapo = 'http://purl.org/cerif/frapo/'
waiver="http://vocab.org/waiver/terms/"
vs="http://www.w3.org/2003/06/sw-vocab-status/ns#"
omv="http://omv.ontoware.org/2005/05/ontology#"
premis="http://multimedialab.elis.ugent.be/users/samcoppe/ontologies/Premis/premis.owl#"
voag="http://voag.linkedmodel.org/schema/voag#"
nie="http://www.semanticdesktop.org/ontologies/2007/01/19/nie#"
gr="http://purl.org/goodrelations/v1#"
meb="http://rdf.myexperiment.org/ontologies/base/"
odrl="http://w3.org/ns/odrl/vocab#"
o="http://w3.org/ns/odrl/2/"
limo="http://purl.org/LiMo/0.1/"
csvw = 'http://w3.org/ns/csvw.jsonld'

#http://www.sparontologies.net/ontologies/c4o
#http://www.sparontologies.net/ontologies/datacite
#http://www.sparontologies.net/ontologies/fabio
#http://www.sparontologies.net/ontologies/frapo


#http://www.sparontologies.net/ontologies/frbr
#http://www.sparontologies.net/uptake

#https://github.com/sparontologies/cito/
#http://www.sparontologies.net/ontologies/cito

#https://w3id.org/fr/def/core#
#https://w3id.org/un/ontology/undo
#https://www.datacite.org
#http://opencitations.net/
#http://pubchem.ncbi.nlm.nih.gov/rdf/
#http://vocab.org/review/terms.html


#https://github.com/opencitations/metadata/
#https://w3id.org/oc/ontology




bp =        'http://www.w3.org/TR/dwbp/'
bp_s =      'http://www.w3.org/TR/sdw-bp/'
d_bp =      'http://www.w3.org/TR/vocab-dqv/'
SKOS =      'http://www.w3.org/2001/sw/wiki/SKOS'
guide =     'http://www.w3.org/Guide/'
trdoc2rdf = 'http://www.w3.org/2001/10/trdoc2rdf'
datacite =  'https://schema.datacite.org/meta/kernel-4.4/metadata.xsd'
checklink = 'http://validator.w3.org/checklink'
vc =        'https://w3c.github.io/vc-data-model/'
tidy =      'http://cgi.w3.org/cgi-bin/tidy'

class schemastore:
	url = 'https://www.schemastore.org/api/json/catalog.json'
	csvw = 'http://w3.org/ns/csvw.jsonld'


class dxprof:
	"""
	www.w3.org/ns/dx/prof/ResourceRole
	"http://www.w3.org/TR/dx-prof/rdf/prof.ttl"
	http://www.w3.org/ns/dx/prof/profilesont.ttl
	http://www.w3.org/TR/dx-prof/alignments/skos.ttl
	http://www.w3.org/TR/dx-prof/alignments/voaf.ttl
	
	http://www.w3.org/ns/dx/prof/
	https://w3c.github.io/dxwg/prof/
	https://w3c.github.io/dxwg/profiles/
	https://w3c.github.io/dxwg/profilesont/
	https://www.w3.org/TR/dx-prof-conneg/
	https://www.w3.org/TR/dx-prof/
	https://www.w3.org/ns/dx/prof/
	"""
	dx_prof =   'http://www.w3.org/TR/dx-prof/'
	prof_ttl =  'http://www.w3.org/TR/dx-prof/rdf/prof.ttl'
	prof =      'http://www.w3.org/ns/dx/prof/'
	role =      'http://www.w3.org/ns/dx/prof/role/'
	role_ttl =  'http://www.w3.org/ns/dx/prof/role/index.ttl'
	
	href="http://www.w3.org/StyleSheets/TR/2016/W3C-WG-NOTE.css"
	ucr = 'http://www.w3.org/TR/dcat-ucr/'
	cr = 'https://github.com/CSIRO-enviro-informatics/prof-ont-implementation-results'
	dcap = 'http://dublincore.org/documents/profile-guidelines/'
	profiles = 'https://w3c.github.io/dxwg/profiles/'
	modspec = 'http://www.opengeospatial.org/standards/modularspec'
	odrl_voc = 'http://www.w3.org/TR/odrl-vocab/'


#http://www.opengeospatial.org/standards/modularspec
#http://www.opengeospatial.org/standards/cat
#http://www.w3.org/2002/06/rdfs2html.xsl
#http://www.openrdf.org/schema/sesame#
#http://www.opengis.net/def/metamodel/ogc-na/
#http://www.opengis.net/defs/crossrefs/specrelations
#http://www.opengis.net/def
#http://www.w3.org/ns/dx/connegp/profile/
#cnpr:http     http://www.w3.org/ns/dx/connegp/profile/
#cnpr:qsa
#cnpr:qsa-alt
#cnpr:rrd -> https://w3c.github.io/dx-connegp/connegp/#getresourcebyprofile
#   http://www.w3.org/ns/dx/connegp/altr
#   http://www.w3.org/ns/adms
#   https://www.w3.org/Protocols/rfc2616/rfc2616-sec12.html
#   https://www.w3.org/2001/tag/issues.html#httpRange-14
#   https://www.w3.org/TR/dx-prof-conneg/
#   https://www.opengis.net/def/appschema/hy_features/hyf/HY_HydroFeature
#   https://www.opengeospatial.org/projects/initiatives/databio



class ontobio:
	'''
	https://ontobio.readthedocs.io/en/latest/
	https://ontobio.readthedocs.io/en/latest/quickstart.html#python
	https://ontobio.readthedocs.io/en/latest/outputs.html#json-output
	https://ontobio.readthedocs.io/en/latest/inputs.html#remote-association-access-via-golr
	https://ontobio.readthedocs.io/en/latest/inputs.html#local-json-ontology-files
	https://ontobio.readthedocs.io/en/latest/commandline.html#ontologies
	https://ontobio.readthedocs.io/en/latest/api.html#ontology-access
	https://github.com/biolink/ontobio
	
	https://www.w3.org/TR/dwbp/#challenges
	https://www.w3.org/TR/tabular-data-primer/
	https://www.w3.org/TR/vocab-duv/
	https://www.w3.org/TR/vocab-dqv/
	https://www.w3.org/TR/dwbp/#distribution
	#https://www.w3.org/TR/dwbp/#dataset
	#https://www.w3.org/TR/dwbp/#data_consumer
	#https://lod-cloud.net/
	
	https://github.com/topics/annotation
	https://github.com/topics/json-ld
	
	http://www.w3.org/ns/oa.ttl
	http://www.w3.org/ns/oa.jsonld
	http://www.w3.org/TR/annotation-vocab/
		https://www.w3.org/annotation/v1/annotation_frame.jsonld
		https://www.w3.org/annotation/v1/collection_frame.jsonld
		https://www.w3.org/annotation/v1/page_frame.jsonld
		https://www.w3.org/TR/activitystreams-core/
		https://www.w3.org/TR/activitystreams-vocabulary/
		
		https://lists.w3.org/Archives/Public/public-annotation/
		http://www.w3.org/ns/activitystreams#totalItems
		http://www.w3.org/ns/activitystreams#partOf
		http://www.w3.org/ns/activitystreams#generator
		http://www.w3.org/ns/activitystreams#Application
		http://www.w3.org/TR/annotation-vocab/diff.html
		http://www.w3.org/TR/annotation-vocab/annotation-vocab.epub
		
		
		http://www.w3.org/TR/annotation-protocol/
		http://www.w3.org/TR/annotation-model/
		http://w3c.github.io/web-annotation/
		
		http://www.openannotation.org/spec/core
		
		https://w3c.github.io/test-results/annotation-vocab/README.md
		http://w3c.github.io/test-results/annotation-vocab/all.html
		http://schema.org/SoftwareApplication
		http://schema.org/Dataset
		
		http://json-ld.org/spec/latest/json-ld-framing/
		http://getty.edu/
		
	https://github.com/w3c/web-annotation
	
	
	
	'''
##
class fair:
	'''
	#http://www.obofoundry.org/
	#http://geneontology.org/docs/download-go-annotations/
	#http://geneontology.org/docs/download-ontology/
	#http://geneontology.org/docs/downloads/
	https://github.com/orgs/owlcs/packages?repo_name=owlapi
	
	https://github.com/owlcs/owlapi
	
	
	https://github.com/oboformat/oboformat-tools
	https://github.com/geneontology/obographs/
	http://owlcollab.github.io/oboformat/doc/obo-syntax.html
	http://www.bioontology.org/wiki/index.php/OboInOwl:Main_Page
	https://www.bioontology.org/wiki/Glossary
	http://purl.obolibrary.org/obo/ro.owl
	http://owlcollab.github.io/
	
	https://theodi.org/guides/marking-up-your-dataset-with-dcat
	http://www.nf.mpg.de/vinci3/doc/image-formats.html
	http://www.geneontology.org/
	http://isa-tools.org/
	http://go-fair.org/go-fair-initiative/
	https://www.go-fair.org/resources/go-fair-materials/materials-for-ins/
	https://www.go-fair.org/resources/glossary/
	https://www.go-fair.org/events/
	https://www.dtls.nl/fair-data/find-fair-data-tools/
	http://www.go-fair.org
	http://go-fair.org/go-fair-initiative/
	https://www.go-fair.org/resources/
	https://www.go-fair.org/how-to-go-fair/
	https://www.go-fair.org/go-fair-initiative/
	https://github.com/peta-pico/FAIR-nanopubs/blob/master/principles.ttl
	https://www.go-fair.org/fair-principles/
	https://www.go-fair.org/fair-principles/542-2/
	https://www.go-fair.org/fair-principles/a1-1-protocol-open-free-universally-implementable/
	https://www.go-fair.org/fair-principles/a1-2-protocol-allows-authentication-authorisation-required/
	https://www.go-fair.org/fair-principles/a2-metadata-accessible-even-data-no-longer-available/
	https://www.go-fair.org/fair-principles/f1-meta-data-assigned-globally-unique-persistent-identifiers/
	https://www.go-fair.org/fair-principles/f2-data-described-rich-metadata/
	https://www.go-fair.org/fair-principles/f3-metadata-clearly-explicitly-include-identifier-data-describe/
	https://www.go-fair.org/fair-principles/f4-metadata-registered-indexed-searchable-resource/
	https://www.go-fair.org/fair-principles/fair-data-principles-explained/f1-meta-data-assigned-globally-unique-persistent-identifiers/
	https://www.go-fair.org/fair-principles/fair-data-principles-explained/f2-data-described-rich-metadata/
	https://www.go-fair.org/fair-principles/fairification-process/
	https://www.go-fair.org/fair-principles/i1-metadata-use-formal-accessible-shared-broadly-applicable-language-knowledge-representation/
	https://www.go-fair.org/fair-principles/i2-metadata-use-vocabularies-follow-fair-principles/
	https://www.go-fair.org/fair-principles/i3-metadata-include-qualified-references-metadata/
	https://www.go-fair.org/fair-principles/metadata-retrievable-identifier-standardised-communication-protocol/
	https://www.go-fair.org/fair-principles/r1-1-metadata-released-clear-accessible-data-usage-license/
	https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/
	https://www.go-fair.org/fair-principles/r1-3-metadata-meet-domain-relevant-community-standards/
	https://www.go-fair.org/fair-principles/r1-metadata-richly-described-plurality-accurate-relevant-attributes/
	
	'''

#https://www.ogc.org/domain/university_and_research
#https://www.ogc.org/domain/defense_and_intel


class vocprez:
	"""
	@id: http://github.com/rdflib/VocPrez
	@version: https://github.com/RDFLib/VocPrez/releases/tag/2.5.9
	
	https://www.go-fair.org/fair-principles
	https://portal.opengeospatial.org/
	http://www.opengis.net/def/glossary
	http://www.opengis.net/def/function/geosparql
	http://www.ogcapi.org
	http://www.locationpowers.net
	http://ogc.standardstracker.org/
	
	http://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/docs/03-003r10
	https://www.ogc.org/ogc/
	https://www.ogc.org/about
	https://www.ogc.org/def-server
	https://www.ogc.org/ogc/join
	https://www.ogc.org/ogc/guidanceltr
	https://www.ogc.org/ogc/programs/ip
	https://www.ogc.org/ogc/regions
	https://www.ogc.org/standards
	https://www.ogc.org/standards/community
	
	https://www.ogc.org/pressroom
	https://www.ogc.org/domain/domain_summaries
	
	https://www.ogc.org/projects/groups
	https://www.ogc.org/resource/products
	https://www.ogc.org/resource/products/stats
	https://www.ogc.org/roadmap
	
	#http://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/metamodel/ogc-na/&_mediatype=text/turtle
	400: The object with URI http://www.opengis.net/def/metamodel/ogc-na/ is not of type skos:ConceptScheme, skos:Collection or
	skos:Concept and only these classes of object are understood by VocPrez
	
    <div id="vp-menu"><span>Definitions Server</span>
		<a href="/vocprez/">Home</a>
		<a href="/vocprez/search">Search</a>
		<a href="/vocprez/vocab/">Browse Vocabularies</a>
		<a href="http://ogc.org/def-server">About</a>
    </div>
	
	------
	
		http://defs.opengis.net/vocprez/
		http://defs.opengis.net/vocprez/about
		http://defs.opengis.net/vocprez/search
		http://defs.opengis.net/vocprez/vocab/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/auth/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/crs/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/dataType/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/def-type/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/dgiwg/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/doc-element/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/doc-type/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/hosted/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/ietf-rfc-4646/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/iso-8601/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/isoDataTypes/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/observationType/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/ogc/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/proxied/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/register/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/serviceType/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/spec-element/
		https://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/uom/
	"""
	url = 'http://defs.opengis.net/vocprez/object?uri=http://www.opengis.net/def/metamodel/ogc-na/&_mediatype=text/turtle'

class prefix:
	"""
	<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML+RDFa 1.0//EN" "http://www.w3.org/MarkUp/DTD/xhtml-rdfa-1.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"
    xmlns:dc="http://purl.org/dc/terms/"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    xmlns:vann="http://purl.org/vocab/vann/"
    xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"
    xmlns:owl="http://www.w3.org/2002/07/owl#"
    xmlns:ov="http://open.vocab.org/terms/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
  >

	"""
	base = 'http://prefix.cc'
	popular = f'{base}/popular'
	
	'about/formats;reverse?uri=http://xmlns.com/foaf/0.1/'
	vann_all = f'{popular}/all.file.vann'
	all_json_ld = f'{popular}/all.file.jsonld'
	all_json = f'{popular}/all.file.json'
	all_txt = f'{popular}/all.file.txt'
	'http://prefix.cc/popular.file.csv'
	#http://prefix.cc/popular.file.ini
	#http://prefix.cc/popular.file.jsonld
	#http://prefix.cc/popular.file.json
	#http://prefix.cc/popular/all
	#https://lov.linkeddata.es/dataset/lov/vocabs/all
	
	ctx = 'http://prefix.cc/context.jsonld'
	_ctx = 'http://prefix.cc/context'
	reverse = 'http://prefix.cc/reverse'
	pre = 'http://prefix.cc/reverse?uri=http://xmlns.com/foaf/0.1/&format=ttl'
	url = 'http://prefix.cc/{prefix}.file.{format}'
	all = 'http://prefix.cc/popular/all'

class obofoundry:
	dash = 'http://dashboard.obofoundry.org/dashboard/index.html'
	tutorial = 'https://github.com/jamesaoverton/obo-tutorial'
	oborel = 'https://github.com/oborel/obo-relations'
	obo = 'https://oborel.github.io/obo-relations/'
	ro = 'https://github.com/oborel/obo-relations/blob/master/ro.owl'
	ro = 'https://github.com/oborel/obo-relations/blob/master/ro.obo'
	ro = 'https://github.com/oborel/obo-relations/blob/master/ro.json'
	ro = 'https://github.com/oborel/obo-relations/blob/master/ro-base.owl'
	ro = 'https://github.com/oborel/obo-relations/blob/master/ro-base.obo'
	oi = 'https://github.com/oborel/obo-relations/blob/master/omo_import.owl'
	co = 'https://github.com/oborel/obo-relations/blob/master/core.owl'
	annotations = 'https://github.com/oborel/obo-relations/blob/master/annotations.owl'
	
	di = 'http://dictybase.org/'
	dii = 'https://github.com/dictyBase/migration-data'
	mged = 'http://mged.sourceforge.net/ontologies/MGEDontology.php'
	obi = 'http://obi-ontology.org'
	bfo = 'http://purl.obolibrary.org/obo/bfo.owl'
	cido = 'http://purl.obolibrary.org/obo/cido.owl'
	miro = 'http://purl.obolibrary.org/obo/miro.owl'
	taxon = 'http://purl.obolibrary.org/obo/ncbitaxon.owl'
	obo_rel = 'http://purl.obolibrary.org/obo/obo_rel.owl'
	ontoneo = 'http://purl.obolibrary.org/obo/ontoneo.owl'
	pato = 'http://purl.obolibrary.org/obo/pato.owl'
	
	robot = 'http://robot.obolibrary.org/convert'
	pb = 'http://www.pathbase.net'
	ncit = 'http://purl.obolibrary.org/obo/ncit.owl'
	thes = 'https://github.com/NCI-Thesaurus/thesaurus-obo-edition'
	base = 'https://github.com/OBOFoundry'
	gh = 'https://github.com/OBOFoundry/OBOFoundry.github.io'
	reg = 'https://github.com/OBOFoundry/OBOFoundry.github.io/blob/master/registry/'
	iss = 'https://github.com/OBOFoundry/OBOFoundry.github.io/issues'
	ont = 'https://github.com/OBOFoundry/OBOFoundry.github.io/tree/master/ontology'

class creativecommons:
	c2 = 'https://creativecommons.org/licenses/by/2.0/'
	c3 = 'https://creativecommons.org/licenses/by/3.0/'
	c4 = 'https://creativecommons.org/licenses/by/4.0/'
	pd = 'https://creativecommons.org/publicdomain/zero/1.0/'

class eli:
	'http://data.europa.eu/eli/ontology#'
	pr = 'http://www.opengis.net/def/metamodel/profiles/'
	hyf = 'https://www.opengis.net/def/schema/hy_features/hyf/'
	ld = 'https://www.w3.org/TR/json-ld/'
	iso = 'https://www.iso.org/standard/57466.html'
	mod = 'http://www.opengis.net/def/ont/modspec/'
	specrel = 'http://www.opengis.net/def/ont/specrel'
	mods = 'http://www.opengis.net/def/ont/modspec'
	arq = 'http://jena.apache.org/ARQ/function#'
	pol = 'http://www.opengis.net/def/metamodel/ogc-na/'
	pipe = 'https://www.opengis.net/def/pipelineml'
	jdc = 'http://www.opengis.net/def/metamodel/profiles/json_ld_context'
	na = 'https://github.com/opengeospatial/NamingAuthority'
	swa = 'http://topbraid.org/swa#'
	tosh = 'http://topbraid.org/tosh#'

class lov_:
	base = lov = 'https://lov.linkeddata.es/dataset/lov'
	qa = f'{lov}/qa'
	about = f'{lov}/about'
	agents = f'{lov}/agents'
	api = f'{lov}/api'
	sparql = f'{lov}/sparql'
	terms = f'{lov}/terms'
	vocabs = f'{lov}/vocabs'
	
	languages = f'{lov}/languages'
	eng = f'{languages}/eng'
	
	#/dataset/lov/api
	
	al = f'{api}/v2/agent/list'
	f'{api}/v2/agent/info?agent=W3C'
	f'{api}/v2/term/search?q=Person&type=class'
	f'{api}/v2/term/suggest?q=preson'
	tag = f'{vocabs}?&tag=API', f'{vocabs}?&tag=Catalogs', \
	      'https://lov.linkeddata.es/dataset/lov/vocabs?&tag=IoT', 'https://lov.linkeddata.es/dataset/lov/vocabs?&tag=Metadata'
	'https://lov.linkeddata.es/dataset/lov/?&tag=Catalogs'
	'https://lov.linkeddata.es/dataset/lov/?&type=class'
	'https://lov.linkeddata.es/dataset/lov/?&type=property'
	'https://lov.linkeddata.es/dataset/lov/?&vocab=obo'
	'http://lov.okfn.org/dataset/lov/Recommendations_Vocabulary_Design.pdf'
	#'http://okfn.org/
	
	acl = 'http://www.w3.org/ns/auth/acl'
	gen = 'http://www.w3.org/2006/gen/ont#', 'http://www.w3.org/2006/gen/ont.n3', 'http://www.w3.org/2006/gen/ont.rdf'
	api = 'https://lov.linkeddata.es/dataset/lov/api'
	#http://purl.org/iso25964/DataSet/Versioning#, http://pub.tenforce.com/schemas/iso25964/versioning
	#http://purl.org/linked-data/sdmx/2009/concept#
	vc = 'http://www.w3.org/2006/vcard/ns#'
	
	#http://purl.org/vocab/changeset/schema#
	#http://purl.org/twc/vocab/vsr/graffle#, https://raw.githubusercontent.com/timrdf/vsr/master/ontologies/vsr.ttl.owl
	#NET,wf4ever,vocab,spar,linked-data,.owl,twc
	
	#:https://lov.linkeddata.es/dataset/lov/api/v2/term/search?q=Person&type=class
	#:https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/search?q=time&lang=English
	#:https://lov.linkeddata.es/dataset/lov/api/v2/agent/search?q=Pierre&type=person
	#:https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/list
	#:https://lov.linkeddata.es/dataset/lov/api/v2/agent/autocomplete?q=bern
	#:https://lov.linkeddata.es/dataset/lov/api/v2/term/suggest?q=preson
	#:https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/info?vocab=schema
	#:https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/autocomplete?q=geo
	#:https://lov.linkeddata.es/dataset/lov/api/v2/term/autocomplete?q=foaf:p&type=class
	#:https://lov.linkeddata.es/dataset/lov/api/v2/agent/list
	#:https://lov.linkeddata.es/dataset/lov/api/v2/agent/info?agent=W3C
	
	DUL = 'http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#'
	IOLite = "http://www.ontologydesignpatterns.org/ont/dul/IOLite.owl#"
	LMM_L1 = "http://www.ontologydesignpatterns.org/ont/lmm/LMM_L1.owl#"
	ontopic = "http://www.ontologydesignpatterns.org/ont/dul/ontopic.owl#"
	
	a_cd = "https://w3id.org/arco/ontology/context-description/"
	arco = "https://w3id.org/arco/ontology/arco/"
	core = "https://w3id.org/arco/ontology/core/"
	opla = "http://ontologydesignpatterns.org/opla#"
	cat = "https://w3id.org/arco/ontology/catalogue/"
	loc = "https://w3id.org/arco/ontology/location/"
	opla1 = "http://ontologydesignpatterns.org/opla/"
	
	_api = 'https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/autocomplete'
	aloc = 'https://lov.linkeddata.es/dataset/lov/vocabs/a-loc'
	algo = 'https://lov.linkeddata.es/dataset/lov/vocabs/algo'
	'https://lov.linkeddata.es/dataset/lov/vocabs/rdf'
	'https://lov.linkeddata.es/dataset/lov/vocabs/rdfs'
	
	'https://lov.linkeddata.es/dataset/lov/api/v2/agent/autocomplete?q=bern'
	sbox = 'https://w3id.org/arco/ontology/location'
	vocab = 'https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/info?vocab=schema'  #datasets
	geo = 'https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/autocomplete?q=geo'
	src = 'https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/search?q=time&lang=English'
	ss = 'https://lov.linkeddata.es/dataset/lov/api/v2/term/search?q={}&type=class'  #class, propery, datatype, instance
	lst = 'https://lov.linkeddata.es/dataset/lov/api/v2/vocabulary/list'  #json

class w3tr:
	scripts =   'http://www.w3.org/scripts'
	std =       'http://www.w3.org/standards/'
	agents =    'http://www.w3.org/standards/agents/'
	types =     'http://www.w3.org/standards/types'
	guide =     'http://www.w3.org/Guide/'
	web_platform_tests = 'https://web-platform-tests.org/'
	tr_automation = 'http://www.w3.org/2002/01/tr-automation'
	vv =            'http://www.w3.org/2002/01/tr-automation/viewBy.xsl'
	automation = 'http://www.w3.org/2002/01/tr-automation/tr-stats-ui'
	automation = 'http://www.w3.org/2002/01/tr-automation/rdf2tr.xsl'
	tr =         'http://www.w3.org/2002/01/tr-automation/rdf2tr'
	ts = 'http://www.w3.org/2001/11/trdoc-data-ts/'
	trdoc2rdf = 'http://www.w3.org/2001/10/trdoc2rdf'
	trdoc = 'http://www.w3.org/2001/10/trdoc-data'
	trleg = 'http://www.w3.org/2000/04/mem-news/trleg.rdf'
	trsupp = 'http://www.w3.org/2000/04/mem-news/trsupp.n3'
	'http://www.w3.org/2000/04/mem-news/Makefile'
	date = "http://www.w3.org/2001/08/date-util.xslt"
	
	tr =     'http://www.w3.org/2000/04/mem-news/tr.rdf'
	groktr = 'http://www.w3.org/2000/04/mem-news/groktr'
	groktr = 'http://www.w3.org/2000/04/mem-news/groktrleg.py'
	tr_merge='http://www.w3.org/2000/04/mem-news/tr-merge.n3'
	trbroken = 'http://www.w3.org/2000/04/mem-news/trbroken.rdf'
	trleg = 'http://www.w3.org/2000/04/mem-news/trleg.rdf'
	trsupp = 'http://www.w3.org/2000/04/mem-news/trsupp.n3'
	xmldsig =  "http://www.w3.org/TR/xmldsig-core/"
	dtb = 'http://id.loc.gov/vocabulary/marcgt/dtb'
	'http://id.loc.gov/vocabulary/marcgt/dtb.skos.rdf'
	'http://id.loc.gov/vocabulary/marcgt/dtb.skos.nt'
	'http://id.loc.gov/vocabulary/marcgt/dtb.skos.json'
	'http://id.loc.gov/vocabulary/marcgt/dtb.madsrdf.rdf'
	'http://id.loc.gov/vocabulary/marcgt/dtb.madsrdf.json'
	'http://id.loc.gov/vocabulary/marcgt/dtb.json'
	'http://id.loc.gov/vocabulary/marcgt/collection_marcgt'
	
	'http://www.w3.org/2000/09/xmldsig#rawX509Certificate'
	#http://id.loc.gov/vocabulary/marcgt/collection_marcgt
	madsrdf = "http://www.loc.gov/mads/rdf/v1#"
	
	
	'http://id.loc.gov/vocabulary/marcgt/dtb.rdf'
	A = 'http://www.loc.gov/mads/rdf/v1#Authority'
	geo = 'http://www.opengis.net/ont/geosparql#'
	de = 'http://www.w3.org/ns/dcat#bbox'
	
	
	con = "http://www.w3.org/blog/2006/02/content-negotiation/"
	fc = 'http://www.w3.org/TR/webarch/#frag-coneg'
	cp = 'http://www.w3.org/TR/chips/#cp9.1'
	pp = 'http://lists.w3.org/Archives/Public/www-qa/'
	cnn = 'http://httpd.apache.org/docs/2.2/content-negotiation.html'
	qa = 'http://www.w3.org/International/questions/qa-apache-lang-neg'
	qap ='http://www.w3.org/International/questions/qa-lang-priorities'
	qw = 'http://www.w3.org/International/questions/qa-when-lang-neg'
	su = 'http://www.w3.org/Provider/Style/URI.html'
	'https://www.w3.org/International/questions/qa-lang-priorities.en'
	ig = 'http://www.w3.org/QA/IG/'
	c = 'http://www.w3.org/2005/04/conneg.phi.'
	stru = 'http://www.w3.org/2001/10/str-util.xsl'
	sty = 'http://www.w3.org/2002/07/01-style-xsl.xsl'
	ont = "http://www.daml.org/2001/03/daml+oil#"
	rcs = "http://www.w3.org/2001/03swell/rcs#"
	
	'http://www.w3.org/2000/10/swap/'
	'http://www.w3.org/2001/02pd/rec54#'
	'http://www.w3.org/2001/07/pubrules-checker'
	'http://www.w3.org/2001/10/trdoc-data'
	'http://www.w3.org/2001/10/trdoc2rdf'
	'http://www.w3.org/2001/11/trdoc-data-ts'
	'http://www.w3.org/2001/sw/'
	'http://www.w3.org/2002/01/tr-automation/TR-papertail'
	'http://www.w3.org/2002/01/tr-automation/rdf2tr'
	'http://www.w3.org/2002/01/tr-automation/rdf2tr.xsl'
	'http://www.w3.org/2002/01/tr-automation/tr-biblio-ui'
	'http://www.w3.org/2002/01/tr-automation/tr-count'
	'http://www.w3.org/2002/01/tr-automation/tr-process'
	'http://www.w3.org/2002/01/tr-automation/tr-stats-ui'
	'http://www.w3.org/2002/01/tr-automation/tr.rdf'
	'http://www.w3.org/2002/01/tr-automation/viewBy.xsl'
	'http://www.w3.org/2003/05/tr-refs/'
	'http://www.w3.org/2004/07/references-checker-ui'
	'http://www.w3.org/Consortium/Process/tr.html#Reports'
	'http://www.w3.org/TR/tr-activity'
	'http://www.w3.org/Team/9709/25-tr.html'
	
class locn:
	locn = 'http://www.w3.org/ns/locn.ttl'
	vs = 'http://www.w3.org/2003/06/sw-vocab-status/ns#'
	sioc = 'http://rdfs.org/sioc/ns#'
	wot = "http://xmlns.com/wot/0.1/"
	sf = 'http://www.opengis.net/ont/sf#'
	wg = 'http://www.w3.org/2003/01/geo/wgs84_pos#'
	ref = 'http://www.w3.org/2001/02pd/rec54#'
	wdsr = 'http://www.w3.org/2007/05/powder-s#'
	cuap = 'http://www.w3.org/TR/cuap'
	cu = 'http://www.w3.org/TR/cuap#protocols'
	c = 'http://www.w3.org/TR/cuap.html'
	
	'http://www.w3.org/TR/UAAG10/conformance.html#conformance-profiles'
	stat = 'http://www.w3.org/TR/UAAG10/cover.html#status'
	uaag = 'http://www.w3.org/2002/10/uaag10-faq/'
	glos = 'http://www.w3.org/TR/UAAG10/glossary.html#terms'
	voaf = 'http://purl.org/vocommons/voaf#'
	vann = 'http://purl.org/vocab/vann/'
	sf = 'http://www.opengis.net/ont/sf#'
	geo = 'http://www.w3.org/2003/01/geo/wgs84_pos#'
	not3 = 'http://www.w3.org/2000/10/n3/notation3.py'
	geoo = 'http://schemas.opengis.net/geosparql/1.0/geosparql_vocab_all.rdf'
	xmod67 = 'http://www.w3.org/2000/10/swap/infoset/xmod67.html'
	lookout = 'http://www.w3.org/2000/10/swap/pim/lookout.py'
	
	
	tr_pdoc = 'tr-process'
	tr_proc = 'tr-process.n3'
	pd = 'http://www.w3.org/2001/02pd/'
	roadmap = 'http://www.w3.org/2001/04/roadmap'
	rec22 = 'http://www.w3.org/2001/02pd/rec22.dot'
	
	rec54 =     "http://www.w3.org/2001/02pd/rec54#", 'http://www.w3.org/2001/02pd/rec54.rdf', 'http://www.w3.org/2001/02pd/rec54.n3'
	mat =   "http://www.w3.org/2002/05/matrix/vocab#"
	trdoc2rdf =    'http://www.w3.org/2001/10/trdoc2rdf.xslt'
	rdfs2html = 'http://www.w3.org/2002/06/rdfs2html.xsl'
	act  =  'http://www.w3.org/TR/tr-activity'
	actp = 'https://w3c.github.io/activitypub/'
	actv = 'https://w3c.github.io/activitystreams/vocabulary/'
	vdu = 'https://w3c.github.io/dwbp/vocab-du.html'
	data = 'https://www.w3.org/2013/data/'
	'https://w3c.github.io/dwbp/bp.html'
	'http://eurovoc.europa.eu/'
	'http://purl.org/dc/terms/conformsTo'
	'http://rdfs.org/sioc/spec/#sec-modules-types'
	intv = 'http://reference.data.gov.uk/id/interval'
	doi = 'http://www.doi.org/'
	cs = 'http://www.sparontologies.net/ontologies/cito/source.html'
	cu = 'https://w3c.github.io/TR/vocab-data-cube/#cubes-slices'
	dwbp = 'https://w3c.github.io/dwbp/dwbp-example.ttl'
	hdf5 = 'https://www.hdfgroup.org/HDF5/'
	ci = 'https://www.w3.org/TR/dwbp-ucr/#R-Citable'
	M = 'https://www.w3.org/TR/dwbp-ucr/#R-FormatMachineRead'
	ldbp = 'https://www.w3.org/TR/ld-bp/#VOCABULARIES'
	dsd = 'https://www.w3.org/TR/vocab-data-cube/#dsd-cog'
	'http://data.ordnancesurvey.co.uk/ontology/admingeo/'
	vg = 'http://rdfs.org/ns/void-guide'
	wi = 'http://semanticweb.org/wiki/VoiD'
	ddi = 'http://www.ddialliance.org/'
	org = 'http://www.w3.org/ns/org#'
	gr = "http://purl.org/goodrelations/v1#"
	owlTime = "http://www.w3.org/2006/time#"
	'http://www.w3.org/TR/vocab-org/'
	'http://www.w3.org/TR/void/'
	'http://www.w3.org/egov/wiki/Data_Catalog_Vocabulary'
	ii = 'https://w3c.github.io/IndexedDB/'
	'https://linkedresearch.org/ldn/'
	its2req = 'https://w3c.github.io/preload/', 'https://w3c.github.io/its2req'
	
	tlreq = 'https://w3c.github.io/tlreq/'
	did_core = 'http://www.w3.org/TR/did-core/'
	r3data = 'http://schema.re3data.org/3-1/re3dataV3-1.xsd'
	fdp_s = 'https://w3id.org/fdp/fdp-o#MetadataService'
	atom = 'http://www.w3.org/TR/tr.xml'
	feed = 'http://www.w3.org/blog/news/feed/atom'
	tr = 'http://www.w3.org/2002/01/tr-automation/tr.rdf'
	tr_automation = 'http://www.w3.org/2002/01/tr-automation/'
	rc = 'https://www.w3.org/2004/07/references-checker.xsl'
	uri = 'http://www.w3.org/2000/07/uri43/uri.xsl'
	rec = "http://www.w3.org/2001/02pd/rec54#"
	doc = "http://www.w3.org/2000/10/swap/pim/doc#"
	
	
	xslt4html = 'http://www.w3.org/2002/08/xslt4html'
	org = "http://www.w3.org/2001/04/roadmap/org#"
	mat = "http://www.w3.org/2002/05/matrix/vocab#"
	doc = "http://www.w3.org/2000/10/swap/pim/doc#"
	contact = "http://www.w3.org/2000/10/swap/pim/contact#"
	log = 'http://www.w3.org/2000/10/swap/log#'
	ns = "http://www.w3.org/2001/02pd/rec54#"
	proc = "http://www.w3.org/Consortium/Process/"
	pubrules = 'http://www.w3.org/pubrules/'
	ge = 'https://www.getty.edu/research/tools/vocabulary/tgn/index.html'
	#https://www.dublincore.org/specifications/dublin-core/dcmi-terms/terms/TGN/
	
class getty:
	#https://www.getty.edu/research/tools/vocabularies/tgn/about.html
	#https://www.getty.edu/research/tools/vocabularies/ulan/about.html
	
	dl = 'http://www.getty.edu/research/tools/vocabularies/obtain/download.html'
	dic = 'https://www.getty.edu/research/tools/article_databases/dictionaries.html'
	lod = 'https://www.getty.edu/research/tools/vocabularies/lod/index.html'
	ore = 'https://www.getty.edu/research/tools/vocabularies/obtain/openrefine.html'
	
	
class style:
	rdfs2html = 'http://www.w3.org/2002/06/rdfs2html'
	csv = 'http://dev.w3.org/cvsweb/2004/rdfs2html/rdfs2html.xsl'
	xr = 'http://www.w3.org/2000/10/swap/xml2rdf.py'
	'http://www.w3.org/2001/02pd/rfc65.n3'
	
	dca = 'http://dublincore.org/2000/03/13-dcagent#'
	dcq = 'http://dublincore.org/2000/03/13-dcq#'
	'http://www.w3.org/2001/02pd/rec54.rdf'
	'http://www.w3.org/2001/02pd/rec54.n3'
	'http://www.w3.org/2001/02pd/rec54'
	'http://www.w3.org/2001/05/xslt'
	'http://www.w3.org/2001/02pd/rdfs.n3'
	'http://www.w3.org/2001/02pd/rdf2dot.xsl'
	prop43 = 'http://www.w3.org/2001/02pd/prop43.n3'
	graphviz = 'http://www.w3.org/2001/02pd/gv.n3'
	'http://www.w3.org/2001/02pd/'
	'http://www.w3.org/2001/02pd/Makefile'
	'http://www.graphviz.org/doc/info/attrs.html'
	'http://www.w3.org/2000/10/atrip/rdfnorm.xsl'
	'http://www.w3.org/2000/08/w3c-synd/'
	
class opencitations:
	tools = 'http://opencitations.net/tools'
	model = 'http://opencitations.net/model'
	datasets = '/datasets'
	#http://www.w3.org/TR/SMIL/'
	#'http://www.w3.org/TR/owl-ref/
	#http://www.w3.org/TR/owl-test/
	#http://www.w3.org/TR/owl-guide

	#http://www.w3.org/TR/qaframe-spec/specgl-ics
	#'http://www.w3.org/TR/WAI-WEBCONTENT
	#http://www.w3.org/TR/qaframe-spec/
	#http://www.w3.org/TR/spec-variability/
	#http://www.w3.org/TR/wsdl
	#http://www.w3.org/TR/wsdl20/
	#http://www.w3.org/2007/06/wsdl/wsdl20.xsd
	#http://www.w3.org/TR/xpath20/

class jsonschema:
	keywords = ('$ref', '$recursiveRef', '$id', '$schema', '$recursiveAnchor')
	cts = ('application/schema+json', 'application/schema-instance+json', 'application/json')
	contextUri = 'contextUri'
	targetMediaType = 'targetMediaType'
	rel = 'rel'
	targetUri = 'targetUri'
	hrefInputTemplates = 'hrefInputTemplates'
	'application/json'
	uri = 'https://json-schema.org/draft/2019-09/hyper-schema'
	vocab = 'https://json-schema.org/draft/2019-09/vocab'
	vocab_core = 'https://json-schema.org/draft/2019-09/vocab/core'
	vhs = 'https://json-schema.org/draft/2019-09/vocab/hyper-schema'
	schema = 'https://json-schema.org/draft/2019-09/schema'
	meta = 'https://json-schema.org/draft/2019-09/meta/hyper-schema'
	links = 'https://json-schema.org/draft/2019-09/links'

class gloss:
	"""
	http://www.w3.org/2001/12/Glossary
	http://www.w3.org/2004/07/def-to-glossary.xsl
	http://www.w3.org/2003/glossary/
	http://www.w3.org/2003/glossary/subglossary/di-gloss.rdf/
	http://www.w3.org/2003/03/glossary-project/
	http://www.w3.org/2003/glossary/subglossary/All/
	http://www.w3.org/2003/glossary/subglossary/ATAG10.rdf/
	http://www.w3.org/2003/glossary/subglossary/CCPP-struct-vocab.rdf/
	http://www.w3.org/2003/glossary/subglossary/CSS2.rdf/
	http://www.w3.org/2003/glossary/subglossary/DOM-Level-2-Events.rdf/
	http://www.w3.org/2003/glossary/subglossary/DOM-Level-2-HTML.rdf/
	http://www.w3.org/2003/glossary/subglossary/DOM-Level-2-Traversal-Range.rdf/
	http://www.w3.org/2003/glossary/subglossary/MathML2.rdf/
	http://www.w3.org/2003/glossary/subglossary/P3P.rdf/
	http://www.w3.org/2003/glossary/subglossary/PNG.rdf/
	http://www.w3.org/2003/glossary/subglossary/Process.rdf/
	http://www.w3.org/2003/glossary/subglossary/REC-xml-names.rdf/
	http://www.w3.org/2003/glossary/subglossary/REC-xml.rdf/
	http://www.w3.org/2003/glossary/subglossary/WCA-terms.rdf/
	http://www.w3.org/2003/glossary/subglossary/charreq.rdf/
	http://www.w3.org/2003/glossary/subglossary/di-gloss.rdf/
	http://www.w3.org/2003/glossary/subglossary/hypertext-terms.rdf/
	http://www.w3.org/2003/glossary/subglossary/owl-guide.rdf/
	http://www.w3.org/2003/glossary/subglossary/qa-glossary.rdf/
	http://www.w3.org/2003/glossary/subglossary/qaframe-spec.rdf/
	http://www.w3.org/2003/glossary/subglossary/rdf-mt.rdf/
	http://www.w3.org/2003/glossary/subglossary/rdf-syntax.rdf/
	http://www.w3.org/2003/glossary/subglossary/rfc2616-sec1.rdf/
	http://www.w3.org/2003/glossary/subglossary/ruby.rdf/
	http://www.w3.org/2003/glossary/subglossary/soap12-part1.rdf/
	http://www.w3.org/2003/glossary/subglossary/speech-synthesis.rdf/
	http://www.w3.org/2003/glossary/subglossary/uuag10.rdf/
	http://www.w3.org/2003/glossary/subglossary/voicexml20.rdf/
	http://www.w3.org/2003/glossary/subglossary/w3c-jargon.rdf/
	http://www.w3.org/2003/glossary/subglossary/wcag10.rdf/
	http://www.w3.org/2003/glossary/subglossary/weaving.rdf/
	http://www.w3.org/2003/glossary/subglossary/webarch.rdf/
	http://www.w3.org/2003/glossary/subglossary/ws-gloss.rdf/
	http://www.w3.org/2003/glossary/subglossary/xforms.rdf/
	http://www.w3.org/2003/glossary/subglossary/xhtml-modularization.rdf/
	http://www.w3.org/2003/glossary/subglossary/xhtml1.rdf/
	http://www.w3.org/2003/glossary/subglossary/xinclude.rdf/
	http://www.w3.org/2003/glossary/subglossary/xkms2-req/
	http://www.w3.org/2003/glossary/subglossary/xlink.rdf/
	http://www.w3.org/2003/glossary/subglossary/xml-names11.rdf/
	http://www.w3.org/2003/glossary/subglossary/xml11.rdf/
	http://www.w3.org/2003/glossary/subglossary/xmlschema-2.rdf/
	http://www.w3.org/2003/glossary/subglossary/xpath-datamodel/
	http://www.w3.org/2003/glossary/subglossary/xpath.rdf/
	http://www.w3.org/2003/glossary/subglossary/xpath20/
	http://www.w3.org/2003/glossary/subglossary/xptr-framework.rdf/
	http://www.w3.org/2003/glossary/subglossary/xquery/
	http://www.w3.org/2003/glossary/subglossary/xslt20/"""