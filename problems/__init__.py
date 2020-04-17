from os.path import dirname, basename, isfile, join
import glob
import re

reg = re.compile(r"([0-9]+)_.+")
# Dynamically Load all problems and make sure they are sorted by problem #
modules = glob.glob(join(dirname(__file__), "*.py"))
modules = {int(reg.search(module).group(1)): module for module in modules if not module.endswith('__init__.py')}
__all__ = [basename(modules[f])[:-3] for f in sorted(modules) if isfile(modules[f])]