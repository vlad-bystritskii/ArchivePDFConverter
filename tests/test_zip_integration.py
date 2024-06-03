import main

import pathlib
import shutil

import pytest

@pytest.fixture(scope="session")
def default_manga_zip(tmp_path_factory):
    test_path = tmp_path_factory.mktemp("data")
    shutil.copy('tests/static/happy_zip/manga.zip', test_path  / 'manga.zip')
    return test_path


def test_zip(monkeypatch, default_manga_zip):
    responses = iter([str(default_manga_zip), 'archive', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    main.main()

    assert pathlib.Path(f'{default_manga_zip}/PDFs/manga/chapter 1.pdf').is_file()

