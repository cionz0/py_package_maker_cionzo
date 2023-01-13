""" This module is a module

    :synopsis: A useful module indeed.
    :position: src.py_package_maker_cionzo.pyprojecttoml.tomler
    :author: cionzo <cionzo@filotrack.com>
    :created on: 12/01/23
    :project: py_package_maker_cionzo
 """
import pathlib

SKELETON = pathlib.Path(__file__).resolve().parent / "skeleton" / "_pyproject.toml"

def create_skeleton(root_folder, project_name, user):
    with SKELETON.open() as _skeleton:
        content = _skeleton.read()
        content = content.replace("_THEPROJECT_", project_name)
        content = content.replace("_THEUSER_", user.name)
        content = content.replace("_THEEMAIL_", user.email)

    with (root_folder / "pyproject.toml").open('w') as outfile:
        outfile.write(content)
