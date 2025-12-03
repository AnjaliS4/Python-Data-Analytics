# price of a brick as a constant
BRICK_PRICE = 1

# thresholds and constants
THRESHOLD_1 = 1000
THRESHOLD_2 = 3000
THRESHOLD_3 = 7000

RATE_3 = 0.05   # for 1001-3000
BASE_3 = 50.0

RATE_2 = 0.10   # for 3001-7000
BASE_2 = 100.0

RATE_4 = 0.15   # for 7001 and above
BASE_4 = 150.0

# initialise discount
discount = 0.0

# read number of bricks
num_bricks = int(input("Enter number of bricks: "))

# decision structure
if num_bricks <= THRESHOLD_1:
    discount = 0
elif num_bricks <= THRESHOLD_2:
    discount = (num_bricks - THRESHOLD_1) * BRICK_PRICE * RATE_3 - BASE_3
elif num_bricks <= THRESHOLD_3:
    discount = (num_bricks - THRESHOLD_2) * BRICK_PRICE * RATE_2 - BASE_2
else:
    discount = (num_bricks - THRESHOLD_3) * BRICK_PRICE * RATE_4 - BASE_4

# print output
print(f"Discount: ${discount:.2f}")
