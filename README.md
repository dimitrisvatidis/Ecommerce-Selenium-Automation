Ecommerce Selenium Automation

This project is a fully automated end-to-end (E2E) test script built with **Python** and **Selenium WebDriver**. It simulates a realistic user journey on a demo e-commerce site, from registration to checkout.

---

What It Does

The script performs the following actions:

1. Launches a browser and navigates to `http://demostore.supersqa.com/`
2. Accepts cookies and handles alerts
3. Registers a new user with a randomly generated email and secure password
4. Searches for a random clothing item
5. Selects a product (and randomizes options like size, color, or logo if available)
6. Adds the product to the cart and proceeds to checkout
7. Fills in billing information with randomly generated Greek names, addresses, and phone numbers
8. Submits the order
9. Returns to the home page
10. Prints runtime statistics and all generated user/order details

---

Technologies Used

- Python 3.x
- Selenium WebDriver
- ChromeDriver (for browser automation)
- `random`, `string`, `time` (Python built-in libraries)

---

Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:dimitrisvatidis/Ecommerce-Selenium-Automation.git
   cd Ecommerce-Selenium-Automation
