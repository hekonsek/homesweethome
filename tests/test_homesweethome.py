import os
from pytest import fixture
from homesweethome.homesweethome import SweetHome
from pathlib import Path


@fixture
def sweet_home() -> SweetHome:
    return SweetHome.create_temporary()

def test_should_create_home(sweet_home: SweetHome):
    assert sweet_home.home_dir().exists()

def test_should_write(sweet_home: SweetHome):
    sweet_home.write_setting("foo.bar", "baz")
    assert sweet_home.read_setting("foo.bar") == "baz"

def test_should_create_directory(sweet_home: SweetHome):
    directory = sweet_home.directory("some/dir")
    assert directory.exists()

def test_should_override_setting_via_env():
    sweet_home = SweetHome.create_temporary("someapp-api")
    os.environ['SOMEAPPAPI_SOME__ENV'] = 'baz'
    assert sweet_home.read_setting("some.env") == "baz"

def test_should_override_setting_via_env():
    os.environ['SOMEAPP_BASEDIR'] = '/tmp/foo'
    sweet_home = SweetHome.create_temporary("someapp")
    assert sweet_home.home_dir() == Path('/tmp/foo/.someapp')