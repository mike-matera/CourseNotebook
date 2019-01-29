import importlib.util
import uuid 
from pathlib import Path

anon_modules = {}
anon_files = {}

def load(filename):
    path = Path(filename).resolve()
    
    mod_uuid = str(uuid.uuid4())
    loaded_mod = {}
    
    loaded_mod['path'] = path
    loaded_mod['spec'] = importlib.util.spec_from_file_location(mod_uuid, path) 
    loaded_mod['module'] = importlib.util.module_from_spec(loaded_mod['spec'])
    loaded_mod['result'] = loaded_mod['spec'].loader.exec_module(loaded_mod['module'])

    anon_modules[mod_uuid] = loaded_mod
    anon_files[path] = loaded_mod
    
    if anon_modules[mod_uuid]['module'].__doc__ is None:
        raise ValueError(f'Your Python file {filename} does not have a docstring!')

    return loaded_mod


def has_docstring(filename):
    mod = load(filename)
    return mod.__doc__ is not None
