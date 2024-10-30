# tests/test_icons.py

import pytest
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication
from pytablericons import OutlineIcon

from helium.resources.icons import tablerIcon, StatusIcons

@pytest.fixture(scope="module", autouse=True)
def app():
    app = QApplication([])
    StatusIcons.initialise_icons()
    yield
    app.quit()

def test_tabler_icon():
    icon = tablerIcon(OutlineIcon.ABC, '#00bb39', size=128)
    assert isinstance(icon, QIcon)


def test_status_icons_initialisation():
    try:
        assert StatusIcons.ICONS_STATUS is not None
        for icon_name in StatusIcons.ICONS_STATUS:
            assert isinstance(StatusIcons.ICONS_STATUS[icon_name], QIcon)

        assert StatusIcons.ICONS_EXTRA is not None
        for icon_name in StatusIcons.ICONS_EXTRA:
            assert isinstance(StatusIcons.ICONS_EXTRA[icon_name], QIcon)
    except Exception as e:
        pytest.fail(f"Failed to initialise StatusIcons: {e}")