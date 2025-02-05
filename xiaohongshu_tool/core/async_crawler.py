"""
异步爬虫模块
使用aiohttp实现高性能请求
"""
import aiohttp
import asyncio
from typing import AsyncGenerator

class AsyncCrawler:
    def __init__(self, session):
        self.session = session
        self.semaphore = asyncio.Semaphore(10)  # 并发控制

    async def fetch(self, url: str) -> AsyncGenerator:
        async with self.semaphore:
            async with self.session.get(url) as response:
                yield await response.text()

    async def batch_fetch(self, urls: list):
        tasks = [self.fetch(url) for url in urls]
        return await asyncio.gather(*tasks) 