from os.path import dirname, basename, isfile, join
import glob
import re
import fnmatch

modules = glob.glob(join(dirname(__file__), "[0-9]*.py"))


def key(fn):
    """
    this returns the problem #
    """
    return int(basename(fn).split("_")[0])


__all__ = [basename(module)[:-3] for module in sorted(modules, key=key)]

