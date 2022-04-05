#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename = namespaces
# author=KGerring
# date = 3/30/22
# project alltypes
# docs root 
"""
 alltypes  

"""

__all__ = []

import sys  # isort:skip
import os  # isort:skip
import re  # isort:skip

formats = 'http://www.w3.org/ns/formats/'

'https://protege.stanford.edu/plugins/owl/dc/protege-dc.owl'

simple = '''
pending          http://pending.schema.org/
dc               http://purl.org/dc/elements/1.1/
dcterms          http://purl.org/dc/terms/
vann             http://purl.org/vocab/vann/
schema           http://schema.org/
sg               http://scigraph.springernature.com/
sgo              http://scigraph.springernature.com/ontologies/core/
sgo-pmc          http://scigraph.springernature.com/ontologies/product-market-codes/
vivo             http://vivoweb.org/ontology/core#
grid-institutes  http://www.grid.ac/institutes/
grid             http://www.grid.ac/ontology/
geo              http://www.opengis.net/ont/geosparql#
rdf              http://www.w3.org/1999/02/22-rdf-syntax-ns#
rdfs             http://www.w3.org/2000/01/rdf-schema#
xsd              http://www.w3.org/2001/XMLSchema#
owl              http://www.w3.org/2002/07/owl#
geo-pos          http://www.w3.org/2003/01/geo/wgs84_pos#
skos             http://www.w3.org/2004/02/skos/core#
skosxl           http://www.w3.org/2008/05/skos-xl#
foaf             http://xmlns.com/foaf/0.1/
ctx              https://springernature.github.io/scigraph/jsonld/sgcontext.json



gold            http://purl.org/linguistics/gold/
bibliography    http://www.linguistics-ontology.org/bibliography/bibliography.owl


articles        https://raw.githubusercontent.com/figshare/user_documentation/master/swagger_documentation/documentation/models/articles.json
coll            https://raw.githubusercontent.com/figshare/user_documentation/master/swagger_documentation/documentation/models
/collections.json
cio             https://raw.githubusercontent.com/micheldumontier/semanticscience/master/ontology/sio/release/sio-release.owl

registry_schema https://raw.githubusercontent.com/OBOFoundry/OBOFoundry.github.io/master/util/schema/registry_schema.json

ssom_jsonld     https://raw.githubusercontent.com/mapping-commons/sssom/master/sssom/jsonld/sssom.context.jsonld


csvw            http://www.w3.org/ns/csvw.jsonld

vann            http://prefix.cc/popular/all.file.vann
rfc_index       https://www.rfc-editor.org/rfc-index.xml

files           /Users/kristen/Desktop/ontologies

rfc             https://xml2rfc.tools.ietf.org/public/rfc/bibxml/reference.RFC.4880.xml

onts            https://raw.githubusercontent.com/OBOFoundry/OBOFoundry.github.io/master/registry/ontologies.yml



'''



if __name__ == '__main__':
	print(__file__)
