import asyncio
import httpx
from parsel import Selector



class CarCrawler:
    MAIN_URL = 'https://www.mashina.kg/search/all/'
    BASE_URL = 'https://www.mashina.kg'

    async def get_page(self, url: str, client: httpx.AsyncClient):
        response = await client.get(url)
        return response.text

    def get_car_data(self, page: str):
        html = Selector(page)
        car_blocks = html.css(".list-item.list-label")
        car_data = []
        for block in car_blocks:
            title = block.css(".name::text").get().strip()
            link = block.css("a::attr(href)").get()
            if link:
                full_link = self.BASE_URL + link
            price_block = block.css(".block.price strong::text").getall()
            price_usd = price_block[0].strip() if price_block else "Цена в USD не найдена"
            car_data.append({"title": title, "link": full_link, "price_usd": price_usd})
        return car_data

    async def get_cars(self):
        tasks = []
        async with httpx.AsyncClient() as client:
            for i in range(1, 5):
                url = f"{self.MAIN_URL}?page={i}"
                task = asyncio.create_task(self.get_page(url, client))
                tasks.append(task)
            results = await asyncio.gather(*tasks)
            all_car_data = []
            for result in results:
                car_data = self.get_car_data(result)
                all_car_data.extend(car_data)
            for i, car in enumerate(all_car_data, start=1):
                print(f"{i}. {car['title']} - {car['price_usd']} : {car['link']}")
            return all_car_data[:3]


if __name__ == "__main__":
    crawler = CarCrawler()
    asyncio.run(crawler.get_cars())
