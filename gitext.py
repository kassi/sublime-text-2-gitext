import sublime, sublime_plugin
import Git.git

class GitAddAllCommand(Git.git.GitTextCommand):
    def run(self, edit):
        self.run_command(['git', 'add', '--all'], working_dir = Git.git.git_root(self.get_working_dir()))
