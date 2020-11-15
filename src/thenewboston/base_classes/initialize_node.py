import decimal

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand, CommandParser
from django.core.validators import validate_ipv46_address

from thenewboston.argparser.validators import int_validator, ipv46_validator, str_length_validator
from thenewboston.constants.network import PROTOCOL_LIST, VERIFY_KEY_LENGTH

"""
The InitializeNode class contains the core logic used when initializing network nodes via the command line.

Includes methods to:
- validate config settings are properly formatted
- standardize error handling
"""


class InitializeNode(BaseCommand):
    unattended = False

    def __init__(self, *args, **kwargs):
        """Inits InitializeNode class"""
        super().__init__(*args, **kwargs)
        self.required_input = {}

    def add_arguments(self, parser: CommandParser):
        """Additional custom arguments"""
        super().add_arguments(parser)
        parser.add_argument('--node_identifier', type=str_length_validator(length=VERIFY_KEY_LENGTH))
        parser.add_argument('--account_number', type=str_length_validator(length=VERIFY_KEY_LENGTH))
        parser.add_argument('--default_transaction_fee', type=int)
        parser.add_argument('--ip_address', type=ipv46_validator())
        parser.add_argument('--port', type=int_validator(min_val=0, max_val=65535))
        parser.add_argument('--protocol', choices=PROTOCOL_LIST)
        parser.add_argument('--version_number', type=str_length_validator(max_len=32))

        parser.add_argument('--unattended', action='store_true')

    def _error(self, message):
        """Display error message string in console"""
        self.stdout.write(self.style.ERROR(message))

    def get_fee(self, *, attribute_name, human_readable_name, value=None):
        """
        Validate fee

        - default_transaction_fee
        """
        valid = False

        while not valid:
            if self.unattended:
                fee = value
            else:
                fee = input(f'Enter {human_readable_name} (required): ')

            if not fee:
                self._error(f'{attribute_name} required')
                continue

            is_valid_integer, fee = self.validate_and_convert_to_integer(fee)

            if not is_valid_integer:
                continue

            self.required_input[attribute_name] = fee
            valid = True

    def get_ip_address(self, value=None):
        """Get IP address from user"""
        valid = False

        while not valid:
            if self.unattended:
                ip_address = value
            else:
                ip_address = input('Enter public IP address (required): ')

            if not ip_address:
                self._error('ip_address required')
                continue

            try:
                validate_ipv46_address(ip_address)
            except ValidationError:
                self._error('Enter a valid IPv4 or IPv6 address')
                continue

            self.required_input['ip_address'] = ip_address
            valid = True

    def get_port(self, value=None):
        """Get port from user"""
        valid = False

        while not valid:
            if self.unattended:
                port = value
            else:
                port = input('Enter port: ')

            if not port:
                break

            try:
                port = int(port)
            except ValueError:
                self._error(f'{port} is not a valid integer')
                continue

            if port < 0:
                self._error('port can not be less than 0')
                continue

            if port > 65535:
                self._error('port can not be greater than 65535')
                continue

            self.required_input['port'] = port
            valid = True

    def get_protocol(self, value=None):
        """Get protocol from user"""
        valid = False

        while not valid:
            if self.unattended:
                protocol = value
            else:
                protocol = input('Enter protocol (required): ')

            if not protocol:
                self._error('protocol required')
                continue

            if protocol not in PROTOCOL_LIST:
                self._error(f'protocol must be one of {PROTOCOL_LIST}')
                continue

            self.required_input['protocol'] = protocol
            valid = True

    def get_verify_key(self, *, attribute_name, human_readable_name, value=None):
        """
        Validate verify key

        - account_number
        - node_identifier
        """
        valid = False

        while not valid:
            if self.unattended:
                verify_key = value
            else:
                verify_key = input(f'Enter {human_readable_name} (required): ')

            if not verify_key:
                self._error(f'{attribute_name} required')
                continue

            if len(verify_key) != VERIFY_KEY_LENGTH:
                self._error(f'{attribute_name} must be {VERIFY_KEY_LENGTH} characters long')
                continue

            self.required_input[attribute_name] = verify_key
            valid = True

    def get_version_number(self, value=None):
        """Get version from user"""
        max_length = 32
        valid = False

        while not valid:
            if self.unattended:
                version = value
            else:
                version = input('Enter version (required): ')

            if not version:
                self._error('version required')
                continue

            if len(version) > max_length:
                self._error(f'version must be less than or equal to {max_length} characters long')
                continue

            self.required_input['version'] = version
            valid = True

    def execute(self, *args, **options):
        self.unattended = options.get('unattended', False)
        return super().execute(*args, **options)

    def handle(self, *args, **options):
        """The actual logic of the command. Subclasses must implement this method"""
        raise NotImplementedError('subclasses of InitializeNode must provide a handle() method')

    def validate_and_convert_to_decimal(self, value):
        """
        Validate that given value can be converted to Decimal value

        Returns: is_valid (bool), decimal_value (Decimal)
        Must return is_valid flag along with decimal_value to allow for proper validation of valid falsy value (0.0)
        """
        try:
            value = decimal.Decimal(value)
        except decimal.InvalidOperation:
            self._error(f'Can not convert {value} to a decimal')
            return False, None

        return True, value

    def validate_and_convert_to_integer(self, value):
        """
        Validate that given value can be converted to integer value

        Returns: is_valid (bool), integer_value (int)
        """
        try:
            value = int(value)
        except ValueError:
            self._error(f'Can not convert {value} to an integer')
            return False, None

        return True, value
