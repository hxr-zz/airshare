#!/usr/bin/python
"""
    ___    _           __
   /   |  (_)_________/ /_  ____ _________
  / /| | / / ___/ ___/ __ \/ __ `/ ___/ _ \
 / ___ |/ / /  (__  ) / / / /_/ / /  /  __/
/_/  |_/_/_/  /____/_/ /_/\__,_/_/   \___/

A file-sharing program for local area networks

"""

import ftpserver as fs
import cmd
import sys

def show_logo():
    print "    ___    _           __"
    print "   /   |  (_)_________/ /_  ____ _________"
    print "  / /| | / / ___/ ___/ __ \/ __ `/ ___/ _ \\"
    print " / ___ |/ / /  (__  ) / / / /_/ / /  /  __/"
    print "/_/  |_/_/_/  /____/_/ /_/\__,_/_/   \___/"
    print


class cli(cmd.Cmd):
    """
    A command line interpreter for airshare
    """

    def __init__(self, *args, **kwargs):
        cmd.Cmd.__init__(self, *args, **kwargs)
        self.prompt="ready> "
        self.use_rawinput=False

    def do_quit(self, arg):
        """
        Exit Airshare.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit Airshare.
        """
        print
        return True

def cli_thread():
    """
    Command line interpreter thread
    """

def main():
    show_logo()
    x = cli()
    x.cmdloop('')
    share_dir = "."
    authorizer = fs.DummyAuthorizer()
    perm = "elr"
    authorizer.add_anonymous(share_dir, perm=perm)
    handler = fs.FTPHandler
    handler.authorizer = authorizer
    ftpd = fs.FTPServer(('0.0.0.0', 0), handler)
    print ftpd.kport
    ftpd.serve_forever()
    pass

if __name__ == '__main__':
    main()

