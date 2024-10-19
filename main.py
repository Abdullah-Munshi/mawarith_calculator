import questionary
#define heirs
heirs = ['Son', 'Daughter', 'Husband', 'Wife', 'Father', 'Mother', 'Brother']
#ask the questions to user
print('Welcome to Mawarith Calculator')
total_land = float(questionary.text('Enter the total land area of the property(decimal): ').ask())
selected_heirs = questionary.checkbox(
    "Select the heirs",
    choices=heirs).ask()
#heir counts
heir_counts = {}

for heir in selected_heirs:
    if heir in ['Son', 'Daughter', 'Wife', 'Mother', 'Brother']:
        count = int(questionary.text('How many {heir} do you have?'.format(heir=heir.lower())).ask())
        heir_counts[heir] = count

