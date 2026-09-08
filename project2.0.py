# ============================================================
#                  PROJECT : LOGIC BOX
#         Pattern Generator and Number Analyzer
# ============================================================
# Author       : Student Project
# Language     : Python 3
# Concepts     : Loops, Nested Loops, range(), break, pass,
#                Menu-Driven Program, Input Validation
# ============================================================

def welcome_message():
    # ========================================================
    #                   WELCOME MESSAGE
    # ========================================================
    print("=" * 55)
    print("   Welcome to the Pattern Generator and Number Analyzer!")
    print("=" * 55)
    print("This program helps you practice:")
    print("  • Nested loops (Pattern Generation)")
    print("  • for / while loops + range()")
    print("  • Control statements (break, pass)")
    print("  • Menu-driven interface")
    print("=" * 55)
    print()


def show_menu():
    # ========================================================
    #                     MAIN MENU
    # ========================================================
    print("\nSelect an option:")
    print("1. Generate a Pattern (Right-angled Triangle)")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")
    print("-" * 45)


def generate_pattern():
    # ========================================================
    #               PATTERN GENERATOR MODULE
    # ========================================================
    print("\n--- Pattern Generator ---")
    
    while True:
        try:
            rows = int(input("Enter the number of rows for the pattern: "))
            
            # Validation + break example
            if rows <= 0:
                print("Invalid input! Number of rows must be positive.")
                print("Stopping pattern generation...")
                break   # <-- break is used here as required
            
            print("\nPattern:")
            # Nested loops to create right-angled triangle
            for i in range(1, rows + 1):          # Outer loop → rows
                for j in range(i):                # Inner loop → columns
                    print("*", end="")
                print()                           # New line after each row
            
            break   # Exit the input loop after successful generation
            
        except ValueError:
            print("Please enter a valid integer!")


def analyze_numbers():
    # ========================================================
    #               NUMBER ANALYZER MODULE
    # ========================================================
    print("\n--- Number Analyzer ---")
    
    while True:
        try:
            start = int(input("Enter the start of the range: "))
            end   = int(input("Enter the end of the range  : "))
            
            if end < start:
                print("Error: End must be greater than or equal to Start.")
                continue   # Re-prompt
            
            total = 0
            
            print()
            # Using range() + for loop as required
            for num in range(start, end + 1):
                
                # pass statement example (placeholder / skip logic)
                if False:          # This condition never runs
                    pass           # <-- pass is used here as required
                
                # Odd or Even check
                if num % 2 == 0:
                    print(f"Number {num} is Even")
                else:
                    print(f"Number {num} is Odd")
                
                total += num
            
            print(f"\nSum of all numbers from {start} to {end} is: {total}")
            break
            
        except ValueError:
            print("Please enter valid integers only!")


def main():
    # ========================================================
    #                    MAIN PROGRAM FLOW
    # ========================================================
    welcome_message()
    
    while True:
        show_menu()
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                generate_pattern()
                
            elif choice == 2:
                analyze_numbers()
                
            elif choice == 3:
                # ====================================================
                #                     EXIT MESSAGE
                # ====================================================
                print("\n" + "=" * 55)
                print("   Thank you for using Logic Box!")
                print("   Exiting the program. Goodbye!")
                print("=" * 55)
                break
                
            else:
                print("Invalid choice! Please select 1, 2 or 3.")
                
        except ValueError:
            print("Please enter a valid number (1, 2 or 3).")


# ============================================================
#                     PROGRAM ENTRY POINT
# ============================================================
if __name__ == "__main__":
    main()
