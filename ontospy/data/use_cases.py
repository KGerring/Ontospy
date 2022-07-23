#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename = use_cases
# author=KGerring
# date = 6/22/22
# project alltypes
# docs root 
"""
 alltypes  

"""
from __future__ import annotations

__all__ = []

import sys  # isort:skip
import os  # isort:skip
import re  # isort:skip

'http://www.w3.org/TR/rdb2rdf-ucr/'

changeset = 'http://vocab.org/changeset/schema.html'
'http://alistair.cockburn.us/get/2465'
'http://www.w3.org/TR/2009/NOTE-dap-api-reqs-20091015/'
'http://dublincore.org/groups/collections/collection-application-profile/'
'http://dvcs.w3.org/hg/gld/raw-file/default/dcat-ucr/index.html'
dcat_ucr = 'http://dvcs.w3.org/hg/gld/raw-file/default/dcat-ucr/index.html'
xmlspec = 'https://www.w3.org/2008/05/xmlspec-diff-generation/'

cwm = 'http://www.w3.org/2000/10/swap/doc/cwm'
cw = 'http://www.w3.org/2000/10/swap/cwm.py'
preload = 'http://www.w3.org/TR/preload/'
st = 'https://www.w3.org/2004/01/pp-impl/100074/status', 'https://www.w3.org/groups/wg/publishing/ipr'
schemastore = 'https://www.schemastore.org/api/json/catalog.json'
sssom = '/Users/kristen/repos/_tmp/sssom-py'

sw_BestPractices = 'http://www.w3.org/2001/sw/BestPractices/'
pubrules = 'https://www.w3.org/pubrules/'
pubrules_doc = 'https://www.w3.org/pubrules/doc'
nsuri = 'https://www.w3.org/2005/07/13-nsuri'
echidna = 'https://github.com/w3c/echidna/wiki'
qaframe_spec = 'https://www.w3.org/TR/qaframe-spec/'
def_to_glossary ='http://www.w3.org/2004/07/def-to-glossary.xsl'
qa_glossary = 'http://www.w3.org/QA/glossary'
qa_handbook = 'https://www.w3.org/TR/qa-handbook/'
qaframe_primer = 'https://www.w3.org/QA/WG/qaframe-primer'

frbr = 'http://www.ifla.org/publications/functional-requirements-for-bibliographic-records'
frbr_core = 'http://vocab.org/frbr/core.html'
lld_uc = 'http://www.w3.org/2005/Incubator/lld/XGR-lld-usecase-20111025/'
uc_frags = 'http://www.w3.org/TR/media-frags-reqs'
oslc = 'http://open-services.net/'
powder_uc = 'http://www.w3.org/TR/powder-use-cases/'
rb_rc = 'http://www.w3.org/TR/rdb2rdf-ucr/'


class raw:
	"""
	
	"""
	_base = 'https://raw.githubusercontent.com'
	lines = {
			f'{_base}/prefixcommons/biocontext/master/registry/monarch_context.jsonld',
			f'{_base}/linked-statistics/disco-spec/master/discovery.ttl',
			f'{_base}/oslc-op/oslc-specs/master/specs/core/core-vocab.ttl',
			f'{_base}/ukgovld/registry-core/master/src/main/vocabs/registryVocab.ttl',
			f'{_base}/pav-ontology/pav/gh-pages/mapping/dcterms.ttl',
			f'{_base}/pav-ontology/pav/gh-pages/mapping/skos.ttl',
			f'{_base}/pav-ontology/pav/gh-pages/provenance.ttl',
			f'{_base}/pav-ontology/pav/gh-pages/pav-no-import.rdf',
			f'{_base}/pav-ontology/pav/gh-pages/mapping/dcterms-void.ttl',
			f'{_base}/opencitations/corpus/master/context.json',
			f'{_base}/dcmi/ldci/master/docs/D2695955.json',
			f'{_base}/mapping-commons/sssom/master/sssom/jsonld/sssom.context.jsonld',
			f'{_base}/frictionlessdata/specs/master/schemas/dictionary/resource.yml',
			f'{_base}/frictionlessdata/specs/master/schemas/dictionary.json',
			f'{_base}/SPAROntologies/cito/master/docs/current/cito.owl',
			f'{_base}/collections-ontology/collections-ontology/master/collections.owl',
			f'{_base}/figshare/user_documentation/master/swagger_documentation/documentation/models/collections.json',
			f'{_base}/figshare/user_documentation/master/swagger_documentation/documentation/models/articles.json',
			f'{_base}/cygri/prefix.cc/master/tools/lov-mappings.sparql',
			f'{_base}/w3c/w3c.github.io/main/w3c.json-schema.json',
			f'{_base}/linkml/linkml/main/linkml/workspaces/datamodel/workspaces.py',
			f'{_base}/linkml/linkml/main/linkml/workspaces/datamodel/workspaces.yaml',
			f'{_base}/OBOFoundry/OBOFoundry.github.io/master/util/schema/registry_schema.json',
			f'{_base}/OBOFoundry/OBOFoundry.github.io/master/registry/ontologies.yml',
			f'{_base}/UKGovLD/publishing-statistical-data/master/specs/src/main/vocab/sdmx.ttl',
			f'{_base}/micheldumontier/semanticscience/master/ontology/sio/release/sio-release.owl',
	}







if __name__ == '__main__':
	print(__file__)
