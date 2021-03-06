# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SMC
                                 A QGIS plugin
 This plugin selects every feature inside the current extent
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-07-17
        copyright            : (C) 2020 by Infogeo54
        email                : hvitoux@departement54.fr
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SMC class from file SMC.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .smc import SMC
    return SMC(iface)
