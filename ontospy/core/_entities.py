# !/usr/bin/env python
#  -*- coding: UTF-8 -*-


from itertools import count

import rdflib
from colorama import Fore
from colorama import Style

from . import *
from .utils import *

# http://stackoverflow.com/questions/8628123/counting-instances-of-a-class

from . import utils as ut


class RdfEntity:
    """
    Pythonic representation of an RDF resource - normally not instantiated but used for
    inheritance purposes

    <triples> : a structure like this:
    [(rdflib.term.URIRef(u'http://xmlns.com/foaf/0.1/OnlineChatAccount'),
      rdflib.term.URIRef(u'http://www.w3.org/2000/01/rdf-schema#comment'),
      rdflib.term.Literal(u'An online chat account.')),
     (rdflib.term.URIRef(u'http://xmlns.com/foaf/0.1/OnlineChatAccount'),
      rdflib.term.URIRef(u'http://www.w3.org/2000/01/rdf-schema#subClassOf')]

    """
    uri: str
    _ids = count(0)

    def __repr__(self):
        return f"<Ontospy: RdfEntity object for uri *{self.uri}*>"

    def __init__(
        self,
        uri,
        rdftype=None,
        namespaces=None,
        ext_model=False,
        is_Bnode: bool=False,
        pref_title="qname",
        pref_lang="en",
    ):
        """
        Init ontology object. Load the graph in memory, then setup all necessary attributes.

        2017-07-23
        ext_model: flag to mark entities that are instantiated but are not part
        of the main model (eg xsd:String range values)
        is_Bnode: flag to identify Bnodes
        """
        self.id = next(self._ids)

        self.uri: rdflib.term.URIRef #Uriref = uri  # rdflib.Uriref

        self.locale = ut.inferURILocalSymbol(self.uri)[0]
        self.ext_model = ext_model
        self.is_Bnode = is_Bnode
        self._pref_title: str = pref_title
        self._pref_lang: str = pref_lang

        self.rdftype = rdftype
        self.triples = None
        self.rdflib_graph = rdflib.Graph()
        self.namespaces = namespaces
        self.all_shapes = []

        self.qname = self._build_qname()
        self.rdftype_qname = self._build_qname(rdftype)

        # PS default slug gets overridden later for typed entities
        self.slug = "entity-" + ut.slugify(self.qname)

        self._children = []
        self._parents = []
        self._instance_of = []
        # self.siblings = []

    def rdf_source(self, format="turtle"):
        """xml, n3, turtle, nt, pretty-xml, trix are built in"""
        if self.triples:
            if not self.rdflib_graph:
                self._buildGraph()
            s = self.rdflib_graph.serialize(format=format)
            if isinstance(s, bytes):
                s = s.decode("utf-8")
            return s
        else:
            return None

    def printSerialize(self, format="turtle"):
        ut.printInfo("\n" + self.rdf_source(format))

    def printTriples(self):
        """display triples"""
        ut.printInfo(Fore.RED + self.uri + Style.RESET_ALL)
        for x in self.triples:
            ut.printInfo(Fore.BLACK + "=> " + str(x[1]))
            ut.printInfo(Style.DIM + ".... " + str(x[2]) + Fore.RESET)
        ut.printInfo("")

    def _build_qname(self, uri=None, namespaces=None):
        """extracts a qualified name for a uri"""
        if not uri:
            uri = self.uri
        if not namespaces:
            namespaces = self.namespaces
        return ut.uri2niceString(uri, namespaces)

    def _buildGraph(self):
        """
        transforms the triples list into a proper rdflib graph
        (which can be used later for querying)
        """
        for n in self.namespaces:
            self.rdflib_graph.bind(n[0], rdflib.Namespace(n[1]))
        if self.triples:
            for terzetto in self.triples:
                self.rdflib_graph.add(terzetto)

    # methods added to RdfEntity even though they apply only to some subs

    def ancestors(self, cl=None, noduplicates=True):
        """returns all ancestors in the taxonomy"""
        if not cl:
            cl = self
        if cl.parents():
            bag = []
            for x in cl.parents():
                if x.uri != cl.uri:  # avoid circular relationships
                    bag += [x] + self.ancestors(x, noduplicates)
                else:
                    bag += [x]
            # finally:
            if noduplicates:
                return remove_duplicates(bag)
            else:
                return bag
        else:
            return []

    def descendants(self, cl=None, noduplicates=True):
        """returns all descendants in the taxonomy"""
        if not cl:
            cl = self
        if cl.children():
            bag = []
            for x in cl.children():
                if x.uri != cl.uri:  # avoid circular relationships
                    bag += [x] + self.descendants(x, noduplicates)
                else:
                    bag += [x]
            # finally:
            if noduplicates:
                return remove_duplicates(bag)
            else:
                return bag
        else:
            return []

    def parents(self):
        """wrapper around property"""
        return self._parents

    def children(self):
        """wrapper around property"""
        return self._children

    def instance_of(self):
        """wrapper around property"""
        return self._instance_of

    def getValuesForProperty(self, aPropURIRef):
        """
        generic way to extract some prop value eg
            In [11]: c.getValuesForProperty(rdflib.RDF.type)
            Out[11]:
            [rdflib.term.URIRef(u'http://www.w3.org/2002/07/owl#Class'),
             rdflib.term.URIRef(u'http://www.w3.org/2000/01/rdf-schema#Class')]
        """
        if not type(aPropURIRef) == rdflib.URIRef:
            aPropURIRef = rdflib.URIRef(aPropURIRef)
        return list(self.rdflib_graph.objects(None, aPropURIRef))

    def bestLabel(self, prefLanguage="", qname_allowed=True, quotes=False):
        """
        facility for extrating the best available label for an entity

        ..This checks RFDS.label, SKOS.prefLabel and finally the qname local component
        """

        test = self.getValuesForProperty(rdflib.RDFS.label)
        out = ""

        if not prefLanguage:
            prefLanguage = self._pref_lang

        if test:
            out = ut.firstStringInList(test, prefLanguage)
        else:
            test = self.getValuesForProperty(rdflib.namespace.SKOS.prefLabel)
            if test:
                out = ut.firstStringInList(test, prefLanguage)
            else:
                if qname_allowed:
                    out = self.locale

        if quotes and out:
            return ut.addQuotes(out)
        else:
            return out

    def bestDescription(self, prefLanguage="", quotes=False):
        """
        facility for extracting a human readable description for an entity
        
        https://www.w3.org/2009/08/skos-reference/skos.rdf
        
        https://www.w3.org/2009/08/skos-reference
        skos.rdf
        skos.html
            #http://www.w3.org/TR/skos-reference/extras.css
            #http://www.w3.org/StyleSheets/TR/base
            #http://www.w3.org/2004/02/skos/core.html
            #skos:mappingRelation, skos:closeMatch
            
        #http://www.w3.org/TR/2009/REC-skos-reference-20090818/#xl
        #http://www.w3.org/2008/05/skos-xl
        #owl:imports rdf:resource="http://www.w3.org/2004/02/skos/core"
        
        #http://www.w3.org/2008/05/skos-xl
        #http://www.w3.org/TR/skos-reference/
        
        skosxl = 'http://www.w3.org/2008/05/skos-xl#'
        #http://www.w3.org/2009/08/skos-reference/skos-xl.rdf
        #http://www.w3.org/TR/skos-reference/skos-xl.rdf
        
        https://www.w3.org/2009/08/skos-reference/skos-xl.rdf
        https://www.w3.org/2009/08/skos-reference/skos-owl1-dl.rdf
        https://www.w3.org/2009/08/skos-reference/skos-dl.rdf
        
        #specs,vocabs,data,tools,development,references,
        #skosxl:labelRelation skosxl:Label
        mads = 'http://www.loc.gov/mads/rdf/v1#
        
        
        #ClosedNamespace
        #NamespaceManager
        #is_ncname
        #split_uri
        #insert_trie
        #insert_strie
        #get_longest_namespace
        #_extras
        #DefinedNamespaceMeta
        #_NS: Namespace
        #__getitem__(cls, name: str, default=None)
        #_NS[name]
        #values = {cls[str(x)] for x in cls.__annotations__}
        #terms = {pfx: str(self._NS)}
        
        __module__
        __annotations__
        __doc__
        __contains__
        __getattribute__
        __new__
        __init__
        as_jsonld_context
        __call__
        __subclasses__
        __prepare__
        __instancecheck__
        __subclasscheck__
        __flags__
        __weakrefoffset__
        __dictoffset__
        __mro__
        __bases__, __abstractmethods__, __text_signature__
        __subclasshook__
        __init_subclass__
        """

        test_preds = [
            rdflib.RDFS.comment,
            rdflib.namespace.DCTERMS.description, #MediaType
            rdflib.namespace.DC.description,
            rdflib.namespace.SKOS.definition,
        ]

        if not prefLanguage:
            prefLanguage = self._pref_lang

        for pred in test_preds:
            test = self.getValuesForProperty(pred)
            # printInfo(str(test), "red")
            if test:
                if quotes:
                    return ut.addQuotes(ut.joinStringsInList(test, prefLanguage))
                else:
                    return ut.joinStringsInList(test, prefLanguage)
        return ""

    @property
    def title(self):
        """Entity title - used for display purposes only.
        Can be set by user once ontospy is created.
        Values allowed: 'qname' or 'label'

        Defaults to 'qname'.
        """

        if self._pref_title == "qname":
            out = self.qname
        elif self._pref_title == "label":
            out = self.bestLabel()
        else:
            return self.qname

        return out


