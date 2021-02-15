<p align="center">
  <img alt="thenewboston logo" src="https://user-images.githubusercontent.com/65713950/100157416-cf2bbc00-2eaa-11eb-95fe-3ef87a18ad93.png" width="620">
</p>

## Overview

Python library for thenewboston digital currency.

This library contains all of the core logic, shared functionality, and
constants used by both the [Bank](https://github.com/thenewboston-developers/Bank) and 
[Validator](https://github.com/thenewboston-developers/Validator) on thenewboston network.

## Project Setup

Follow the steps below to set up the project on your environment. If you run into any problems, feel free to leave a 
GitHub Issue or reach out to any of our communities above.

Install required packages:
```
pip3 install -e .
```

## Testing

To run tests:
```
pytest
```

To run tests with coverage report:
```
pytest --cov-config=.coveragerc --cov=./src 
```

To run linting:
```
flake8 .
```

## Building

The building and publishing of this package is automated through GitHub actions. To publish a new release, update the
`./src/thenewboston/__init__.py` file with the latest version number. The updated package will be published once the
branch is merged into `master`.

To produce a source distribution manually:
```
python3 setup.py sdist
```

## Community

Join the community to stay updated on the most recent developments, project roadmaps, and random discussions about completely unrelated topics.

- [thenewboston.com](https://thenewboston.com/)
- [Discord](https://discord.gg/thenewboston)
- [Facebook](https://www.facebook.com/TheNewBoston-464114846956315/)
- [Instagram](https://www.instagram.com/thenewboston_official/)
- [LinkedIn](https://www.linkedin.com/company/thenewboston-developers/)
- [Reddit](https://www.reddit.com/r/thenewboston/)
- [Twitch](https://www.twitch.tv/thenewboston/videos)
- [Twitter](https://twitter.com/thenewboston_og)
- [YouTube](https://www.youtube.com/user/thenewboston)

## Donate

All donations will go to thenewboston to help fund the team to continue to develop the community and create new content.

| Coin | Address |
|-|-|
| ![thenewboston Logo](https://github.com/thenewboston-developers/Website/raw/development/src/assets/images/thenewboston.png) | b6e21072b6ba2eae6f78bc3ade17f6a561fa4582d5494a5120617f2027d38797 |
| ![Bitcoin Logo](https://github.com/thenewboston-developers/Website/raw/development/src/assets/images/bitcoin.png) | 3GZYi3w3BXQfyb868K2phHjrS4i8LooaHh |
| ![Ethereum Logo](https://github.com/thenewboston-developers/Website/raw/development/src/assets/images/ethereum.png) | 0x0E38e2a838F0B20872E5Ff55c82c2EE7509e6d4A |

## License

thenewboston is [MIT licensed](http://opensource.org/licenses/MIT).
