'''

Copyright (C) 2017 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2016-2017 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from scif.logger import bot
import sys
import pwd
import os


def main(args,parser,subparser):

    from scif.main import ScifRecipe
    apps = args.recipe

    if len(apps) == 0:
        bot.error("You must provide a recipe (.scif) file to install.")
        sys.exit(1)

    recipe = apps.pop(0)

    if not os.path.exists(recipe):
        bot.error("Cannot find recipe file %s" %recipe)
        sys.exit(1)

    if len(apps) == 0:
        apps = None

    client = ScifRecipe(recipe) # writable is True

    # Preview the entire recipe, or the apps chosen
    client.install(apps)
