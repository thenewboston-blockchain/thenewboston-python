# -*- coding: utf-8 -*-
import argparse
from pathlib import Path

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator, validate_ipv4_address, validate_ipv6_address


def str_length_validator(length: int = None, min_len: int = None, max_len: int = None):
    """Argparse validator for strings"""
    def inner(value):
        if not isinstance(value, str):
            raise argparse.ArgumentTypeError('Expecting string')
        if length and not len(value) == length:
            raise argparse.ArgumentTypeError('String length should be exactly %s chars' % length)
        if min_len and len(value) < min_len:
            raise argparse.ArgumentTypeError('String length should be greater or equal to %s chars' % min_len)
        if max_len and len(value) > max_len:
            raise argparse.ArgumentTypeError('String length should be less or equal to %s chars' % max_len)
        return value
    return inner


def int_validator(min_val: int = None, max_val: int = None):
    """Argparse validator for integers"""
    def inner(value):
        try:
            value = int(value)
        except ValueError:
            raise argparse.ArgumentTypeError('Value is not a valid integer')
        if value < min_val:
            raise argparse.ArgumentTypeError('Value can not be less than %s' % min_val)
        if value > max_val:
            raise argparse.ArgumentTypeError('Value can not be greater than %s' % max_val)
        return value
    return inner


def ipv46_validator():
    """Argparse validator to check whether a string is IP v4 or v6 address"""
    def inner(value):
        try:
            validate_ipv4_address(value)
        except ValidationError:
            try:
                validate_ipv6_address(value)
            except ValidationError:
                raise argparse.ArgumentTypeError('Enter a valid IPv4 or IPv6 address')
        return value
    return inner


def url_validator(suffix: str = None):
    """Argparse validator to check whether a string a proper url"""
    def inner(value):
        try:
            validator = URLValidator(schemes=['http', 'https'])
            validator(value)
        except ValidationError:
            raise argparse.ArgumentTypeError('Invalid URL')
        if suffix and Path(value).suffix != suffix:
            raise argparse.ArgumentTypeError('JSON file required')
        return value
    return inner
