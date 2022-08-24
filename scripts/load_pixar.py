import csv
from blogtest.models import Obfuscated

def run():
    with open('testifeo/obfuscated.csv') as f:
        reader = csv.reader(f, delimiter='|', quotechar='"')
        next(reader)  # Advance past the header

        Obfuscated.objects.all().delete()

        for row in reader:
            print(row)
            if row:
                print(row[2])
                Obf = Obfuscated(NUMDOS=row[0],
                            NUMDOSVERLING=row[1],ANCART=row[2],
                            FILIERE=row[3],ETAPE=row[4],
                            VERLING=row[5],FORMAT=row[6]
                            )
                Obf.save()