class Ontology(RdfEntity):
    """
    Pythonic representation of an OWL ontology
    """

    def __repr__(self):
        return f"<Ontospy: Ontology object for uri *{self.uri}*>"

    def __init__(
        self,
        uri,
        rdftype=None,
        namespaces=None,
        pref_prefix="",
        ext_model=False,
        pref_title="qname",
        pref_lang="en",
    ):
        """
        Init ontology object. Load the graph in memory, then setup all necessary attributes.
        """
        super().__init__(
            uri,
            rdftype,
            namespaces,
            ext_model,
            pref_title=pref_title,
            pref_lang=pref_lang,
        )
        # self.uri = uri # rdflib.Uriref
        self.prefix = pref_prefix
        self.slug = "ontology-" + ut.slugify(self.qname)
        self.all_classes = []
        self.all_properties = []
        self.all_skos_concepts = []

    def annotations(self, qname=True):
        """
        wrapper that returns all triples for an onto.
        By default resources URIs are transformed into qnames
        """
        if qname:
            return sorted(
                [
                    (ut.uri2niceString(x, self.namespaces)),
                    (ut.uri2niceString(y, self.namespaces)),
                    z,
                ]
                for x, y, z in self.triples
            )
        else:
            return sorted(self.triples)

    def describe(self):
        """shotcut to pull out useful info for interactive use"""
        # self.printGenericTree()
        # self.printTriples()
        ut.printInfo(self.uri, "green")
        self.stats()

    def stats(self):
        """shotcut to pull out useful info for interactive use"""
        ut.printInfo(f"Classes.....: {len(self.all_classes):d}")
        ut.printInfo(f"Properties..: {len(self.all_properties):d}")


