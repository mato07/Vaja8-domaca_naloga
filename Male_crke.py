# -*- coding: utf-8 -*-

tekst1 = "Ta TEKST žeLim PreTVOriti v maLe črke. ReŠitev ne deluje za Č Ž Š."

resitev1 = tekst1.lower()

print resitev1

tekst2 = "Ta TEKST žeLim PreTVOriti v maLe črke. ReŠitev deluje tudi za Č Ž Š."

resitev2 = tekst2.decode('utf8').lower()

print resitev2