import variables as v

scoreCoal = v.excessCoal * 100
scoreCapacitors = v.capacitors * 500
scoreTotal = scoreCoal + scoreCapacitors

atari = [
    "MISSION COMPLETE !",
    " ",
    "The ATARI tribe can now plow their fields",
    "with peace. Now go get some rest.",
    " ",
    "You reclaimed "+str(v.excessCoal)+" tons of our coal.",
    " ",
    str(v.capacitors)+" Amigas died with acid leaking from",
    "their old capacitors.",
    " ",
    str(v.excessCoal)+" tons of coal x 100 = "+str(scoreCoal)+" pts.",
    str(v.capacitors)+" sets of capacitors x 500 = "+str(scoreCapacitors)+" pts.",
    "Total score = "+str(scoreTotal)+" pts.",
    " ",
    "... But Sir, I fear all we have done",
    "is to awaken a sleeping giant.",
    "Amigans will be back in...", 
    "",
    "(Fire or Return to continue)",
]

amiga = [
    "MISSION COMPLETE !",
    " ",
    "The ATARI tribe got serious hit.",
    "Now go get some rest.",
    " ",
    "You intercepted "+str(v.excessCoal)+" tons of Atarimen's coal.",
    " ",
    "You saved "+str(v.capacitors)+" capacitors for our Amigas. ",
    " ",
    " ",
    str(v.excessCoal)+" tons of coal x 100 = "+str(scoreCoal)+" pts.",
    str(v.capacitors)+" sets of capacitors x 500 = "+str(scoreCapacitors)+" pts.",
    "Total score = "+str(scoreTotal)+" pts.",
    " ",
    "... and all they accomplished in that amateur",
    "attack is awakening of our sleeping giant.",
    "We, the Amigans will crush them in...",
    "",
    "(Fire or Return to continue)", 
]

leakedTxt = [ "if (leaked capacitor == 2){", # message to print, too short to push into
    "amigaModeDestroy(); ", # seperate file, i think
    "}",
    "// WTF",
    "NO AMIGA SPIRIT FROM YOU I SMELL.",
    "LEAKED CAPACITOR NO GOOD IMPROVEMENT IS.",
    "SPACESHIP WICHER OF OURS YOU DESTROYED.",
    "MAY THE WEAKNESS OF ATARI BE WITH YOU.",
    "CHEATER. EAT COAL.",
    "(Fire or Return to continue)",
]