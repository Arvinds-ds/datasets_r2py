"""[Observations](https://github.com/edwardlib/observations) provides
a one line Python API for loading standard data sets in machine
learning. It automates the process from downloading, extracting,
loading, and preprocessing data. Observations helps keep the workflow
reproducible and follow sensible standards.

Observations is a standalone Python library and must be installed
separate from Edward.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

{{function_imports}}


def remove_undocumented(module_name, allowed_exception_list=None):
  """Removes symbols in a module that are not referenced by a docstring.

  Args:
    module_name: the name of the module (usually `__name__`).
    allowed_exception_list: a list of names that should not be removed.

  Returns:
    None
  """
  import sys as _sys
  current_symbols = set(dir(_sys.modules[module_name]))
  should_have = allowed_exception_list or []
  extra_symbols = current_symbols - set(should_have)
  target_module = _sys.modules[module_name]
  for extra_symbol in extra_symbols:
    # Skip over __file__, etc. Also preserves internal symbols.
    if extra_symbol.startswith('_'):
      continue
    fully_qualified_name = module_name + '.' + extra_symbol
    delattr(target_module, extra_symbol)


# Export modules and constants.
_allowed_symbols = [
  {{allowed_symbols}}

]

# Remove all extra symbols that don't have a docstring or are not explicitly
# referenced in the whitelist.
remove_undocumented(__name__, _allowed_symbols)
