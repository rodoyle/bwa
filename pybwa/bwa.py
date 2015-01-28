#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module for calling the Burrows Wheeler Aligner Functions
"""
from __future__ import division
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

from cffi import FFI

ffi = FFI()

ffi.verify('#include "../../bwa/bwa.h"')

log = logging.getLogger(__name__)