# Sysrev Client

## Development

### Setup

- Install Nix ([Linux](https://github.com/DeterminateSystems/nix-installer#the-determinate-nix-installer) | [macOS](https://determinate.systems/posts/graphical-nix-installer))
- Install [direnv](https://direnv.net/)
- Install [nix-direnv](https://github.com/nix-community/nix-direnv) (or [lorri](https://github.com/nix-community/lorri) for macOS).
- Run `direnv allow` in the repository root
  - `direnv` will now install all dependencies and load the environment from `flake.nix`

## Polylith

``` bash
# create a base
uv run poly create base --name my_base

# create a component
uv run poly create component --name my_component
```
