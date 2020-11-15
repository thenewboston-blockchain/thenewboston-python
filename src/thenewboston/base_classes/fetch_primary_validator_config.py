from django.core.exceptions import ValidationError
from django.core.management import CommandParser

from thenewboston.argparser.validators import decimal_validator
from thenewboston.base_classes.initialize_node import InitializeNode
from thenewboston.constants.network import PRIMARY_VALIDATOR
from thenewboston.utils.format import format_address
from thenewboston.utils.network import fetch
from thenewboston.utils.validators import validate_is_real_number

"""
The FetchPrimaryValidatorConfig class contains logic to fetch and validate configuration data from a primary validator.
"""


class FetchPrimaryValidatorConfig(InitializeNode):

    def __init__(self, *args, **kwargs):
        """Initialize FetchPrimaryValidatorConfig class"""
        super().__init__(*args, **kwargs)

        self.required_input = {
            'ip_address': None,
            'port': None,
            'protocol': None,
            'trust': None
        }

    def add_arguments(self, parser: CommandParser):
        """Additional custom arguments"""
        super().add_arguments(parser)
        parser.add_argument('--trust', type=decimal_validator(min_val=0, max_val=100))

    def get_primary_validator_address(self):
        """Return formatted address of primary validator"""
        return format_address(
            ip_address=self.required_input['ip_address'],
            port=self.required_input['port'],
            protocol=self.required_input['protocol']
        )

    def get_trust(self, value=None):
        """Get trust from user"""
        valid = False

        while not valid:
            if self.unattended:
                trust = value
            else:
                trust = input('Enter trust (required): ')

            if not trust:
                self._error('trust required')
                continue

            is_valid_decimal, trust = self.validate_and_convert_to_decimal(trust)

            if not is_valid_decimal:
                continue

            try:
                validate_is_real_number(trust)
            except ValidationError:
                self._error('Value must be a real number')
                continue

            if trust < 0:
                self._error('Value can not be less than 0')
                continue

            if trust > 100:
                self._error('Value can not be greater than 100')
                continue

            self.required_input['trust'] = trust
            valid = True

    def fetch_validator_config(self):
        """Return config"""
        address = self.get_primary_validator_address()
        url = f'{address}/config'
        results = fetch(url=url, headers={})
        return results

    def handle(self, *args, **options):
        """Run script"""
        connected = False

        while not connected:
            self.required_input = {
                'ip_address': None,
                'port': None,
                'protocol': None
            }

            self.get_ip_address(value=options.get('ip_address'))
            self.get_protocol(value=options.get('protocol'))
            self.get_port(value=options.get('port'))

            try:
                config = self.fetch_validator_config()

                if not self.is_config_valid(config):
                    continue

                self.get_trust(value=options.get('trust'))
                self.handle_primary_validator_config(config)
            except Exception as e:
                self._error('Unable to connect')
                self._error(e)
                continue

            connected = True

        self.stdout.write(self.style.SUCCESS('Success'))

    def handle_primary_validator_config(self, primary_validator_config):
        """Handle primary validator configuration data"""
        raise NotImplementedError(
            'subclasses of FetchPrimaryValidatorConfig must provide a handle_primary_validator_config() method'
        )

    def is_config_valid(self, config):
        """Validate config response data from the validator"""
        if config.get('node_type') != PRIMARY_VALIDATOR:
            self._error(f'node_type is not {PRIMARY_VALIDATOR}')
            return False

        return True
