
# Infomaniak recipes

This folder contains recipes for AI on [Infomaniak](https://www.infomaniak.com/).

## Configuration of Mistral's Vibe tool

The elements to add for configuring Mistral Vibe to use Infomaniak are available in `config.toml`.

You will need to do the following:

- Copy/paste the sections into `~/.vibe/config.toml`
- Replace `PROJECT_ID` by the ID of your project (in the Infomaniak manager)
- Set the environment `INFOMANIAK_AI_TOKEN` to have your Infomaniak API token as a value
