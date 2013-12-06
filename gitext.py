import sublime, sublime_plugin
import Git.git

class GitAddAllCommand(GitTextCommand):
    def run(self, edit):
        self.run_command(['git', 'add', '--all'], working_dir = git_root(self.get_working_dir()))
