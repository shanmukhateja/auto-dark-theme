## auto-dark-theme

A background process to switch between light and dark themes on KDE Plasma.

> This is a work-in-progress software so expect missing features and bugs.

## Pre-requisites

1. KDE Plasma
2. Python 3.10.x
3. PyGObject
4. dbus-python v1.32.2

## Usage

You will need to build the app from source as it's currently a work-in-progress.

In the future, this section will be improved.

### Autostart

This app is meant to be launched as part of `plasma-workspace.target` or `plasma-workspace-wayland.target` by systemd.

Please follow these instructions to setup:

1. Copy `config/auto-dark-theme.service` to `$HOME/.local/share/systemd/user` 

2. Open the service file in your favorite text editor and make the following changes.

    1. Please update project directory path for `WorkingDirectory` and `ExecStart`.
    2. If using X11, please replace `plasma-workspace-wayland.target` with `plasma-workspace.target`.

3. Enable the service using the below command:

```sh
systemctl --user enable --now auto-dark-theme.service
```
4. CLI - Optional
    - If you'd like to use command-line tool, copy `config/autodarktheme` to any directory inside `$PATH`.
    - Run `chmod +x `path/to/autodarktheme` to mark it as executable.

## Development

1. Clone the repository.

```sh
git clone https://github.com/shanmukhateja/auto-dark-theme
cd auto-dark-theme
```

2. Setup virtualenv and install dependencies.

```sh
virtualenv .
pip install -r requirements.txt
```

3. Copy the sample config file:

```sh
mkdir -p $HOME/.config/auto-dark-theme/
cp ./config/config.sample.ini $HOME/.config/auto-dark-theme/config.ini
```

4. Run the app:

```sh
$ python3 -m auto-dark-theme
```

## License

MIT

# Credits

1. dbus-python

2. PyGObject
