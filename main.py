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

# ------------------------- Objects -------------------------
cloudMaker = WordsAnalyzer()

# --------------------------- Code ----------------------------
for i in os.listdir(libraryRoute):
    cloudMaker.makeCloud(f'{libraryRoute}{i}')