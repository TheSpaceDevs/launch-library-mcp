from .models import *
from launch_library_mcp.launch_library_client.api_client import JsonApi

from .enum import CustomEnum


class SpaceflightNewsApiClient(JsonApi):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def articles_list(
        self,
        event: List[int] = None,
        has_event: bool = None,
        has_launch: bool = None,
        is_featured: bool = None,
        launch: List[str] = None,
        limit: int = None,
        news_site: str = None,
        news_site_exclude: str = None,
        offset: int = None,
        ordering: List[CustomEnum] = None,
        published_at_gt: str = None,
        published_at_gte: str = None,
        published_at_lt: str = None,
        published_at_lte: str = None,
        search: str = None,
        summary_contains: str = None,
        summary_contains_all: str = None,
        summary_contains_one: str = None,
        title_contains: str = None,
        title_contains_all: str = None,
        title_contains_one: str = None,
        updated_at_gt: str = None,
        updated_at_gte: str = None,
        updated_at_lt: str = None,
        updated_at_lte: str = None,
        **kwargs,
    ) -> PaginatedArticleList:
        params = {
            "event": event,
            "has_event": has_event,
            "has_launch": has_launch,
            "is_featured": is_featured,
            "launch": launch,
            "limit": limit,
            "news_site": news_site,
            "news_site_exclude": news_site_exclude,
            "offset": offset,
            "ordering": ordering,
            "published_at_gt": published_at_gt,
            "published_at_gte": published_at_gte,
            "published_at_lt": published_at_lt,
            "published_at_lte": published_at_lte,
            "search": search,
            "summary_contains": summary_contains,
            "summary_contains_all": summary_contains_all,
            "summary_contains_one": summary_contains_one,
            "title_contains": title_contains,
            "title_contains_all": title_contains_all,
            "title_contains_one": title_contains_one,
            "updated_at_gt": updated_at_gt,
            "updated_at_gte": updated_at_gte,
            "updated_at_lt": updated_at_lt,
            "updated_at_lte": updated_at_lte,
            **kwargs,
        }
        response = self.get(
            f"/v4/articles/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedArticleList(**response)

    async def articles_list_async(
        self,
        event: List[int] = None,
        has_event: bool = None,
        has_launch: bool = None,
        is_featured: bool = None,
        launch: List[str] = None,
        limit: int = None,
        news_site: str = None,
        news_site_exclude: str = None,
        offset: int = None,
        ordering: List[CustomEnum] = None,
        published_at_gt: str = None,
        published_at_gte: str = None,
        published_at_lt: str = None,
        published_at_lte: str = None,
        search: str = None,
        summary_contains: str = None,
        summary_contains_all: str = None,
        summary_contains_one: str = None,
        title_contains: str = None,
        title_contains_all: str = None,
        title_contains_one: str = None,
        updated_at_gt: str = None,
        updated_at_gte: str = None,
        updated_at_lt: str = None,
        updated_at_lte: str = None,
        **kwargs,
    ) -> PaginatedArticleList:
        params = {
            "event": event,
            "has_event": has_event,
            "has_launch": has_launch,
            "is_featured": is_featured,
            "launch": launch,
            "limit": limit,
            "news_site": news_site,
            "news_site_exclude": news_site_exclude,
            "offset": offset,
            "ordering": ordering,
            "published_at_gt": published_at_gt,
            "published_at_gte": published_at_gte,
            "published_at_lt": published_at_lt,
            "published_at_lte": published_at_lte,
            "search": search,
            "summary_contains": summary_contains,
            "summary_contains_all": summary_contains_all,
            "summary_contains_one": summary_contains_one,
            "title_contains": title_contains,
            "title_contains_all": title_contains_all,
            "title_contains_one": title_contains_one,
            "updated_at_gt": updated_at_gt,
            "updated_at_gte": updated_at_gte,
            "updated_at_lt": updated_at_lt,
            "updated_at_lte": updated_at_lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/v4/articles/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedArticleList(**response)

    def articles_retrieve(self, id: int = None, **kwargs) -> Article:
        params = {**kwargs}
        response = self.get(
            f"/v4/articles/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Article(**response)

    async def articles_retrieve_async(self, id: int = None, **kwargs) -> Article:
        params = {**kwargs}
        response = await self.getAsync(
            f"/v4/articles/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Article(**response)

    def blogs_list(
        self,
        event: List[int] = None,
        has_event: bool = None,
        has_launch: bool = None,
        is_featured: bool = None,
        launch: List[str] = None,
        limit: int = None,
        news_site: str = None,
        news_site_exclude: str = None,
        offset: int = None,
        ordering: List[CustomEnum] = None,
        published_at_gt: str = None,
        published_at_gte: str = None,
        published_at_lt: str = None,
        published_at_lte: str = None,
        search: str = None,
        summary_contains: str = None,
        summary_contains_all: str = None,
        summary_contains_one: str = None,
        title_contains: str = None,
        title_contains_all: str = None,
        title_contains_one: str = None,
        updated_at_gt: str = None,
        updated_at_gte: str = None,
        updated_at_lt: str = None,
        updated_at_lte: str = None,
        **kwargs,
    ) -> PaginatedBlogList:
        params = {
            "event": event,
            "has_event": has_event,
            "has_launch": has_launch,
            "is_featured": is_featured,
            "launch": launch,
            "limit": limit,
            "news_site": news_site,
            "news_site_exclude": news_site_exclude,
            "offset": offset,
            "ordering": ordering,
            "published_at_gt": published_at_gt,
            "published_at_gte": published_at_gte,
            "published_at_lt": published_at_lt,
            "published_at_lte": published_at_lte,
            "search": search,
            "summary_contains": summary_contains,
            "summary_contains_all": summary_contains_all,
            "summary_contains_one": summary_contains_one,
            "title_contains": title_contains,
            "title_contains_all": title_contains_all,
            "title_contains_one": title_contains_one,
            "updated_at_gt": updated_at_gt,
            "updated_at_gte": updated_at_gte,
            "updated_at_lt": updated_at_lt,
            "updated_at_lte": updated_at_lte,
            **kwargs,
        }
        response = self.get(
            f"/v4/blogs/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedBlogList(**response)

    async def blogs_list_async(
        self,
        event: List[int] = None,
        has_event: bool = None,
        has_launch: bool = None,
        is_featured: bool = None,
        launch: List[str] = None,
        limit: int = None,
        news_site: str = None,
        news_site_exclude: str = None,
        offset: int = None,
        ordering: List[CustomEnum] = None,
        published_at_gt: str = None,
        published_at_gte: str = None,
        published_at_lt: str = None,
        published_at_lte: str = None,
        search: str = None,
        summary_contains: str = None,
        summary_contains_all: str = None,
        summary_contains_one: str = None,
        title_contains: str = None,
        title_contains_all: str = None,
        title_contains_one: str = None,
        updated_at_gt: str = None,
        updated_at_gte: str = None,
        updated_at_lt: str = None,
        updated_at_lte: str = None,
        **kwargs,
    ) -> PaginatedBlogList:
        params = {
            "event": event,
            "has_event": has_event,
            "has_launch": has_launch,
            "is_featured": is_featured,
            "launch": launch,
            "limit": limit,
            "news_site": news_site,
            "news_site_exclude": news_site_exclude,
            "offset": offset,
            "ordering": ordering,
            "published_at_gt": published_at_gt,
            "published_at_gte": published_at_gte,
            "published_at_lt": published_at_lt,
            "published_at_lte": published_at_lte,
            "search": search,
            "summary_contains": summary_contains,
            "summary_contains_all": summary_contains_all,
            "summary_contains_one": summary_contains_one,
            "title_contains": title_contains,
            "title_contains_all": title_contains_all,
            "title_contains_one": title_contains_one,
            "updated_at_gt": updated_at_gt,
            "updated_at_gte": updated_at_gte,
            "updated_at_lt": updated_at_lt,
            "updated_at_lte": updated_at_lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/v4/blogs/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedBlogList(**response)

    def blogs_retrieve(self, id: int = None, **kwargs) -> Blog:
        params = {**kwargs}
        response = self.get(
            f"/v4/blogs/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Blog(**response)

    async def blogs_retrieve_async(self, id: int = None, **kwargs) -> Blog:
        params = {**kwargs}
        response = await self.getAsync(
            f"/v4/blogs/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Blog(**response)

    def info_retrieve(self, **kwargs) -> Info:
        params = {**kwargs}
        response = self.get(
            f"/v4/info/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Info(**response)

    async def info_retrieve_async(self, **kwargs) -> Info:
        params = {**kwargs}
        response = await self.getAsync(
            f"/v4/info/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Info(**response)

    def reports_list(
        self,
        limit: int = None,
        news_site: str = None,
        news_site_exclude: str = None,
        offset: int = None,
        ordering: List[CustomEnum] = None,
        published_at_gt: str = None,
        published_at_gte: str = None,
        published_at_lt: str = None,
        published_at_lte: str = None,
        search: str = None,
        summary_contains: str = None,
        summary_contains_all: str = None,
        summary_contains_one: str = None,
        title_contains: str = None,
        title_contains_all: str = None,
        title_contains_one: str = None,
        updated_at_gt: str = None,
        updated_at_gte: str = None,
        updated_at_lt: str = None,
        updated_at_lte: str = None,
        **kwargs,
    ) -> PaginatedReportList:
        params = {
            "limit": limit,
            "news_site": news_site,
            "news_site_exclude": news_site_exclude,
            "offset": offset,
            "ordering": ordering,
            "published_at_gt": published_at_gt,
            "published_at_gte": published_at_gte,
            "published_at_lt": published_at_lt,
            "published_at_lte": published_at_lte,
            "search": search,
            "summary_contains": summary_contains,
            "summary_contains_all": summary_contains_all,
            "summary_contains_one": summary_contains_one,
            "title_contains": title_contains,
            "title_contains_all": title_contains_all,
            "title_contains_one": title_contains_one,
            "updated_at_gt": updated_at_gt,
            "updated_at_gte": updated_at_gte,
            "updated_at_lt": updated_at_lt,
            "updated_at_lte": updated_at_lte,
            **kwargs,
        }
        response = self.get(
            f"/v4/reports/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedReportList(**response)

    async def reports_list_async(
        self,
        limit: int = None,
        news_site: str = None,
        news_site_exclude: str = None,
        offset: int = None,
        ordering: List[CustomEnum] = None,
        published_at_gt: str = None,
        published_at_gte: str = None,
        published_at_lt: str = None,
        published_at_lte: str = None,
        search: str = None,
        summary_contains: str = None,
        summary_contains_all: str = None,
        summary_contains_one: str = None,
        title_contains: str = None,
        title_contains_all: str = None,
        title_contains_one: str = None,
        updated_at_gt: str = None,
        updated_at_gte: str = None,
        updated_at_lt: str = None,
        updated_at_lte: str = None,
        **kwargs,
    ) -> PaginatedReportList:
        params = {
            "limit": limit,
            "news_site": news_site,
            "news_site_exclude": news_site_exclude,
            "offset": offset,
            "ordering": ordering,
            "published_at_gt": published_at_gt,
            "published_at_gte": published_at_gte,
            "published_at_lt": published_at_lt,
            "published_at_lte": published_at_lte,
            "search": search,
            "summary_contains": summary_contains,
            "summary_contains_all": summary_contains_all,
            "summary_contains_one": summary_contains_one,
            "title_contains": title_contains,
            "title_contains_all": title_contains_all,
            "title_contains_one": title_contains_one,
            "updated_at_gt": updated_at_gt,
            "updated_at_gte": updated_at_gte,
            "updated_at_lt": updated_at_lt,
            "updated_at_lte": updated_at_lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/v4/reports/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedReportList(**response)

    def reports_retrieve(self, id: int = None, **kwargs) -> Report:
        params = {**kwargs}
        response = self.get(
            f"/v4/reports/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Report(**response)

    async def reports_retrieve_async(self, id: int = None, **kwargs) -> Report:
        params = {**kwargs}
        response = await self.getAsync(
            f"/v4/reports/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Report(**response)
