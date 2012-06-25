
#
# spyne - Copyright (C) Spyne contributors.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#


ARRAY_SUFFIX = 'Array'
RESPONSE_SUFFIX = 'Response'
RESULT_SUFFIX = 'Result'
TYPE_SUFFIX = 'Type'


def set_array_suffix(what):
    global ARRAY_SUFFIX
    ARRAY_SUFFIX = what


def set_response_suffix(what):
    global RESPONSE_SUFFIX
    RESPONSE_SUFFIX = what


def set_result_suffix(what):
    global RESULT_SUFFIX
    RESULT_SUFFIX = what


def set_type_suffix(what):
    global TYPE_SUFFIX
    TYPE_SUFFIX = what
