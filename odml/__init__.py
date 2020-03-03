import warnings

from sys import version_info as _python_version

from .doc import BaseDocument as Document
from .dtypes import DType
from .fileio import load, save, display
from .info import VERSION
from .property import BaseProperty as Property
from .section import BaseSection as Section
from .tools.parser_utils import SUPPORTED_PARSERS as PARSERS


def _format_warning(warn_msg, *args, **kwargs):
    """
    Used to provide users with deprecation warnings via the warnings module
    but without spamming them with full stack traces.
    """
    final_msg = "%s\n" % str(warn_msg)
    # If available add category name to the message
    if args and hasattr(args[0], "__name__"):
        final_msg = "%s: %s" % (args[0].__name__, final_msg)

    return final_msg


# Monkey patch formatting 'warnings' messages for the whole module.
warnings.formatwarning = _format_warning

if _python_version.major < 3:
    msg = "Python 2 has been deprecated.\n\todML support for Python 2 will be dropped August 2020."
    warnings.warn(msg, category=DeprecationWarning, stacklevel=2)
elif _python_version.major == 3 and _python_version.minor < 6:
    msg = "The '%s' package is not tested with your Python version. " % __name__
    msg += "\n\tPlease consider upgrading to the latest Python distribution."
    warnings.warn(msg)

__version__ = VERSION
