from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List


class Report(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    title: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
    news_site: Optional[str] = None
    summary: Optional[str] = None
    published_at: Optional[str] = None
    updated_at: Optional[str] = None


class PaginatedReportList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[Report]] = None


class Launch(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    launch_id: Optional[str] = None
    provider: Optional[str] = None


class Event(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    event_id: Optional[int] = None
    provider: Optional[str] = None


class Blog(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    title: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
    news_site: Optional[str] = None
    summary: Optional[str] = None
    published_at: Optional[str] = None
    updated_at: Optional[str] = None
    featured: Optional[bool] = None
    launches: Optional[List[Launch]] = None
    events: Optional[List[Event]] = None


class PaginatedBlogList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[Blog]] = None


class Article(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    title: Optional[str] = None
    url: Optional[str] = None
    image_url: Optional[str] = None
    news_site: Optional[str] = None
    summary: Optional[str] = None
    published_at: Optional[str] = None
    updated_at: Optional[str] = None
    featured: Optional[bool] = None
    launches: Optional[List[Launch]] = None
    events: Optional[List[Event]] = None


class PaginatedArticleList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[Article]] = None


class Info(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    version: Optional[str] = None
    news_sites: Optional[List[str]] = None
