from enum import Enum


class CustomEnum(str, Enum):

    PUBLISHED_AT_DESC = "-published_at"
    UPDATED_AT_DESC = "-updated_at"
    PUBLISHED_AT_ASC = "published_at"
    UPDATED_AT_ASC = "updated_at"
