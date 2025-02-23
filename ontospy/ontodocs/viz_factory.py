# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
#
#


import os
import shutil
import sys
import zipfile

# http://stackoverflow.com/questions/1714027/version-number-comparison
from distutils.version import StrictVersion

# django loading requires different steps based on version
# https://docs.djangoproject.com/en/dev/releases/1.7/#standalone-scripts
import django
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers.rdf import TurtleLexer

from .. import *  # import main ontospy VERSION
from ..core.utils import *
from .builder import ONTODOCS_VIZ_STATIC
from .builder import ONTODOCS_VIZ_TEMPLATES
from .utils import *

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

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass


if StrictVersion(django.get_version()) > StrictVersion("1.7"):
    from django.conf import settings
    from django.template import Context
    from django.template import Template

else:
    from django.conf import settings
    from django.template import Context
    from django.template import Template


try:
    from .CONFIG import VISUALIZATIONS_LIST

    VISUALIZATIONS_LIST = VISUALIZATIONS_LIST["Visualizations"]
except:  # Mother of all exceptions
    printDebug("Visualizations configuration file not found.", fg="red")
    raise


class VizFactory:
    """
    Object encapsulating common methods for building visualizations

    Tip: subclass and override as needed.
    """

    def __init__(self, ontospy_graph, title=""):
        self.title = ""
        self.ontospy_graph = ontospy_graph
        self.static_files = []
        self.static_url = ""  # one used in templates
        self.final_url = None
        self.output_path = None
        self.output_path_static = None
        home = os.path.expanduser("~")
        self.output_path_DEFAULT = os.path.join(home, "ontospy-viz-test")
        self.template_name = ""
        self.main_file_name = ""
        self.templates_root = ONTODOCS_VIZ_TEMPLATES
        self.static_root = ONTODOCS_VIZ_STATIC
        self.title = title or self.infer_best_title()
        self.basic_context_data = self._build_basic_context()

    def infer_best_title(self):
        """Selects something usable as a title for an ontospy graph.
        If we have more than one ontology definition, use a generic title."""
        if self.ontospy_graph.all_ontologies:
            if len(self.ontospy_graph.all_ontologies) > 1:
                return f"RDF knowledge graph ({len(self.ontospy_graph.all_ontologies)} ontologies)"
            else:
                return self.ontospy_graph.all_ontologies[0].uri
        elif self.ontospy_graph.sources:
            if len(self.ontospy_graph.sources) > 1:
                return f"RDF knowledge graph {len(self.ontospy_graph.sources)} sources"
            else:
                return self.ontospy_graph.sources[0]
        else:
            return "Untitled"

    def build(self, output_path=""):
        """method that should be inherited by all vis classes"""

        self.output_path = self.checkOutputPath(output_path)
        self._buildStaticFiles()
        self.final_url = self._buildTemplates()
        printDebug("Done.", "comment")
        printDebug("=> %s" % (self.final_url), "comment")
        return self.final_url

    def _buildTemplates(self):
        """
        do all the things necessary to build the viz
        should be adapted to work for single-file viz, or multi-files etc.

        :param output_path:
        :return:
        """
        #  in this case we only have one
        contents = self._renderTemplate(self.template_name, extraContext=None)
        # the main url used for opening viz
        f = self.main_file_name
        main_url = self._save2File(contents, f, self.output_path)
        return main_url

    def _renderTemplate(self, template_name, extraContext=None):
        """

        :param template_name: NOTE *relative* to templates folder
        :param extraContext: a dict that can be loaded on demand
        :return: the rendered template as a string
        """
        atemplate = open(self.templates_root + template_name, "r")
        t = Template(atemplate.read())
        context = Context(self.basic_context_data)
        if extraContext and type(extraContext) == dict:
            context.update(extraContext)
        contents = safe_str(t.render(context))
        return contents

    def _buildStaticFiles(self):
        """move over static files so that relative imports work
        Note: if a dir is passed, it is copied with all of its contents
        If the file is a zip, it is copied and extracted too
        # By default folder name is 'static', unless *output_path_static* is passed (now allowed only in special applications like KompleteVizMultiModel)
        """
        if not self.output_path_static:
            self.output_path_static = os.path.join(self.output_path, "static")
        # printDebug(self.output_path_static, "red")
        if not os.path.exists(self.output_path_static):
            os.makedirs(self.output_path_static)
        for x in self.static_files:
            source_f = os.path.join(self.static_root, x)
            dest_f = os.path.join(self.output_path_static, x)
            if os.path.isdir(source_f):
                if os.path.exists(dest_f):
                    # delete first if exists, as copytree will throw an error otherwise
                    shutil.rmtree(dest_f)
                shutil.copytree(source_f, dest_f)
            else:
                shutil.copyfile(source_f, dest_f)
                if x.endswith(".zip"):
                    printDebug("..unzipping")
                    zip_ref = zipfile.ZipFile(os.path.join(dest_f), "r")
                    zip_ref.extractall(self.output_path_static)
                    zip_ref.close()
                    printDebug("..cleaning up")
                    os.remove(dest_f)
                    # http://superuser.com/questions/104500/what-is-macosx-folder
                    shutil.rmtree(os.path.join(self.output_path_static, "__MACOSX"))

    def preview(self):
        if self.final_url:
            import webbrowser

            webbrowser.open(self.final_url)
        else:
            printDebug("Nothing to preview")

    def _build_basic_context(self):
        """
        Return a standard dict used in django as a template context
        """
        # printDebug(str(self.ontospy_graph.toplayer_classes))
        topclasses = self.ontospy_graph.toplayer_classes[:]
        if len(topclasses) < 3:  # massage the toplayer!
            for topclass in self.ontospy_graph.toplayer_classes:
                for child in topclass.children():
                    if child not in topclasses:
                        topclasses.append(child)

        if not self.static_url:
            self.static_url = "static/"  # default

        context_data = {
            "STATIC_URL": self.static_url,
            "ontodocs_version": VERSION,
            "ontospy_graph": self.ontospy_graph,
            "topclasses": topclasses,
            "docs_title": self.title,
            "namespaces": self.ontospy_graph.namespaces,
            "stats": self.ontospy_graph.stats(),
            "sources": self.ontospy_graph.sources,
            "ontologies": self.ontospy_graph.all_ontologies,
            "classes": self.ontospy_graph.all_classes,
            "properties": self.ontospy_graph.all_properties,
            "objproperties": self.ontospy_graph.all_properties_object,
            "dataproperties": self.ontospy_graph.all_properties_datatype,
            "annotationproperties": self.ontospy_graph.all_properties_annotation,
            "skosConcepts": self.ontospy_graph.all_skos_concepts,
            "individuals": self.ontospy_graph.all_individuals,
        }

        return context_data

    def _save2File(self, contents, filename, path):
        filename = os.path.join(path, filename)
        f = open(filename, "wb")
        f.write(contents)  # python will convert \n to os.linesep
        f.close()  # you can omit in most cases as the destructor will call it
        url = "file://" + filename
        return url

    def checkOutputPath(self, output_path):
        """
        Create or clean up output path
        """
        if not output_path:
            # output_path = self.output_path_DEFAULT
            output_path = os.path.join(
                self.output_path_DEFAULT, slugify(str(self.title))
            )
        if os.path.exists(output_path):
            shutil.rmtree(output_path)
        os.makedirs(output_path)
        return output_path

    def highlight_code(self, ontospy_entity):
        """
        produce an html version of Turtle code with syntax highlighted
        using Pygments CSS
        """
        try:
            pygments_code = highlight(
                ontospy_entity.rdf_source(), TurtleLexer(), HtmlFormatter()
            )
            pygments_code_css = HtmlFormatter().get_style_defs(".highlight")
            return {
                "pygments_code": pygments_code,
                "pygments_code_css": pygments_code_css,
            }
        except Exception as e:
            printDebug("Error: Pygmentize Failed", "red")
            return {}

