<p align="center">
  <img alt="thenewboston logo" src="https://i.imgur.com/MautJBL.png" width="620">
</p>

## Overview

Python library for thenewboston digital currency.

This library contains all of the core logic, shared functionality, and
constants used by both the [Bank](https://github.com/thenewboston-developers/Bank) and 
[Validator](https://github.com/thenewboston-developers/Validator) on thenewboston network.

# Community

Join the community to stay updated on the most recent developments, project roadmaps, and random discussions about
completely unrelated topics.

- [thenewboston.com](https://thenewboston.com/)
- [Slack](https://join.slack.com/t/thenewboston/shared_invite/zt-hkw1b98m-X3oe6VPX6xenHvQeaXQbfg)
- [reddit](https://www.reddit.com/r/thenewboston/)
- [Facebook](https://www.facebook.com/TheNewBoston-464114846956315/)
- [Twitter](https://twitter.com/bucky_roberts)
- [YouTube](https://www.youtube.com/user/thenewboston)

# Project Setup

Follow the steps below to set up the project on your environment. If you run into any problems, feel free to leave a 
GitHub Issue or reach out to any of our communities above.

Install required packages:
```
pip3 install -r requirements.txt
```

## Testing

To run tests:
```
pytest
```

To run tests with coverage report:
```
pytest --cov-config=.coveragerc --cov=./thenewboston 
```

## Building

To produce a source distribution:
```
python3 setup.py sdist
```

## License

thenewboston is [MIT licensed](http://opensource.org/licenses/MIT).
