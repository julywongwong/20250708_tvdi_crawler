from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as p:
        #browser = await p.chromium.launch(headless=False)
        browser = await p.firefox.launch(headless=False,slow_mo=10000)  # Use Firefox instead of Chromium
        page = await browser.new_page()
        await page.goto('https://example.com')
        await page.wait_for_selector('p') #等待元素載入
        content = await page.inner_text('p')
        print(content)
        await browser.close()


asyncio.run(main())