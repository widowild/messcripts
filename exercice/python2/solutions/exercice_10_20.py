#! /usr/bin/env python
# -*- coding:Utf-8 -*-

s1 = u"àéèêëîïôöûüù"
s2 = u""
for c in s1:
    code =ord(c)
    s2 = s2 + unichr(code -32)

print s1
print s2

