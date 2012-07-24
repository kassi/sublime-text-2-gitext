import sublime, sublime_plugin
from git import *

class GitAddAllCommand(GitTextCommand):
    def run(self, edit):
        self.run_command(['git', 'add', '--all'], working_dir = git_root(self.get_working_dir()))
