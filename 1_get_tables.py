import os
import calendar

# User input
year = 2020

monthnames = ['xaneiro',
              'febreiro',
              'marzo',
              'abril',
              'maio',
              'xuño',
              'xullo',
              'agosto',
              'setembro',
              'outubro',
              'novembro',
              'decembro']

weekdaynames = ['Luns',
              'Martes',
              'Mércores',
              'Xoves',
              'Venres',
              'Sábado',
              'Domingo']

# Folder for table files
dpath = os.path.join(os.getcwd(),'tables')

# Create data folder
if not os.path.exists(dpath):
    os.makedirs(dpath)

# Save variables
varfname = os.path.join(dpath,'Variables.txt')
print('Year: %i\nWriting ...' %year)
print(os.path.basename(varfname))
with open(varfname , 'w') as f:
    f.write('Year = %s\n' %year)
    for m in range(len(monthnames)):
        f.write('%s = %s\n' %(calendar.month_name[m+1],monthnames[m]))
    for m in range(len(weekdaynames)):
        f.write('%s = %s\n' %(calendar.day_name[m],weekdaynames[m]))

# Loop through calendar
cal = calendar.Calendar()
for mm in range(1,13):
    monthcal = cal.monthdatescalendar(year,mm)

    # Set table file name
    tabfname = os.path.join(dpath,'%s.csv' % calendar.month_name[mm])

    # Write headers for file
    print(os.path.basename(tabfname))
    with open(tabfname, 'w') as f:
        f.write('mon,tue,wed,thu,fri,sat,sun\n')

    # Loop through each week
    for week in monthcal:
        T = []
        # Loop through each day of the week
        for d in week:
            # Write latex entries (gray color if different month)
            if d.month != mm:
                T.append('{\\noindent\color{gray}%i}' %(d.day))
            else:
                T.append(str(d.day))
        # String strings to file
        with open(tabfname, 'a') as f:
            f.write(",".join(T) + '\n')
    # Add extra lines for consistency
    if len(monthcal) < 5:
        with open(tabfname, 'a') as f:
            f.write(','*6 + '\n')
    if len(monthcal) < 6:
        with open(tabfname, 'a') as f:
            f.write(','*6)

print('Done!')

