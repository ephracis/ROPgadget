#!/usr/bin/env python2
## -*- coding: utf-8 -*-
##
##  Jonathan Salwan - 2014-05-12
## 
##  http://shell-storm.org
##  http://twitter.com/JonathanSalwan
## 
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software  Foundation, either  version 3 of  the License, or
##  (at your option) any later version.
##

from capstone import *

class Raw:
    def __init__(self, binary, arch, mode):
        self.__binary = bytearray(binary)
        self.__arch   = arch
        self.__mode   = mode

    def getEntryPoint(self):
        return 0x0

    def getExecSections(self):
        return [{"name": "raw", "offset": 0x0, "size": len(self.__binary), "vaddr": 0x0, "opcodes": str(self.__binary)}]

    def getDataSections(self):
        return []

    def getArch(self):
        arch =  {
                    "x86":      CS_ARCH_X86,
                    "arm":      CS_ARCH_ARM,
                    "arm64":    CS_ARCH_ARM64,
                    "sparc":    CS_ARCH_SPARC,
                    "mips":     CS_ARCH_MIPS,
                    "ppc":      CS_ARCH_PPC
                }
        try:
            ret = arch[self.__arch]
        except:
            print "[Error] Raw.getArch() - Architecture not supported. Only supported: x86 arm arm64 sparc mips ppc"
            return None
        return ret

    def getArchMode(self):
        mode =  {
                    "32":      CS_MODE_32,
                    "64":      CS_MODE_64,
                    "arm":     CS_MODE_ARM,
                    "thumb":   CS_MODE_THUMB
                }
        try:
            ret = mode[self.__mode]
        except:
            print "[Error] Raw.getArchMode() - Mode not supported. Only supported: 32 64 arm thumb"
            return None
        return ret

    def getFormat(self):
        return "Raw"