class OntoClass(RdfEntity):
    """
    Python representation of a generic class within an ontology.
    Includes methods for representing and querying RDFS/OWL classes


    domain_of_inferred: a list of dict
            [{<Class *http://xmlns.com/foaf/0.1/Person*>:
            [<Property *http://xmlns.com/foaf/0.1/currentProject*>,<Property *http://xmlns.com/foaf/0.1/familyName*>,
                etc....]},
        {<Class *http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing*>:
            [<Property *http://xmlns.com/foaf/0.1/based_near*>, etc...]},
            ]
    """

    def __init__(
        self,
        uri,
        rdftype=None,
        namespaces=None,
        ext_model=False,
        pref_title="qname",
        pref_lang="en",
    ):
        """
        ...
        """
        super().__init__(
            uri,
            rdftype,
            namespaces,
            ext_model,
            pref_title=pref_title,
            pref_lang=pref_lang,
        )
        self.slug = "class-" + slugify(self.qname)
        self.domain_of = []
        self.range_of = []
        self.domain_of_inferred = []
        self.range_of_inferred = []
        self.ontology = None
        self._instances = False  # calc on demand at runtime
        self.sparqlHelper = None  # the original graph the class derives from
        self.shapedProperties = []  # properties of this class that belong to a shape

    def __repr__(self):
        return f"<Class *{self.uri}*>"

    @property
    def instances(self):  # = all instances
        if not self._instances:
            return []
        return self._instances

    def count(self):
        return len(self.instances)

    def printStats(self):
        """shortcut to pull out useful info for interactive use"""
        ut.printInfo("----------------")
        ut.printInfo(f"Parents......: {len(self.parents()):d}")
        ut.printInfo(f"Children.....: {len(self.children()):d}")
        ut.printInfo(f"Ancestors....: {len(self.ancestors()):d}")
        ut.printInfo(f"Descendants..: {len(self.descendants()):d}")
        ut.printInfo(f"Domain of....: {len(self.domain_of):d}")
        ut.printInfo(f"Range of.....: {len(self.range_of):d}")
        ut.printInfo(f"Instances....: {self.count():d}")
        ut.printInfo("----------------")

    def printGenericTree(self):
        ut.printGenericTree(self)

    def describe(self):
        """shotcut to pull out useful info for interactive use"""
        # self.printTriples()
        ut.printInfo(self.uri, "green")
        self.printStats()
        # self.printGenericTree()


