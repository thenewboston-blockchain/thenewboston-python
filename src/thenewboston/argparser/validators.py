# -*- coding: utf-8 -*-
import argparse
import decimal
import math
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
        if min_val and value < min_val:
            raise argparse.ArgumentTypeError('Value can not be less than %s' % min_val)
        if max_val and value > max_val:
            raise argparse.ArgumentTypeError('Value can not be greater than %s' % max_val)
        return value
    return inner


def decimal_validator(min_val: [int, decimal.Decimal] = None, max_val: [int, decimal.Decimal] = None):
    """Argparse validator for decimals"""
    def inner(value):
        try:
            value = decimal.Decimal(value)
        except decimal.InvalidOperation:
            raise argparse.ArgumentTypeError('Value is not a valid decimal')
        if math.isnan(value):
            raise argparse.ArgumentTypeError('NaN is not allowed')
        if math.isinf(value):
            raise argparse.ArgumentTypeError('Infinity is not allowed')
        if min_val and value < min_val:
            raise argparse.ArgumentTypeError(f'Value can not be less than {min_val}')
        if max_val and value > max_val:
            raise argparse.ArgumentTypeError(f'Value can not be greater than {max_val}')
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
