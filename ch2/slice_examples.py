# Examples of slicing the string "bicycle"

WORD = "bicycle"

# Slicing to get every second character
print(WORD[::2])  # Output: 'bcle'

# Slicing to get every third character
print(WORD[::3])  # Output: 'bye'

# Slicing to get the first three characters
print(WORD[:3])  # Output: 'bic'

# Slicing to get the last three characters
print(WORD[-3:])  # Output: 'cle'

# Slicing to get the characters from index 1 to 4
print(WORD[1:5])  # Output: 'icyc'

# Slicing to get the characters in reverse order
print(WORD[::-1])  # Output: 'elcycib'

print(WORD[::-2])  # Output: 'eccb'

print(
    """
##########################################
# Using slice objects
##########################################
"""
)

# Create a slice object
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 47)
QUANTITY = slice(47, 52)
ITEM_TOTAL = slice(52, None)

# Read the file and print the line items
with open(
    "ch2/invoice.txt", encoding="utf-8", mode="r"
) as invoice:
    for line in invoice:
        line_items = line
        print(
            line_items[SKU],
            line_items[DESCRIPTION],
            line_items[UNIT_PRICE],
            line_items[QUANTITY],
            line_items[ITEM_TOTAL],
        )
