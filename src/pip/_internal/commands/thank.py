from pip._internal.cli.base_command import Command
#from pip._internal.cli
from pip._internal.exceptions import CommandError


class ThankCommand(Command):

    def __init__(self, *args, **kw):
        super(ThankCommand, self).__init__(*args, **kw)
#        self.cmd_opts.add_option(
#            '-i

    def run(self, options, args):
            if not args:
                raise CommandError('Missing package argument.')
            query = args[0]
            print(f"You just thanked {query}")

            