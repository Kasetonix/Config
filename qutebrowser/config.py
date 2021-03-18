c.aliases = {'q': 'quit', 'w': 'session-save', 'wq': 'quit --save'}

c.content.cookies.accept = 'all'

config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://drive.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')

config.set('content.images', True, 'chrome-devtools://*')
config.set('content.images', True, 'devtools://*')

config.set('content.javascript.enabled', True, 'chrome-devtools://*')
config.set('content.javascript.enabled', True, 'devtools://*')
config.set('content.javascript.enabled', True, 'chrome://*/*')
config.set('content.javascript.enabled', True, 'qute://*/*')

config.set('content.notifications', True, 'https://www.reddit.com')
config.set('content.notifications', True, 'https://www.youtube.com')

c.downloads.location.directory = '/home/kasetonix/Downloads'

c.tabs.show = 'always'

c.url.default_page = 'file:///home/kasetonix/Documents/Homepage/homepage.html'

c.url.searchengines = {'DEFAULT': 'https://duckduckgo.com/?q={}', 'google': 'https://www.google.com/search?q={}', 'reddit': 'https://www.reddit.com/r/{}', 'wiki': 'https://en.wikipedia.org/wiki/{}', 'yt': 'https://www.youtube.com/results?search_query={}'}

c.colors.completion.fg = ['#83a598', '#fbf1c7', '#fbf1c7']
c.colors.completion.odd.bg = '#282828'
c.colors.completion.even.bg = '#282828'
c.colors.completion.category.fg = '#d79921'
c.colors.completion.category.bg = 'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #3c3836)'
c.colors.completion.category.border.top = '#504945'
c.colors.completion.category.border.bottom = '#504945'
c.colors.completion.item.selected.fg = '#504945'
c.colors.completion.item.selected.bg = '#fabd2f'
c.colors.completion.item.selected.match.fg = '#d79921'
c.colors.completion.match.fg = '#d79921'
c.colors.completion.scrollbar.fg = '#fbf1c7'
c.colors.downloads.bar.bg = '#3c3836'
c.colors.downloads.error.bg = '#cc241d'
c.colors.hints.fg = '#3c3836'
c.colors.hints.match.fg = '#689d6a'
c.colors.messages.info.bg = '#3c3836'
c.colors.statusbar.normal.bg = '#3c3836'
c.colors.statusbar.insert.fg = '#fbf1c7'
c.colors.statusbar.insert.bg = '#83a598'
c.colors.statusbar.passthrough.bg = '#458588'
c.colors.statusbar.command.bg = '#3c3836'
c.colors.statusbar.url.warn.fg = 'yellow'
c.colors.tabs.bar.bg = '#3c3836'
c.colors.tabs.odd.bg = '#665c54'
c.colors.tabs.even.bg = '#665c54'
c.colors.tabs.selected.odd.bg = '#3c3836'
c.colors.tabs.selected.even.bg = '#3c3836'
c.colors.tabs.pinned.odd.bg = 'seagreen'
c.colors.tabs.pinned.even.bg = 'seagreen'
c.colors.tabs.pinned.selected.odd.bg = '#d79921'
c.colors.tabs.pinned.selected.even.bg = '#d79921'
c.colors.statusbar.caret.selection.bg = '#fe8019'

c.fonts.default_family = '"Roboto"'
c.fonts.default_size = '14pt'
c.fonts.completion.entry = '13pt "Roboto"'
c.fonts.debug_console = '13pt "Inconsolata"'
c.fonts.prompts = 'default_size Inconsolata'
c.fonts.statusbar = '13pt "Roboto"'

c.scrolling.smooth = True

c.tabs.title.format = '{audio}{current_title}'

c.content.autoplay = False

c.statusbar.hide = True 

c.statusbar.widgets = ["keypress", "url", "scroll"]

c.downloads.position = 'bottom'

c.downloads.remove_finished = 5

c.tabs.favicons.scale = 0.75

config.load_autoconfig()
