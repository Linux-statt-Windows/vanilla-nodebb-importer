#!/usr/bin/env python2.7
# -*- coding: UTF-8 -*-


"""
Author:             Michael Rong
                    <miro@electronic.works>
                    www.electronic.works

Creation Date:      2016-03-09

Copyright:          (c) 2016 Linux statt Windows
                    https://linux-statt-windows.org
"""


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# *                                                                         *
# *  Copyright (C) 2016 Linux statt Windows                                 *
# *                                                                         *
# *  'vanilla-nodebb-importer' is free software:                            *
# *  you can redistribute it and/or modify                                  *
# *  it under the terms of the GNU General Public License as published by   *
# *  the Free Software Foundation, version 3 of the License.                *
# *                                                                         *
# *  'vanilla-nodebb-importer' is distributed in the hope that it will be   *
# *  useful, but WITHOUT ANY WARRANTY; without even the implied warranty    *
# *  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the       *
# *  GNU General Public License for more details.                           *
# *                                                                         *
# *  You should have received a copy of the GNU General Public License      *
# *  along with 'vanilla-nodebb-importer'. If not, see                      *
# *  <http://www.gnu.org/licenses/>.                                        *
# *                                                                         *
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *


import sys
from Settings import *


settings = Settings()


def main():
    settings.initSettings()
    


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
