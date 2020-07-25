from pathlib import Path

# Find the parent directory of this file and recursively search for python files that follow problem naming scheme
problems_dir = Path(__file__).parent
modules = problems_dir.glob("**/p[0-9][0-9][0-9].py")

# Remove the .py, sort by problem # and add to __all__
__all__ = [module.stem for module in sorted(modules, key=lambda m: m.stem)]
