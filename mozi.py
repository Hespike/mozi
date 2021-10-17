def szekem(azonosito):
    if azonosito > 98:
        azonosito = azonosito / 98
    if azonosito < 15:
        sor = 1
        if azonosito <= 7:
            oldal = "jobb"
            szam = 8 - azonosito
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
        if azonosito >= 8:
            oldal = "bal"
            szam = azonosito - 7
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
    if 14 < azonosito < 29:
        sor = 2
        if azonosito <= 21:
            oldal = "jobb"
            szam = 22 - azonosito
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
        if azonosito >= 22:
            oldal = "bal"
            szam = azonosito - 21
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
    if 28 < azonosito < 43:
        sor = 3
        if azonosito <= 35:
            oldal = "jobb"
            szam = 36 - azonosito
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
        if azonosito >= 36:
            oldal = "bal"
            szam = azonosito - 35
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
    if 42 < azonosito < 57:
        sor = 4
        if azonosito <= 49:
            oldal = "jobb"
            szam = 50 - azonosito
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
        if azonosito >= 50:
            oldal = "bal"
            szam = azonosito - 49
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
    if 56 < azonosito < 71:
        sor = 5
        if azonosito <= 63:
            oldal = "jobb"
            szam = 64 - azonosito
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
        if azonosito >= 64:
            oldal = "bal"
            szam = azonosito - 63
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
    if 70 < azonosito < 85:
        sor = 6
        if azonosito <= 77:
            oldal = "jobb"
            szam = 78 - azonosito
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
        if azonosito >= 78:
            oldal = "bal"
            szam = azonosito - 77
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
    if 84 < azonosito < 99:
        sor = 7
        if azonosito <= 91:
            oldal = "jobb"
            szam = 92 - azonosito
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
        if azonosito >= 92:
            oldal = "bal"
            szam = azonosito - 91
            return("%d. sor, %s %d. szek" % (sor, oldal, szam))
