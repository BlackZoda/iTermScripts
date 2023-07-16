# BlackZoda's iTerm2 Scripts

For how to write and use Python scripts for iTerm2 see the details in the [iTerm2 documentation](https://iterm2.com/documentation-scripting-fundamentals.html).

If you just want to run a script, place it the `/Users/{Username}/Library/Application Support/iTerm2/Scripts[/AutoLaunch]` folder. Daemon scripts should be placed in the `./AutoLaunch` folder, while scripts that are manually triggered should be placed diretly in the root folder.

## Pane Transparency

Daemon running in the background (in the `./AutoLaunch` folder) that automatically sets the transparency of all panes. Set the desired transparency (between 0 and 1) for the active and inactive panes in the `settings.json` file – `pane_transparency.active`, and `pane_transparency.inactive`. Works with new windows and split panes.

I also added settings for blur. Blur seem to only be global, and can't be set for individual panes as far as I know. If you still want to use it, you can set `pane_transparency.blur` to `true` and `pane_transparency.blur_radius` to an integer between 0 and 30 (30 being most blury) in the `settings.json` file.
