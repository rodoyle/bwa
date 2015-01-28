#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for manipulatig the Burrows Wheeler Transform
"""
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

from cffi import FFI

ffi = FFI()

ffi.verify('#include "../../bwa/bwt.h"')

log = logging.getLogger(__name__)



