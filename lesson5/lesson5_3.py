import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        url = 'https://blockcast.it/2025/07/22/tom-lee-sees-eth-hitting-15k-with-ethereum-emerging-as-wall-streets-favored-blockchain/'
        result = await crawler.arun(url=url)
        print(type(result))  #列印結果的類型
        print("=" * 20)  #分隔線
        

        #列印取出的結果
        print(result.markdown)
        

if __name__ == "__main__":
    #執行主函式
    asyncio.run(main())