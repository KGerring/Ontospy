# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
ONTOSPY
Copyright (c)  __Michele Pasin__ <http://www.michelepasin.org>.
All rights reserved.

"""

import datetime
import optparse
import os
import os.path
import platform
import shutil
import subprocess
import sys
import time

import rdflib
import requests
from colorama import Fore
from colorama import Style

from . import *
from .manager import *
from .manager import get_localontologies, get_home_location, get_or_create_home_repo
from .ontospy import Ontospy
from .utils import *
from .utils import printDebug, printInfo



try:
    import pickle
except ImportError:
    import pickle as cPickle

try:
    import urllib.request, urllib.error, urllib.parse
except ImportError:
    # print("python3")
    import urllib.request
    from urllib.request import urlopen

try:
    from urllib.parse import quote  # Python 2.X
except ImportError:
    from urllib.parse import quote  # Python 3+

try:
    from configparser import SafeConfigParser
except ImportError:  # python3
    from configparser import SafeConfigParser

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass


# ===========
# ACTIONS FIRED FROM THE SHELL OR COMMAND LINE
# note: all actions are loaded in ontospy.py and called from other modules as 'ontospy.action_bootstrap' etc...
# ===========


def action_analyze(
    sources,
    endpoint=None,
    print_opts=False,
    verbose=False,
    extra=False,
    raw=False,
    individuals=False,
    format="",
):
    """
    Load up a model into ontospy and analyze it
    """
    ut.printDebug("Parsing ...", fg="white")
    for x in sources:
        ut.printInfo(f"# {str(x)}", fg="white")
    ut.printInfo("")

    if extra:
        hide_base_schemas = False
        hide_implicit_types = False
        hide_implicit_preds = False
    else:
        hide_base_schemas = True
        hide_implicit_types = True
        hide_implicit_preds = True

    if individuals:
        hide_individuals = False
    else:
        hide_individuals = True

    if raw:
        o = Ontospy(
            uri_or_path=sources, verbose=verbose, rdf_format=format, build_all=False
        )
        s = o.serialize()
        ut.printInfo(s)
        return
    elif endpoint:
        g = Ontospy(
            rdf_format=format,
            sparql_endpoint=sources[0],
            verbose=verbose,
            hide_base_schemas=hide_base_schemas,
            hide_implicit_types=hide_implicit_types,
            hide_implicit_preds=hide_implicit_preds,
            hide_individuals=hide_individuals,
        )
        ut.printDebug("Extracting classes info")
        g.build_classes()
        ut.printDebug("..done")
        ut.printDebug("Extracting properties info")
        g.build_properties()
        ut.printDebug("..done")
        if not hide_individuals:
            ut.printDebug(
                "Extracting individuals info (WARNING - on Sparql endpoints this could lead to very long performance times"
            )
            g.build_individuals()
            ut.printDebug("..done")
    else:
        g = Ontospy(
            uri_or_path=sources,
            rdf_format=format,
            verbose=verbose,
            hide_base_schemas=hide_base_schemas,
            hide_implicit_types=hide_implicit_types,
            hide_implicit_preds=hide_implicit_preds,
            hide_individuals=hide_individuals,
        )

    if len(g.rdflib_graph):
        ut.shellPrintOverview(g, print_opts)


def action_reveal_library():
    path = get_home_location()
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def action_serialize(source, out_fmt="turtle", verbose=False):
    """
    Util: render RDF into a different serialization
    valid options are: xml, n3, turtle, nt, pretty-xml, json-ld
    """

    o = Ontospy(uri_or_path=source, verbose=verbose, build_all=False)
    s = o.serialize(out_fmt)
    ut.printInfo(s)


def action_jsonld_playground(source_path, verbose=False):
    """
    Util: sends a json-ld file to the awesome https://json-ld.org/playground/
    """
    import webbrowser

    BASE_URL = "https://json-ld.org/playground/#startTab=tab-expanded&json-ld="
    my_file_handle = None

    ut.printDebug(f"Preparing... : {str(source_path)}", "comment")

    try:
        my_file_handle = open(source_path)
    except IOError:
        ut.printDebug(
            "------------------\nFile not found or path is incorrect", "important"
        )

    if my_file_handle:

        webbrowser.open(BASE_URL + quote(my_file_handle.read()))


def action_listlocal(all_details=True):
    "select a file from the local repo"

    options = get_localontologies()

    counter = 1
    # ut.printDebug("------------------", 'comment')
    if not options:
        ut.printDebug(
            "Your local library is empty. Use 'ontospy lib --bootstrap' to add some ontologies to it."
        )
        return
    else:
        if all_details:
            _print_table_ontologies()
        else:
            _print2cols_ontologies()

        while True:
            ut.printDebug(
                "------------------\nSelect a model by typing its number: (enter=quit)",
                "important",
            )
            var = eval(input())
            if var == "" or var == "q":
                return None
            else:
                try:
                    _id = int(var)
                    ontouri = options[_id - 1]
                    # ut.printDebug("\nYou selected:", "comment")
                    ut.printDebug(
                        "---------\nYou selected: " + ontouri + "\n---------", "green"
                    )
                    return ontouri
                except:
                    ut.printDebug("Please enter a valid option.", "comment")
                    continue


def _print2cols_ontologies():
    ontologies = get_localontologies()

    if ontologies:
        ut.printDebug("------------", "tip")
        counter = 0
        out = []
        for x in ontologies:
            counter += 1
            out += [f"[{str(counter)}] {x}"]
        ut.pprint2columns(out, max_length=60)


def _print_table_ontologies():
    """
    list all local files
    2015-10-18: removed 'cached' from report
    2016-06-17: made a subroutine of action_listlocal()
    """
    ontologies = get_localontologies()
    ONTOSPY_LOCAL_MODELS = get_home_location()

    if ontologies:
        ut.printDebug("")
        temp = []
        from collections import namedtuple

        Row = namedtuple("Row", ["N", "Added", "File"])
        # Row = namedtuple('Row',['N','Added','Cached', 'File'])
        counter = 0
        for file in ontologies:
            counter += 1
            _counter = str(counter)
            # name = Style.BRIGHT + file + Style.RESET_ALL
            name = click.style(file, fg="green")
            try:
                mtime = os.path.getmtime(ONTOSPY_LOCAL_MODELS + "/" + file)
            except OSError:
                mtime = 0
            last_modified_date = str(datetime.datetime.fromtimestamp(mtime))

            # cached = str(os.path.exists(ONTOSPY_LOCAL_CACHE + "/" + file + ".pickle"))
            temp += [Row(_counter, last_modified_date, name)]
        ut.pprinttable(temp)
        ut.printDebug("")
    return


def action_import(location: str, verbose=True):
    """
    Import files into the local repo
    """

    location = str(location)  # prevent errors from unicode being passed

    # 1) extract file from location and save locally
    ONTOSPY_LOCAL_MODELS = get_home_location()
    fullpath = ""

    try:
        if location.startswith("www."):  # support for lazy people
            location = f"http://{str(location)}"
            
        if location.startswith("http"):
            headers = {"Accept": "application/rdf+xml"}
            try:
                # Py2
                req = urllib.request.Request(location, headers=headers)
                res = urllib.request.urlopen(req)
            except:
                # Py3
                req = urllib.request.Request(location, headers=headers)
                res = urlopen(req)
            final_location = res.geturl()  # after 303 redirects
            ut.printDebug(f"Saving data from <{final_location}>", "green")
            # filename = final_location.split("/")[-1] or final_location.split("/")[-2]
            filename = location.replace("http://", "").replace("/", "_")
            if not filename.lower().endswith((".rdf", ".owl", ".rdfs", ".ttl", ".n3")):
                filename = filename + ".rdf"
            fullpath = ONTOSPY_LOCAL_MODELS + "/" + filename  # 2016-04-08
            # fullpath = ONTOSPY_LOCAL_MODELS + filename

            # print("==DEBUG", final_location, "**", filename,"**", fullpath)

            file_ = open(fullpath, "wb")
            file_.write(res.read())
            file_.close()
        else:
            if os.path.isfile(location):
                filename = location.split("/")[-1] or location.split("/")[-2]
                fullpath = ONTOSPY_LOCAL_MODELS + "/" + filename
                shutil.copy(location, fullpath)
            else:
                raise ValueError("The location specified is not a file.")
    except:
        ut.printDebug(
            "Error retrieving file. Please make sure <%s> is a valid location."
            % location,
            "important",
        )
        if os.path.exists(fullpath):
            os.remove(fullpath)
        return None

    try:
        g = Ontospy(fullpath, verbose=verbose)
        # ut.printDebug("----------")
    except:
        g = None
        if os.path.exists(fullpath):
            os.remove(fullpath)
        ut.printDebug(
            "Error parsing file. Please make sure %s contains valid RDF." % location,
            "important",
        )

    if g:
        ut.printDebug("Caching...", "red")
        do_pickle_ontology(filename, g)
        ut.printDebug("----------\n...completed!", "important")

    # finally...
    return g



def action_import_folder(location):
    """Try to import all files from a local folder"""

    if os.path.isdir(location):
        onlyfiles = [
            f for f in os.listdir(location) if os.path.isfile(os.path.join(location, f))
        ]
        for file in onlyfiles:
            if not file.startswith("."):
                filepath = os.path.join(location, file)
                ut.printDebug("\n---------\n" + filepath + "\n---------", fg="red")
                return action_import(filepath)
    else:
        ut.printDebug("Not a valid directory", "important")
        return None


def action_webimport(hrlinetop=False):
    """select from the available online directories for import"""
    DIR_OPTIONS = {1: "http://lov.okfn.org", 2: "http://prefix.cc/popular/"}
    selection = None
    while True:
        if hrlinetop:
            ut.printDebug("----------")
        text = "Please select which online directory to scan: (enter=quit)\n"
        for x in DIR_OPTIONS:
            text += f"{x:d}) {DIR_OPTIONS[x]}\n"
        var = eval(input(text + "> "))
        if var == "q" or var == "":
            return None
        else:
            try:
                selection = int(var)
                test = DIR_OPTIONS[selection]  # throw exception if number wrong
                break
            except:
                ut.printDebug("Invalid selection. Please try again.", "important")
                continue

    ut.printDebug("----------")
    text = "Search for a specific keyword? (enter=show all)\n"
    var = eval(input(text + "> "))
    keyword = var

    try:
        if selection == 1:
            _import_LOV(keyword=keyword)
        elif selection == 2:
            _import_PREFIXCC(keyword=keyword)
    except:
        ut.printDebug("Sorry, the online repository seems to be unreachable.")

    return True


def _import_LOV(
    baseuri="http://lov.okfn.org/dataset/lov/api/v2/vocabulary/list", keyword=""
):
    """
    2016-03-02: import from json list
    """

    ut.printDebug(f"----------\nReading source... <{baseuri}>")
    query = requests.get(baseuri, params={})
    all_options = query.json()
    options = []

    # pre-filter if necessary
    if keyword:
        for x in all_options:
            if (
                keyword in x["uri"].lower()
                or keyword in x["titles"][0]["value"].lower()
                or keyword in x["nsp"].lower()
            ):
                options.append(x)
    else:
        options = all_options

    ut.printDebug("----------\n%d results found.\n----------" % len(options))

    if options:
        # display:
        counter = 1
        for x in options:
            uri, title, ns = x["uri"], x["titles"][0]["value"], x["nsp"]
            # print("%s ==> %s" % (d['titles'][0]['value'], d['uri']))
            ut.printDebug(
                click.style(f"[{counter:d}]", fg="blue")
                + click.style(uri + " ==> ", fg="black")
                + click.style(title, fg="red"),
                err=True,
            )

            counter += 1

        while True:
            var = eval(
                input(
                    Style.BRIGHT
                    + "=====\nSelect ID to import: (q=quit)\n"
                    + Style.RESET_ALL
                )
            )
            if var == "q":
                break
            else:
                try:
                    _id = int(var)
                    ontouri = options[_id - 1]["uri"]
                    ut.printDebug(
                        Fore.RED
                        + "\n---------\n"
                        + ontouri
                        + "\n---------"
                        + Style.RESET_ALL
                    )
                    action_analyze([ontouri])
                    if click.confirm(
                        "=====\nDo you want to save to your local library?"
                    ):
                        action_import(ontouri)
                    return
                except:
                    ut.printDebug("Error retrieving file. Import failed.")
                    continue


SOURCE = "http://prefix.cc/popular/all.file.vann"

def _import_PREFIXCC(keyword=""):
    """
    List models from web catalog (prefix.cc) and ask which one to import
    2015-10-10: originally part of main ontospy; now standalone only
    2016-06-19: eliminated dependency on extras.import_web
    """
    SOURCE = "http://prefix.cc/popular/all.file.vann"
    options = []

    ut.printDebug("----------\nReading source...")
    g = Ontospy(SOURCE, verbose=False)

    for x in g.all_ontologies:
        if keyword:
            if keyword in str(x.prefix).lower() or keyword in str(x.uri).lower():
                options += [(str(x.prefix), str(x.uri))]
        else:
            options += [(str(x.prefix), str(x.uri))]

    ut.printDebug(f"----------\n{len(options):d} results found.")

    counter = 1
    for x in options:
        ut.printDebug(
            Fore.BLUE
            + Style.BRIGHT
            + "[%d]" % counter
            + Style.RESET_ALL
            + x[0]
            + " ==> "
            + Fore.RED
            + x[1]
            + Style.RESET_ALL
        )
        # ut.printDebug(Fore.BLUE + x[0] + " ==> " + x[1])
        counter += 1

    while True:
        var = eval(
            input(
                Style.BRIGHT
                + "=====\nSelect ID to import: (q=quit)\n"
                + Style.RESET_ALL
            )
        )
        if var == "q":
            break
        else:
            try:
                _id = int(var)
                ontouri = options[_id - 1][1]
                ut.printDebug(
                    Fore.RED
                    + "\n---------\n"
                    + ontouri
                    + "\n---------"
                    + Style.RESET_ALL
                )
                action_analyze([ontouri])
                if click.confirm("=====\nDo you want to save to your local library?"):
                    action_import(ontouri)
                return
            except:
                ut.printDebug("Error retrieving file. Import failed.")
                continue


def action_bootstrap(verbose=False):
    """Bootstrap the local REPO with a few cool ontologies"""
    ut.printDebug("The following ontologies will be imported:")
    ut.printDebug("--------------")
    count = 0
    for s in BOOTSTRAP_ONTOLOGIES:
        count += 1
        ut.printInfo(count, "<%s>" % s)

    ut.printDebug("--------------")
    ut.printDebug("Note: this operation may take several minutes.")
    ut.printDebug("Proceed? [Y/N]")
    var = eval(input())
    if var == "y" or var == "Y":
        for uri in BOOTSTRAP_ONTOLOGIES:
            try:
                ut.printDebug("--------------")
                action_import(uri, verbose)
            except:
                ut.printDebug("OPS... An Unknown Error Occurred - Aborting Installation")
        ut.printDebug("\n==========\n" + "Bootstrap command completed.", "important")
        return True
    else:
        ut.printDebug("--------------")
        ut.printDebug("Goodbye")
        return False


def action_update_library_location(_location):
    """
    Sets the folder that contains models for the local library
    @todo: add options to move things over etc..
    note: this is called from 'manager'
    """

    # if not(os.path.exists(_location)):
    # 	os.mkdir(_location)
    # 	ut.printDebug("Creating new folder..", "comment")

    ut.printDebug("Old location: '%s'" % get_home_location(), "comment")

    if os.path.isdir(_location):

        config = SafeConfigParser()
        config_filename = ONTOSPY_LOCAL + "/config.ini"
        config.read(config_filename)
        if not config.has_section("models"):
            config.add_section("models")

        config.set("models", "dir", _location)
        with open(config_filename, "w") as f:
            config.write(f)  # note: this does not remove previously saved settings

        return _location
    else:
        return None


def action_cache_reset():
    """
    Delete all contents from cache folder
    Then re-generate cached version of all models in the local repo

    """
    ut.printDebug("""The existing cache will be erased and recreated.""")
    ut.printDebug(
        """This operation may take several minutes, depending on how many files exist in your local library."""
    )
    ONTOSPY_LOCAL_MODELS = get_home_location()
    # https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder-in-python
    # NOTE This will not only delete the contents but the folder itself as well.
    shutil.rmtree(ONTOSPY_LOCAL_CACHE_TOP)

    var = eval(input(Style.BRIGHT + "=====\nProceed? (y/n) " + Style.RESET_ALL))
    if var == "y":
        repo_contents = get_localontologies()
        ut.printInfo(
            Style.BRIGHT
            + "\n=====\n%d ontologies available in the local library\n====="
            % len(repo_contents)
            + Style.RESET_ALL
        )
        for onto in repo_contents:
            fullpath = ONTOSPY_LOCAL_MODELS + "/" + onto
            try:
                ut.printInfo(Fore.RED + "\n=====\n" + onto + Style.RESET_ALL)
                ut.printInfo("Loading graph...")
                g = Ontospy(fullpath)
                ut.printInfo("Loaded ", fullpath)
            except:
                g = None
                ut.printDebug(
                    "Error parsing file. Please make sure %s contains valid RDF."
                    % fullpath
                )

            if g:
                ut.printInfo("Caching...")
                do_pickle_ontology(onto, g)

        ut.printDebug(Style.BRIGHT + "===Completed===" + Style.RESET_ALL)

    else:
        ut.printDebug("Goodbye")


def actions_delete():
    """
    DEPRECATED (v 1.9.4)
    delete an ontology from the local repo
    """

    filename = action_listlocal()

    ONTOSPY_LOCAL_MODELS = get_home_location()

    if filename:
        fullpath = ONTOSPY_LOCAL_MODELS + filename

        if os.path.exists(fullpath):
            var = eval(input("Are you sure you want to delete this file? (y/n)"))
            if var == "y":
                os.remove(fullpath)
                ut.printDebug("Deleted %s" % fullpath, "important")
                cachepath = ONTOSPY_LOCAL_CACHE + filename + ".pickle"
                # @todo: do this operation in /cache...
                if os.path.exists(cachepath):
                    os.remove(cachepath)
                    ut.printDebug("---------")
                    ut.printDebug("File deleted [%s]" % cachepath, "important")

                return True
            else:
                ut.printDebug("Goodbye")

    return False


def action_erase():
    """
    DEPRECATED (v 1.9.4)
    just a wrapper.. possibly to be extended in the future
    """
    get_or_create_home_repo(reset=True)
    return True


def action_visualize(
    args,
    fromshell=False,
    path=None,
    title="",
    viztype="",
    theme="",
    preflabel="",
    preflang="",
    extra=False,
    individuals=False,
    verbose=False,
):
    """
    export model into another format eg html, d3 etc...
    <fromshell> : the local name is being passed from ontospy shell
    """

    from ..ontodocs.builder import VISUALIZATIONS_LIST
    from ..ontodocs.builder import ask_visualization
    from ..ontodocs.builder import build_visualization
    from ..ontodocs.builder import select_visualization

    if fromshell:
        ontouri = args
        islocal = True
    else:
        ontouri = args[0]
        islocal = False

    if extra:
        hide_base_schemas = False
        hide_implicit_types = False
        hide_implicit_preds = False
    else:
        hide_base_schemas = True
        hide_implicit_types = True
        hide_implicit_preds = True

    if individuals:
        hide_individuals = False
    else:
        hide_individuals = True

    # select a visualization
    if viztype:
        viztype = select_visualization(viztype)
    else:
        viztype = ask_visualization()
        if viztype == "":
            return None
        # raise SystemExit, 1

    # 2017-01-23: bypass pickled stuff as it has wrong counts etc..
    # get ontospy graph
    ut.printDebug("Loading graph...", dim=True)

    g = Ontospy(
        ontouri,
        verbose=verbose,
        pref_title=preflabel,
        pref_lang=preflang,
        hide_base_schemas=hide_base_schemas,
        hide_implicit_types=hide_implicit_types,
        hide_implicit_preds=hide_implicit_preds,
        hide_individuals=hide_individuals,
    )

    # put viz in home folder by default: <ontouri>/<viztype>/files..
    if not path:
        from os.path import expanduser

        home = expanduser("~")
        onto_path = slugify(str(ontouri))
        viz_path = slugify(str(VISUALIZATIONS_LIST[viztype]["Title"]))
        path = os.path.join(home, "ontospy-viz/" + onto_path + "/" + viz_path)
        if not os.path.exists(path):
            os.makedirs(path)

    # url  = build_viz(ontouri, g, viztype, path)
    ut.printDebug("Building visualization...", dim=True)
    url = build_visualization(ontouri, g, viztype, path, title, theme)

    return url
