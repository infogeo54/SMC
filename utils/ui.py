from qgis.PyQt.QtWidgets import QTableWidgetItem
from qgis.PyQt.QtCore import Qt

def create_label(text):
    item = QTableWidgetItem(text)
    item.setFlags(Qt.NoItemFlags)
    item.setTextAlignment(Qt.AlignCenter)
    return item

def create_checkbox():
    item = QTableWidgetItem()
    item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
    item.setCheckState(Qt.Unchecked)
    return item

def create_rows(communes):
    rows = []
    for c in communes:
        label, checkbox = create_label(c.attribute("nom")), create_checkbox()
        rows.append(dict(label=label, checkbox=checkbox))
    return rows