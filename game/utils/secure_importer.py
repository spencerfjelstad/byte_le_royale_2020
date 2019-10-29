from game.config import ALLOW_ONLY_MODE, ALLOWED_MODULES, RESTRICTED_MODULES, Debug, DebugLevel
import importlib


# replaces builtin import function to prevent clients from importing modules they shouldn't
def secure_importer(module_to_import, globals=None, locals=None, fromlist=(), level=0):
    # Determine name of calling module
    frommodule = globals['__name__'] if globals else None
    debug(f"{frommodule} attempting to import {module_to_import}")

    if validate_import(module_to_import):
        # Module is following restrictions. Continue normal functionality
        return importlib.__import__(module_to_import, globals, locals, fromlist, level)
    else:
        # Module cannot be imported legally
        raise ImportError("Attempted invalid import. Suspected the client imported something they shouldn't have.")


# Applies validation to the import accessed by the client
def validate_import(module_name):

    if module_name in ALLOWED_MODULES:
        # skip validation, since it is specifically allowed
        return True
    elif ALLOW_ONLY_MODE:
        # If it's not in the allowed modules during allow_only_mode, then validation fails
        return False

    # Check against restricted modules
    # break apart module into module and all submodules
    sections = module_name.split(".")
    accessed_modules = list()
    # A module "game.common.client" will check "game", "game.common", and "game.common.client"
    for i in range(len(sections)):
        accessed_modules.append(".".join(sections[:i+1]))

    # check each submodule being imported
    for module in accessed_modules:
        if module in RESTRICTED_MODULES:
            return False

    # all tests passed, successful validation
    return True


# Debug print statement
def debug(*args):
    if Debug.level >= DebugLevel.engine:
        print('Engine: ', end='')
        print(*args)