class MawarithCalculator:
    def __init__(self, total_property):
        self.total_property = total_property
        self.shares = {}
        self.selected_heirs = {}
    # method for add new heir
    def add_heir(self, heir_name, count=1):
        self.selected_heirs[heir_name] = { 'count': count}

    # method for calculation
    def calculate_shares(self):
        """
        Calculate the shares of the selected heirs according to Islamic inheritance laws.
        """
        remaining_property = self.total_property
        
        # 1. Calculate the Wife's share (if present)
        if 'Wife' in self.selected_heirs:
            wife_share = 0.125 if 'Son' in self.selected_heirs or 'Daughter' in self.selected_heirs else 0.25
            self.shares['Wife'] = wife_share * self.total_property
            remaining_property -= self.shares['Wife']
        
        # 2. Calculate children's shares (if Sons or Daughters exist)
        sons_count = self.selected_heirs.get('Son', {}).get('count', 0)
        daughters_count = self.selected_heirs.get('Daughter', {}).get('count', 0)
        
        if sons_count > 0 or daughters_count > 0:
            total_units = sons_count * 2 + daughters_count  # Sons get double the share of daughters
            if sons_count > 0:
                self.shares['Son'] = (2 * sons_count / total_units) * remaining_property
            if daughters_count > 0:
                self.shares['Daughter'] = (1 * daughters_count / total_units) * remaining_property
        
        # 3. Calculate sibling's shares if no children
        if sons_count == 0 and daughters_count == 0:
            if 'Brother' in self.selected_heirs:
                self.shares['Brother'] = 0.5 * remaining_property
            if 'Sister' in self.selected_heirs:
                self.shares['Sister'] = 0.5 * remaining_property
    
    #method for display shares
    def display_shares(self):
        print("\n--- Inheritance Shares ---")
        for heir, share in self.shares.items():
            print(f"{heir}: {share:.2f}")
    #method for reset the calculator
    def reset(self):
        self.shares = {}
        self.selected_heirs = {}

# Main program to run the Mawarith Calculator
def main():
    print("Welcome to the Mawarith (Islamic Inheritance) Calculator")
    
    # Step 1: Get the total property
    total_property = float(input("Enter the total property value: "))
    
    # Step 2: Initialize the calculator
    calc = MawarithCalculator(total_property)
    
    # Step 3: Ask for heirs
    wife = input("Is the wife alive? (yes/no): ").lower()
    if wife == 'yes':
        calc.add_heir('Wife', 'Wife')

    sons = int(input("How many sons are alive? (Enter 0 if none): "))
    if sons > 0:
        calc.add_heir('Son', sons)

    daughters = int(input("How many daughters are alive? (Enter 0 if none): "))
    if daughters > 0:
        calc.add_heir('Daughter', daughters)

    brother = input("Is there a brother alive? (yes/no): ").lower()
    if brother == 'yes':
        calc.add_heir('Brother')

    sister = input("Is there a sister alive? (yes/no): ").lower()
    if sister == 'yes':
        calc.add_heir('Sister')
    
    # Step 4: Calculate the shares
    calc.calculate_shares()

    # Step 5: Display the shares
    calc.display_shares()

if __name__ == "__main__":
    main()
