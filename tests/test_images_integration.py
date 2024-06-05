import main

import pathlib
import shutil

import pytest


@pytest.fixture(scope="session")
def default_manga(tmp_path_factory):
    test_path = tmp_path_factory.mktemp("data")
    shutil.copytree('tests/static/happy_images', test_path  / 'manga')
    return test_path


def test_images(monkeypatch, default_manga):
    responses = iter([str(default_manga), 'images', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    main.main()

    assert pathlib.Path(f'{default_manga}/PDFs/manga/chapter 1.pdf').is_file()

