## Global agent guidelines for this repo

- When possible, store the canonical version of app config files (e.g., VS Code `settings.json`, `keybindings.json`, terminal profiles, etc.) inside this repo and use symlinks from their default locations to point into the repo.
- Prefer small, focused shell scripts or single copy-pastable command blocks that the user can run manually to create/update those symlinks rather than complex automation.
- Avoid modifying files outside this repo from within tooling unless explicitly requested by the user; instead, print commands or instructions the user can run themselves.

