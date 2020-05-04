# The following comment should be removed at some point in the future.
# mypy: disallow-untyped-defs=False

from __future__ import absolute_import

from optparse import Values

import pip._vendor.requests as requests

from pip._internal.cli.base_command import Command
from pip._internal.cli.status_codes import SUCCESS
from pip._internal.exceptions import CommandError
from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import Any, List

json_url_format = "https://pypi.org/pypi/{}/json".format


class ThankCommand(Command):

    def __init__(self, *args, **kw):
        super(ThankCommand, self).__init__(*args, **kw)

    def run(self, options, args):
        # type: (Values, List[Any]) -> int
        if not args:
            raise CommandError('Missing package argument.')

        query = args[0]

        # Need to add exception handling
        resp = requests.get(json_url_format(query))
        json_data = resp.json()

        funding = json_data["info"]["project_urls"].get("Funding")

        print("Funding link: {}".format(funding))

        print("You just thanked {}".format(query))

        return SUCCESS
