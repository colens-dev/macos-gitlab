import json
import webbrowser

from wrappers.gitlab import GitLabWrapper, GitLabException
import rumps


class GitLabApp(rumps.App):

    def __init__(self):
        super(GitLabApp, self).__init__("GitLab Integration")
        self.config = self.__get_config()
        self.gitlab_wrapper = GitLabWrapper(url=self.config.get('url', ''))
        self.icon = "icons/gitlab.png"
        self.__setup_menu()
        rumps.debug_mode(True)

    def __get_config(self):
        try:
            with open('config.json', 'r') as f:
                return json.load(f)
        except OSError:
            return {}

    def __setup_menu(self):
        self.menu.clear()
        username_in_brackets = ''
        if self.config.get("username", ''):
            username_in_brackets = '(' + self.config.get("username", '') + ')'
        self.menu = [
            "My MRs",
            "For review",
            "Preferences",
            rumps.MenuItem(
                'GitLab Username ' + username_in_brackets,
                icon="icons/settings.png",
                callback=self.gitlab_username
            ),
            rumps.MenuItem(
                'GitLab URL',
                icon="icons/settings.png",
                callback=self.gitlab_url
            ),
            rumps.MenuItem(
                'GitLab Token',
                icon="icons/settings.png",
                callback=self.gitlab_token
            ),
            rumps.MenuItem('Quit', callback=rumps.quit_application)
        ]

    def gitlab_token(self, sender):
        previous_token = ""
        if self.config:
            previous_token = self.config.get('token', '')
        token = rumps.Window("GitLab Token", default_text=previous_token).run()
        if token.text:
            self.config['token'] = token.text
        with open('config.json', 'w+') as f:
            f.write(json.dumps(self.config))
        self.check_merge_requests('')

    def gitlab_username(self, sender):
        previous_username = ""
        if self.config:
            previous_username = self.config.get('username', '')
        username = rumps.Window(
            "GitLab Username",
            default_text=previous_username
        ).run()

        if username.text:
            self.config['username'] = username.text
        with open('config.json', 'w+') as f:
            f.write(json.dumps(self.config))
        self.check_merge_requests('')

    def gitlab_url(self, sender):
        previous_url = ""
        if self.config:
            previous_url = self.config.get('url', '')
        url = rumps.Window("GitLab URL", default_text=previous_url).run()
        if url.text:
            self.config['url'] = url.text
        with open('config.json', 'w+') as f:
            f.write(json.dumps(self.config))
        self.gitlab_wrapper.url = url.text
        self.check_merge_requests('')

    def open_link(self, sender):
        webbrowser.open_new_tab(sender.key)

    @rumps.timer(30)
    def check_merge_requests(self, _):
        # Clear menu items and populate it again
        self.__setup_menu()
        username = self.config.get('username')
        token = self.config.get('token')

        try:
            opened_mrs = self.gitlab_wrapper.get_opened_merge_requests(
                username=username,
                token=token
            )
        except GitLabException:
            self.__set_title_error()
            return

        # Set status in case no MRs are found
        if len(opened_mrs) == 0:
            menu_item = rumps.MenuItem("All done!", icon="icons/review.png")
            self.menu.insert_after('For review', menu_item)
        else:
            # Add links to MRs in menu
            for mr in opened_mrs:
                menu_item = rumps.MenuItem(
                    mr.get('title'),
                    callback=self.open_link,
                    key=mr.get('web_url'),
                    icon="icons/review.png"
                )
                self.menu.insert_after('For review', menu_item)

        try:
            my_mrs = self.gitlab_wrapper.get_my_merge_requests(
                username=username,
                token=token
            )
        except GitLabException:
            self.__set_title_error()
            return

        # Set status in case no MRs are found
        if len(my_mrs) == 0:
            menu_item = rumps.MenuItem(
                "Start creating something cool :)",
                icon="icons/edit.png"
            )
            self.menu.insert_after('My MRs', menu_item)
        else:
            # Add links to MRs in menu
            for mr in my_mrs:
                menu_item = rumps.MenuItem(
                    mr.get('title')+' ',
                    callback=self.open_link,
                    key=mr.get('web_url'),
                    icon="icons/edit.png"
                )
                self.menu.insert_after('My MRs', menu_item)

        # Add number of MRs to title
        total_mrs = len(opened_mrs + my_mrs)
        if total_mrs > 0:
            self.title = str(len(opened_mrs + my_mrs))
        else:
            self.title = ''
        if total_mrs > 10:
            self.title = '10+'

    def __set_title_error(self):
        self.title = 'x'


if __name__ == '__main__':
    app = GitLabApp()
    app.run()
