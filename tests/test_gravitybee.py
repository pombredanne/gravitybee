# test_gravitybee.py

import pytest
import glob
import os

from subprocess import check_output

from gravitybee import Arguments, PackageGenerator

@pytest.fixture
def arguments():
    """Returns an Arguments instance using the included app"""
    return Arguments(
        src_dir="src",
        extra_data=["gbextradata"],
        verbose=True,
        pkg_dir=os.path.join("tests", "gbtestapp"),
        clean=True)

def test_generation(arguments):
    """ Tests running the executable. """
    pg = PackageGenerator(arguments)
    generated_okay = pg.generate()

    assert generated_okay

def test_executable(arguments):
    """ Tests running the executable. """
    pg = PackageGenerator(arguments)
    generated_okay = pg.generate()
    if generated_okay:
        files = glob.glob('gbtestapp-4.2.6-standalone*')

        cmd_output = check_output(os.path.join('.',files[0]))
        compare_file = open(os.path.join("tests", "gbtestapp", "correct_stdout.txt"),"rb").read()

        assert cmd_output == compare_file
    else:
        assert False

@pytest.fixture
def defaults():
    if not os.getcwd().endswith(os.path.join("tests", "gbtestapp")):
        os.chdir(os.path.join("tests", "gbtestapp"))
    return Arguments()

def test_clean(defaults):
    assert not defaults.clean

def test_pkg_dir(defaults):
    assert defaults.pkg_dir == '.'

def test_src_dir(defaults):
    assert defaults.src_dir is None

def test_name_format(defaults):
    assert defaults.name_format == '{an}-{v}-standalone-{os}-{m}'

def test_extra_data(defaults):
    assert defaults.extra_data is None

def test_work_dir(defaults):
    assert defaults.work_dir[:11] == 'gb_workdir_'

def test_console_script(defaults):
    assert defaults.console_script == 'gbtestapp'

def test_app_version(defaults):
    assert defaults.app_version == '4.2.6'

def test_app_name(defaults):
    assert defaults.app_name == 'gbtestapp'

def test_pkg_name(defaults):
    assert defaults.pkg_name == 'gbtestapp'