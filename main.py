# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: November 4th, 2025
# | Last update..: November 5th, 2025
# | WhatIs.......: Words Analyzer - Class
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------

# ------------------------- Libraries -------------------------
import os  # os.path.exists(path)
from WordsAnalyzer_class import WordsAnalyzer

# ------------------------- Variables -------------------------
libraryRoute = 'library/'
groupedTokens = {}
allTokens = ""

# ------------------------- Objects -------------------------
cloudMaker = WordsAnalyzer()

# --------------------------- Code ----------------------------
for i in os.listdir(libraryRoute):
    groupedTokens[i] = cloudMaker.getTokensFromFile(f'{libraryRoute}{i}', show_tokens=False)
    cloudMaker.makeCloud(groupedTokens[i], "self")

for j in groupedTokens:
    print(f"{j}: {groupedTokens[j]}")
    allTokens += groupedTokens[j]

cloudMaker.makeCloud(allTokens, "AllTokens")