from fastapi import FastAPI
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test-bs4")
async def test_bs4():
    # Create a sample HTML string
    html_content = """
    <html>
        <body>
            <h1>Test Heading</h1>
            <p class="test-class">This is a test paragraph</p>
            <ul>
                <li>Item 1</li>
                <li>Item 2</li>
            </ul>
        </body>
    </html>
    """
    
    # Parse HTML using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract some data to demonstrate parsing
    return {
        "heading": soup.h1.text,
        "paragraph": soup.p.text,
        "list_items": [item.text for item in soup.find_all('li')],
        "paragraph_class": soup.p['class'][0]
    }
    
