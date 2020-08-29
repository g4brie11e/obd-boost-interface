# OBD Boost Interface
[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

Initially inspired by seeing a friend's boost gauge extension in their Mini Cooper S, I am replicating this on an old Android smartphone. Also working on formatting other helpful on board diagnostic data like error codes so I can avoid using expensive (and often buggy) MacOS software.

## Requirements
- [Python 3.8.x](https://www.python.org/downloads/release/python-385/) (tested with 3.8.5)
```
  $ sudo apt-get update
  $ sudo apt-get install python3.8
```
- A terminal emulator 
- ELM327 OBD-II adapter (bluetooth or cable)
- [Python-OBD Library](https://python-obd.readthedocs.io/en/latest/#installation) - latest release:
```
   $ pip install obd
```

## How To Use
[TODO]
```
  $ python ./run.py
```

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

[![HitCount](http://hits.dwyl.io/g4brie11e/obd-boost-interface.svg)](http://hits.dwyl.io/g4brie11e/obd-boost-interface)
