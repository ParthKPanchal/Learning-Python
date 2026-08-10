from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://mr-parth-k-panchal-react-portfolio.netlify.app/")

# 1. Page title
print("Page Title:", driver.title)

# 2. Current URL
print("Current URL:", driver.current_url)

# 3. Find all H1 tags
headings = driver.find_elements("xpath", "//h1")

print("Number of H1 tags:", len(headings))

for heading in headings:
    print("H1:", heading.text)

# 4. Find all links
links = driver.find_elements("tag name", "a")

print("Number of links:", len(links))

for link in links:
    print(link.text)

driver.quit()