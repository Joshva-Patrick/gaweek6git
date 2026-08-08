import re
from playwright.sync_api import sync_playwright

# Replace these with the actual absolute URLs for Seed 7 through Seed 16
SEED_URLS = [
    "https://example.com/path/to/seed-7",
    "https://example.com/path/to/seed-8",
    "https://example.com/path/to/seed-9",
    "https://example.com/path/to/seed-10",
    "https://example.com/path/to/seed-11",
    "https://example.com/path/to/seed-12",
    "https://example.com/path/to/seed-13",
    "https://example.com/path/to/seed-14",
    "https://example.com/path/to/seed-15",
    "https://example.com/path/to/seed-16",
]

def main():
    total_sum = 0.0

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for url in SEED_URLS:
            page.goto(url, wait_until="networkidle")
            
            # Extract all cell elements from tables on the page
            cells = page.query_selector_all("table td, table th")
            for cell in cells:
                text = cell.inner_text().strip()
                # Find all integer or floating-point numbers in each table cell
                matches = re.findall(r"[-+]?\d*\.\d+|\d+", text)
                for num in matches:
                    total_sum += float(num)

        browser.close()

    # The auto-grader searches the workflow logs for the printed total
    print(f"TOTAL SUM: {total_sum}")

if __name__ == "__main__":
    main()