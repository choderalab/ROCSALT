"""
ROCSALT
Dual Topology Alchemical Free Energy Calculations: ROCS Input
"""

# Add imports here
from .alchemy import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
