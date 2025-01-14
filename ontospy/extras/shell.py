# !/usr/bin/env python
#  -*- coding: UTF-8 -*-


"""
ONTOSPY
Copyright (c)  __Michele Pasin__ <http://www.michelepasin.org>.
All rights reserved.

Ontospy Shell Launcher

"""

import sys
import click

from .. import *  # imports __init__
from .shell_lib import STARTUP_MESSAGE
from .shell_lib import Shell

# http://click.pocoo.org/5/arguments/
# http://click.pocoo.org/5/options/

try:
    import readline
except:
    click.secho("WARNING: ontospy shell can't without the readline library.", fg="red")
    click.secho(
        "Tip: install it with `pip install readline` (you can try pyreadline on Windows)",
        fg="green",
    )
    sys.exit(0)


def launch_shell(source=None):
    Shell()._clear_screen()
    print(STARTUP_MESSAGE)
    if source and len(source) > 1:
        click.secho("Note: currently only one argument can be passed", fg="red")
    uri = source[0] if source else None
    Shell(uri).cmdloop()
    raise SystemExit(1)


CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])

# @click.option('--source', '-s',  multiple=True, help='Load the shell with a specific graph (uri or file)')


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("source", nargs=-1)
def cli_run_shell(source=None):
    """
    This application launches the Ontospy interactive shell.

    Note: if a local path or URI of an RDF model is provided, that gets loaded into the shell by default. E.g.:

    > ontospy-shell path/to/mymodel.rdf
    """
    launch_shell(source)


if __name__ == "__main__":
    try:
        # http://stackoverflow.com/questions/32553969/modify-usage-string-on-click-command-line-interface-on-windows
        cli_run_shell(prog_name="ontospy-shell")
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
