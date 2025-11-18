"""git-dit package

Minimal package metadata and exported version.
"""

__version__ = "1.0.0"

from . import core  # re-export for convenience (stubs)

__all__ = ["__version__", "core"]
