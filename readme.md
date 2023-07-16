# BlackZoda's iTerm2 Scripts

For how to write and use Python scripts for iTerm2 see the details in the [iTerm2 documentation](https://iterm2.com/documentation-scripting-fundamentals.html). If you just want to run a script, place it the `/Users/{Username}/Library/Application Support/iTerm2/Scripts[/AutoLaunch]` folder. Daemon scripts should be placed in the `Scripts/AutoLaunch folder, while scripts that are manually triggered should be placed diretly in `Scripts`.

## Pane Transparency
Daemon running in the background that automatically sets the transparency of all panes. Set the desired transparency for the active and inactive panesin the settings.json file – pane_transparency.active, and pane_transparency.inactive. Works with new windows and split panes.
