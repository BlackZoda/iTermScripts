#!/usr/bin/env python3.7

import iterm2
import json
import os

# Global settings
SETTINGS_FILE = os.path.join(os.path.dirname(__file__), '../settings.json')

# Default pane transparency settings (overridden by settings.json)
DEFAULT_TRANSPARENCY_ACTIVE = 0.2
DEFAULT_TRANSPARENCY_INACTIVE = 0.5

async def load_settings():
    """Load settings from the settings.json configuration file."""

    with open(SETTINGS_FILE) as f:
        settings = json.load(f)

    pane_transparency = settings.get("pane_transparency", {})
    transparancy_active = pane_transparency.get("active", DEFAULT_TRANSPARENCY_ACTIVE)
    transparency_inactive = pane_transparency.get("inactive", DEFAULT_TRANSPARENCY_INACTIVE)

    return transparancy_active, transparency_inactive

async def transparancy_update(app, active_session, update, transparency_active, transparency_inactive):
    """Updating the transparency of the active and inactive panes."""

    if update.active_session_changed or update.selected_tab_changed:

        inactive_change = iterm2.LocalWriteOnlyProfile()
        inactive_change.set_transparency(transparency_inactive)

        active_change = iterm2.LocalWriteOnlyProfile()
        active_change.set_transparency(transparency_active)

        # Updates all inactive panes
        await transparancy_update_inactive(app, active_session, inactive_change)
        print(f"Inactive: {transparency_inactive}")

        # Updates the the active pane
        if active_session:
            await active_session.async_set_profile_properties(active_change)
            print(f"Active: {transparency_active}")

async def transparancy_update_inactive(app, active_session, inactive_change):
    """Updating the transparency off all inactive panes."""

    # Looping over all inactive panes and changing transparency
    for window in app.terminal_windows:
            for tab in window.tabs:
                for session in tab.all_sessions:
                    if session != active_session:
                        await session.async_set_profile_properties(inactive_change)

async def main(connection):
    """Pane transparency main method"""

    app = await iterm2.async_get_app(connection)

    transparency_active, transparency_inactive = await load_settings()

    async with iterm2.FocusMonitor(connection) as mon:
        active_session = app.current_terminal_window.current_tab.current_session
        while True:
            update = await mon.async_get_next_update()

            if update.active_session_changed:
                active_session = app.get_session_by_id(update.active_session_changed.session_id)

            await transparancy_update(app, active_session, update, transparency_active, transparency_inactive)

iterm2.run_forever(main)