class OntoProperty(RdfEntity):
    """
    Python representation of a generic RDF/OWL property.

    rdftype is one of:
    rdflib.term.URIRef(u'http://www.w3.org/2002/07/owl#ObjectProperty')
    rdflib.term.URIRef(u'http://www.w3.org/2002/07/owl#DatatypeProperty')
    rdflib.term.URIRef(u'http://www.w3.org/2002/07/owl#AnnotationProperty')
    rdflib.term.URIRef(u'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property')

    """

    def __init__(
        self,
        uri,
        rdftype=None,
        namespaces=None,
        ext_model=False,
        pref_title="qname",
        pref_lang="en",
    ):
        """
        ...
        """
        super().__init__(
            uri,
            rdftype,
            namespaces,
            ext_model,
            pref_title=pref_title,
            pref_lang=pref_lang,
        )

        self.slug = "prop-" + ut.slugify(self.qname)
        self.rdftype = ut.inferMainPropertyType(rdftype)

        self.domains = []
        self.ranges = []
        self.ontology = None

    def __repr__(self):
        return f"<Property *{self.uri}*>"

    def printGenericTree(self):
        ut.printGenericTree(self)

    def printStats(self):
        """shotcut to pull out useful info for interactive use"""
        ut.printInfo("----------------")
        ut.printInfo("Parents......: %d" % len(self.parents()))
        ut.printInfo("Children.....: %d" % len(self.children()))
        ut.printInfo("Ancestors....: %d" % len(self.ancestors()))
        ut.printInfo("Descendants..: %d" % len(self.descendants()))
        ut.printInfo("Has Domain...: %d" % len(self.domains))
        ut.printInfo("Has Range....: %d" % len(self.ranges))
        ut.printInfo("----------------")

    def describe(self):
        """shotcut to pull out useful info for interactive use"""
        # self.printTriples()
        ut.printInfo(self.uri, "green")
        self.printStats()
        # self.printGenericTree()


class OntoSKOSConcept(RdfEntity):
    """
    Python representation of a generic SKOS concept within an ontology.
    @todo: complete methods..

    """

    def __init__(
        self,
        uri,
        rdftype=None,
        namespaces=None,
        ext_model=False,
        pref_title="qname",
        pref_lang="en",
    ):
        """
        ...
        """
        super().__init__(
            uri,
            rdftype,
            namespaces,
            ext_model,
            pref_title=pref_title,
            pref_lang=pref_lang,
        )
        self.slug = "concept-" + ut.slugify(self.qname)
        self.instance_of = []
        self.ontology = None
        self.sparqlHelper = None  # the original graph the class derives from

    def __repr__(self):
        return f"<SKOS Concept *{self.uri}*>"

    def printStats(self):
        """shotcut to pull out useful info for interactive use"""
        ut.printInfo("----------------")
        ut.printInfo("Parents......: %d" % len(self.parents()))
        ut.printInfo("Children.....: %d" % len(self.children()))
        ut.printInfo("Ancestors....: %d" % len(self.ancestors()))
        ut.printInfo("Descendants..: %d" % len(self.descendants()))
        ut.printInfo("----------------")

    def printGenericTree(self):
        ut.printGenericTree(self)

    def describe(self):
        """shotcut to pull out useful info for interactive use"""
        # self.printTriples()
        ut.printInfo(self.uri, "green")
        self.printStats()
        self.printGenericTree()


class OntoShape(RdfEntity):
    """
    Python representation of a SHACL shape.

    """

    def __init__(
        self,
        uri,
        rdftype=None,
        namespaces=None,
        ext_model=False,
        pref_title="qname",
        pref_lang="en",
    ):
        """
        ...
        """
        super().__init__(
            uri,
            rdftype,
            namespaces,
            ext_model,
            pref_title=pref_title,
            pref_lang=pref_lang,
        )
        self.slug = "shape-" + ut.slugify(self.qname)
        self.ontology = None
        self.targetClasses = []
        self.sparqlHelper = None  # the original graph the class derives from

    def __repr__(self):
        return "<SHACL shape *%s*>" % (self.uri)

    def printStats(self):
        """shotcut to pull out useful info for interactive use"""
        ut.printInfo("----------------")
        ut.printInfo("Parents......: %d" % len(self.parents()))
        ut.printInfo("Children.....: %d" % len(self.children()))
        ut.printInfo("Ancestors....: %d" % len(self.ancestors()))
        ut.printInfo("Descendants..: %d" % len(self.descendants()))
        ut.printInfo("----------------")

    def describe(self):
        """shotcut to pull out useful info for interactive use"""
        # self.printTriples()
        self.printStats()


__all__ = sorted(['OntoShape',
                  'OntoSKOSConcept',
                  'OntoProperty',
                  'OntoClass',
                  'Ontology',
                  'RdfEntity'])
