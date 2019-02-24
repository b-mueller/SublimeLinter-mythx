SublimeLinter-contrib-mythx
===========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-__linter__.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-__linter__)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [MythX](https://mythx.io). It will be used with files that have the “solidity” syntax.

## Installation
SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that [sabre](https://www.github.com/b-mueller/sabre) is installed on your system.

In order for [sabre](https://www.github.com/b-mueller/sabre) to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## MythX API Access
To use this plugin you'll probably want to have a MythX API account. See [here](https://docs.mythx.io/en/latest/main/getting-started.html#obtaining-api-credentials) for instructions. Make sure that the following environment variables are set:

```
MYTHX_ETH_ADDRESS=[...]
MYTHX_PASSWORD=yourpassword
```

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

