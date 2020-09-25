<p align="center">
  <img alt="thenewboston logo" src="https://i.imgur.com/MautJBL.png" width="620">
</p>

## Overview

Python library for thenewboston digital currency.

This library contains all of the core logic, shared functionality, and
constants used by both the [Bank](https://github.com/thenewboston-developers/Bank) and 
[Validator](https://github.com/thenewboston-developers/Validator) on thenewboston network.

## Community

Join the community to stay updated on the most recent developments, project roadmaps, and random discussions about 
completely unrelated topics.

- [thenewboston.com](https://thenewboston.com/)
- [Slack](https://join.slack.com/t/thenewboston/shared_invite/zt-gyodq1sw-OYiKy4sy_rmREHIlisFjLA)
- [reddit](https://www.reddit.com/r/thenewboston/)
- [Facebook](https://www.facebook.com/TheNewBoston-464114846956315/)
- [Twitter](https://twitter.com/bucky_roberts)

## Project Setup

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
