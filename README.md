# Sublime Text Chrome Auto Refresh
### Refresh Chrome without losing window focus of Sublime Text

Compatible with OSX and Chrome only.

Chrome Refresh has two settings for each window that determine how it behaves:

- **enabled**: the page is refreshed on save. Set by `ctrl+shift+p` and typing `Chrome Refresh: Enable/Disable`
- **url**: if unset, the current tab will be refreshed, if set it switches to/opens the tab and refreshes that url. Set the url by doing `ctrl+shift+p` and typing `Chrome Refresh: Set Url` (unset by entering a blank url)

`command+shift+r` forces a refresh of the specified page.

To compile teh applescripts:

    osacompile -o chromeopen.scpt chromeopen.AppleScript