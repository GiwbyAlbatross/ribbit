#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2024  <giwby@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR ANY PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details. If you can find one :)
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
# 

import os
import flask

app = flask.Flask(__name__)

# register routes etc.

if __name__ == '__main__':
    app.run('0.0.0.0', os.environ.get('RIBBIT_PORT', '8080'), debug=__debug__, threaded=True)