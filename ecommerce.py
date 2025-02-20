import numpy as np
import pandas as pd

cart_items = [
    {"Item": "webcam", "Price": 800, "Quantity": 1},
    {"Item": "printer ink", "Price": 700, "Quantity": 2},
    {"Item": "Headphones", "Price": 300, "Quantity": 3},
    {"Item": "Keyboard", "Price": 500, "Quantity": 1},
    {"Item": "Mouse", "Price": 400, "Quantity": 1},
    {"Item": "Cleaning kit", "Price": 200, "Quantity": 1},
    {"Item": "USB Drive", "Price": 30, "Quantity": 2},
]

# --- Function to Display Shopping Cart ---
def display_cart(cart):
    """Displays the shopping cart in a structured format."""
    df = pd.DataFrame(cart)
    df["Total Price"] = df["Price"] * df["Quantity"]
    print("\nShopping Cart:")
    print(df)
    return df

# --- Function to Calculate Total Bill ---
# --- Function to Perform Item Price Analysis ---
def price_analysis(cart):
    """Analyzes item price statistics using NumPy."""
    prices = np.array([item["Price"] for item in cart])
    
    stats = {
        "min": np.min(prices),
        "max": np.max(prices),
        "mean": np.mean(prices),
        "std": np.std(prices)
    }
    
    print("\nPrice Analysis:")
    print(f"Minimum Price: ${stats['min']}")
    print(f"Maximum Price: ${stats['max']}")
    print(f"Average Price: ${stats['mean']:.2f}")
    print(f"Standard Deviation of Prices: ${stats['std']:.2f}")
    
    return stats

# --- Function to Find the Most Expensive Item ---

# --- Main Function to Run the Shopping Analysis ---
def main():
    df_cart = display_cart(cart_items)  # Display cart
    price_analysis(cart_items)  # Perform price analysis
      # Find the most expensive item

if __name__ == "__main__":
    main()
