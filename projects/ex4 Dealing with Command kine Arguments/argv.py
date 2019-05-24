from sys import argv


class CommandArgs(object):
    def __init__(self):
        self.len = len(argv)
        self.ls = {
            '-h':
            """
            -h --help   Help command for ARGV. Type -h or --help and then
                        command 'name' to get help.
            """,
            'sum':
            """
            sum         'sum' is used to sum 2 arguments. ex: sum 1 2
            """
        }

    def show(self):
        for text in self.ls.values():
            print(text)

    def invalid(self):
        print(f"\n\tInvalid command. Try -h or --help.\n")

    def get(self, command):
        text = self.ls.get(command)
        if text:
            return text
        return self.invalid()

    def prnt(self, command):
        print(self.get(command))

    def help(self):
        if self.len == 2:
            self.show()
        elif self.len == 3:
            self.prnt(argv[2])
        else:
            self.invalid()

    def check(self):
        if self.len == 1:
            self.show()
        if self.len > 1:
            if argv[1] == '-h' or argv[1] == '--help':
                self.help()


commands = CommandArgs()
commands.check()
