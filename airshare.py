#!/usr/bin/python
"""
    ___    _           __
   /   |  (_)_________/ /_  ____ _________
  / /| | / / ___/ ___/ __ \/ __ `/ ___/ _ \
 / ___ |/ / /  (__  ) / / / /_/ / /  /  __/
/_/  |_/_/_/  /____/_/ /_/\__,_/_/   \___/

A file-sharing program for local area networks

"""

import threading
import cmd
import sys
import ftpserver as fs

share_dir = '.'

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

def run_cli():
    cl_ui = cli()
    cl_ui.cmdloop('')

def serve_files():
    authorizer = fs.DummyAuthorizer()
    perm = "elr"
    authorizer.add_anonymous(share_dir, perm=perm)
    handler = fs.FTPHandler
    handler.authorizer = authorizer
    ftpd = fs.FTPServer(('0.0.0.0', 0), handler)
    print ftpd.kport
    ftpd.serve_forever()

def main():
    global share_dir
    show_logo()
    share_dir = "."

    ui = threading.Thread(name='ui', target=run_cli)
    fs = threading.Thread(name='fs', target=serve_files)

    fs.setDaemon(True)

    fs.start()
    ui.start()

    ui.join()
    pass

if __name__ == '__main__':
    main()

