# -*- coding: utf-8 -*-

"""
------------------------------------------------------------------------
Copyright 2024 Yanhong Lyu
All Rights Reserved

EnMNP Academic License

mhcuid.py 
------------------------------------------------------------------------

Generates unique identifier for a given MHC allele.
"""


import re
def mhcuid(mhc : str) -> str:
    return re.sub(r"[^A-Z0-9]+", "", mhc.upper())

