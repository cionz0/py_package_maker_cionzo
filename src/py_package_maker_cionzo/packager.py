""" This module is a module

    :synopsis: A useful module indeed.
    :position: src.py_package_maker_cionzo.packager
    :author: cionzo <cionzo@filotrack.com>
    :created on: 12/01/23
    :project: py_package_maker_cionzo
 """
import argparse
import re
from collections import namedtuple
from pathlib import Path

from license import license_manager
from .pyprojecttoml import tomler

User = namedtuple('User', "name email")
ENDING_MESSAGE = '\nPlease do not forget to review and update:' \
                 '\n- pyproject.toml and it main sections' \
                 '\n\t[build-system]/requires\tfor your dependencies' \
                 '\n\t[project.urls] and its children for correct pointing' \
                 '\n- README.md' \
                 '\n\nAfter that: ' \
                 '\n\t- feel free to put your code in src folder, and' \
                 '\n\t- run the build'

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog='packager',
        description='Creates the skeleton for a python package.',
        epilog='This script has to be run from the root folder of the project that you want to turn into a package.',
        usage=argparse.SUPPRESS)

    parser.add_argument("-l", "--license", choices=[lic.value for lic in license_manager.License], default=None,
                        dest='license', help="Specifies the license to be used. See https://choosealicense.com")

    root_folder = Path('.').absolute()
    project_name = root_folder.name

    try:
        args = parser.parse_args()
        user_name = input("please type your (nick)name: ")

        pattern = "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
        compiled_pattern = re.compile(pattern)
        match = None
        while match is None:
            email = input("please type your email address: ")
            match = compiled_pattern.fullmatch(email)
            if match is None:
                print("a valid email address is required")




        # STEP 1: fill license file
        license_manager.add_license(root_folder, args.license, user_name)

        # STEP 2: create test folder
        test_folder = root_folder / "tests"
        test_folder.mkdir(exist_ok=True)

        # STEP 3: create pyproject.toml
        tomler.create_skeleton(root_folder, project_name, user=User(user_name, email))

        # STEP 4: create README.md
        with (root_folder / "README.md").open('w') as outfile:
            outfile.write("")

        # STEP 5: init src folder
        init_file_path = root_folder / "src" / project_name / "__init__.py"
        init_file_path.parent.mkdir(parents=True, exist_ok=True)

        with init_file_path.open('w') as outfile:
            outfile.write("")

        print(ENDING_MESSAGE)
    except SystemExit:
        parser.print_help()

        raise
    # except argparse.ArgumentError. as arg_error:
    #     print("seeeeellallero")
    #     parser.print_help()
    #     parser.print_usage()
    #     exit(1)

    # if len(unknown_args) > 0:
    #     parser.print_usage()
    #
    #     exit(1)
