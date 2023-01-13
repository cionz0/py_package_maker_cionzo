""" This module is a module

    :synopsis: A useful module indeed.
    :position: src.py_package_maker_cionzo.license.license_manager
    :author: cionzo <cionzo@filotrack.com>
    :created on: 12/01/23
    :project: py_package_maker_cionzo
 """
import pathlib
from datetime import date
from enum import Enum

SKELETON_FOLDER = pathlib.Path(__file__).resolve().parent / "skeletons"


class License(str, Enum):
    MIT = "mit"
    GNU_GPLv3 = "GNU_GPLv3"
    # COMMUNITY = "community"
    # CUSTOM = "custom_link"


LICENSE_FILES = {
    License.MIT: SKELETON_FOLDER / f"{License.MIT}.txt",
    License.GNU_GPLv3: SKELETON_FOLDER / f"{License.GNU_GPLv3}.txt"
    # License.COMMUNITY:  SKELETON_FOLDER / f"{License.COMMUNITY}.txt",
}


def add_license(path: pathlib.PosixPath, lic: License, name: str):
    if lic is None:
        return
    # if lic == License.CUSTOM:
    #     print("not yet implemented")



    with LICENSE_FILES[lic].open() as _skeleton:
        content = _skeleton.read()
        content = content.replace("_THIS_YEAR_", f"{date.today().year}")
        content = content.replace("_FULLNAME_", name)

    with (path / "LICENSE").open('w') as lic_file:
        lic_file.write(content)
