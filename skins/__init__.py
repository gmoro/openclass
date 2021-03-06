#!/usr/bin/python
"""
OpenClass skin template and base class.

Copyright, (C) Eugeni Dodonov <eugeni@dodonov.net>, 2011

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.

"""

class Skin:
    def __init__(self, logger, gui):
        """Initializes a gui passed from the gui class.
        You MUST define all the variables which gui expects,
        otherwise bad things will happen. Trust me."""
        pass

def get_skin(logger, skin_name):
    """Converts a skin name into a valid skin"""
    skin = None
    try:
        skin_file = __import__("skins.%s" % skin_name)
        skin_class = getattr(skin_file, skin_name)
        skin = getattr(skin_class, skin_name)
    except:
        logger.exception("Trying to load skin %s" % skin_name)
    return skin

