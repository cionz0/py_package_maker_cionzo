""" This module is a module

    :synopsis: A useful module indeed.
    :position: src.py_package_maker_cionzo.builder
    :author: cionzo <cionzo@filotrack.com>
    :created on: 13/01/23
    :project: py_package_maker_cionzo
 """
import os
import pip

if __name__ == "__main__":
    # Step 1: build
    if os.name == "nt":
        python_executable = "py"
    else:
        python_executable = "python3"
    build_cmd = f"{python_executable} -m build"
    os.system(build_cmd)

