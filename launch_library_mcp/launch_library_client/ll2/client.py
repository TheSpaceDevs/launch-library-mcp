from typing import List
from .models import *
from launch_library_mcp.launch_library_client.api_client import JsonApi


class LaunchLibrary2DocsClient(JsonApi):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def agencies_list(
        self,
        abbrev: str = None,
        abbrev__contains: str = None,
        attempted_landings: int = None,
        attempted_landings__gt: int = None,
        attempted_landings__gte: int = None,
        attempted_landings__lt: int = None,
        attempted_landings__lte: int = None,
        consecutive_successful_landings: int = None,
        consecutive_successful_landings__gt: int = None,
        consecutive_successful_landings__gte: int = None,
        consecutive_successful_landings__lt: int = None,
        consecutive_successful_landings__lte: int = None,
        consecutive_successful_launches: int = None,
        consecutive_successful_launches__gt: int = None,
        consecutive_successful_launches__gte: int = None,
        consecutive_successful_launches__lt: int = None,
        consecutive_successful_launches__lte: int = None,
        country_code: List[str] = None,
        description: str = None,
        description__contains: str = None,
        failed_landings: int = None,
        failed_landings__gt: int = None,
        failed_landings__gte: int = None,
        failed_landings__lt: int = None,
        failed_landings__lte: int = None,
        failed_launches: int = None,
        failed_launches__gt: int = None,
        failed_launches__gte: int = None,
        failed_launches__lt: int = None,
        failed_launches__lte: int = None,
        featured: bool = None,
        founding_year: int = None,
        founding_year__gt: int = None,
        founding_year__gte: int = None,
        founding_year__lt: int = None,
        founding_year__lte: int = None,
        id: int = None,
        limit: int = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        parent__id: int = None,
        pending_launches: int = None,
        pending_launches__gt: int = None,
        pending_launches__gte: int = None,
        pending_launches__lt: int = None,
        pending_launches__lte: int = None,
        search: str = None,
        spacecraft: bool = None,
        successful_landings: int = None,
        successful_landings__gt: int = None,
        successful_landings__gte: int = None,
        successful_landings__lt: int = None,
        successful_landings__lte: int = None,
        successful_launches: int = None,
        successful_launches__gt: int = None,
        successful_launches__gte: int = None,
        successful_launches__lt: int = None,
        successful_launches__lte: int = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        type__id: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicAgencyEndpointList:
        params = {
            "abbrev": abbrev,
            "abbrev__contains": abbrev__contains,
            "attempted_landings": attempted_landings,
            "attempted_landings__gt": attempted_landings__gt,
            "attempted_landings__gte": attempted_landings__gte,
            "attempted_landings__lt": attempted_landings__lt,
            "attempted_landings__lte": attempted_landings__lte,
            "consecutive_successful_landings": consecutive_successful_landings,
            "consecutive_successful_landings__gt": consecutive_successful_landings__gt,
            "consecutive_successful_landings__gte": consecutive_successful_landings__gte,
            "consecutive_successful_landings__lt": consecutive_successful_landings__lt,
            "consecutive_successful_landings__lte": consecutive_successful_landings__lte,
            "consecutive_successful_launches": consecutive_successful_launches,
            "consecutive_successful_launches__gt": consecutive_successful_launches__gt,
            "consecutive_successful_launches__gte": consecutive_successful_launches__gte,
            "consecutive_successful_launches__lt": consecutive_successful_launches__lt,
            "consecutive_successful_launches__lte": consecutive_successful_launches__lte,
            "country_code": country_code,
            "description": description,
            "description__contains": description__contains,
            "failed_landings": failed_landings,
            "failed_landings__gt": failed_landings__gt,
            "failed_landings__gte": failed_landings__gte,
            "failed_landings__lt": failed_landings__lt,
            "failed_landings__lte": failed_landings__lte,
            "failed_launches": failed_launches,
            "failed_launches__gt": failed_launches__gt,
            "failed_launches__gte": failed_launches__gte,
            "failed_launches__lt": failed_launches__lt,
            "failed_launches__lte": failed_launches__lte,
            "featured": featured,
            "founding_year": founding_year,
            "founding_year__gt": founding_year__gt,
            "founding_year__gte": founding_year__gte,
            "founding_year__lt": founding_year__lt,
            "founding_year__lte": founding_year__lte,
            "id": id,
            "limit": limit,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "parent__id": parent__id,
            "pending_launches": pending_launches,
            "pending_launches__gt": pending_launches__gt,
            "pending_launches__gte": pending_launches__gte,
            "pending_launches__lt": pending_launches__lt,
            "pending_launches__lte": pending_launches__lte,
            "search": search,
            "spacecraft": spacecraft,
            "successful_landings": successful_landings,
            "successful_landings__gt": successful_landings__gt,
            "successful_landings__gte": successful_landings__gte,
            "successful_landings__lt": successful_landings__lt,
            "successful_landings__lte": successful_landings__lte,
            "successful_launches": successful_launches,
            "successful_launches__gt": successful_launches__gt,
            "successful_launches__gte": successful_launches__gte,
            "successful_launches__lt": successful_launches__lt,
            "successful_launches__lte": successful_launches__lte,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            "type__id": type__id,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/agencies/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicAgencyEndpointList(**response)

    async def agencies_list_async(
        self,
        abbrev: str = None,
        abbrev__contains: str = None,
        attempted_landings: int = None,
        attempted_landings__gt: int = None,
        attempted_landings__gte: int = None,
        attempted_landings__lt: int = None,
        attempted_landings__lte: int = None,
        consecutive_successful_landings: int = None,
        consecutive_successful_landings__gt: int = None,
        consecutive_successful_landings__gte: int = None,
        consecutive_successful_landings__lt: int = None,
        consecutive_successful_landings__lte: int = None,
        consecutive_successful_launches: int = None,
        consecutive_successful_launches__gt: int = None,
        consecutive_successful_launches__gte: int = None,
        consecutive_successful_launches__lt: int = None,
        consecutive_successful_launches__lte: int = None,
        country_code: List[str] = None,
        description: str = None,
        description__contains: str = None,
        failed_landings: int = None,
        failed_landings__gt: int = None,
        failed_landings__gte: int = None,
        failed_landings__lt: int = None,
        failed_landings__lte: int = None,
        failed_launches: int = None,
        failed_launches__gt: int = None,
        failed_launches__gte: int = None,
        failed_launches__lt: int = None,
        failed_launches__lte: int = None,
        featured: bool = None,
        founding_year: int = None,
        founding_year__gt: int = None,
        founding_year__gte: int = None,
        founding_year__lt: int = None,
        founding_year__lte: int = None,
        id: int = None,
        limit: int = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        parent__id: int = None,
        pending_launches: int = None,
        pending_launches__gt: int = None,
        pending_launches__gte: int = None,
        pending_launches__lt: int = None,
        pending_launches__lte: int = None,
        search: str = None,
        spacecraft: bool = None,
        successful_landings: int = None,
        successful_landings__gt: int = None,
        successful_landings__gte: int = None,
        successful_landings__lt: int = None,
        successful_landings__lte: int = None,
        successful_launches: int = None,
        successful_launches__gt: int = None,
        successful_launches__gte: int = None,
        successful_launches__lt: int = None,
        successful_launches__lte: int = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        type__id: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicAgencyEndpointList:
        params = {
            "abbrev": abbrev,
            "abbrev__contains": abbrev__contains,
            "attempted_landings": attempted_landings,
            "attempted_landings__gt": attempted_landings__gt,
            "attempted_landings__gte": attempted_landings__gte,
            "attempted_landings__lt": attempted_landings__lt,
            "attempted_landings__lte": attempted_landings__lte,
            "consecutive_successful_landings": consecutive_successful_landings,
            "consecutive_successful_landings__gt": consecutive_successful_landings__gt,
            "consecutive_successful_landings__gte": consecutive_successful_landings__gte,
            "consecutive_successful_landings__lt": consecutive_successful_landings__lt,
            "consecutive_successful_landings__lte": consecutive_successful_landings__lte,
            "consecutive_successful_launches": consecutive_successful_launches,
            "consecutive_successful_launches__gt": consecutive_successful_launches__gt,
            "consecutive_successful_launches__gte": consecutive_successful_launches__gte,
            "consecutive_successful_launches__lt": consecutive_successful_launches__lt,
            "consecutive_successful_launches__lte": consecutive_successful_launches__lte,
            "country_code": country_code,
            "description": description,
            "description__contains": description__contains,
            "failed_landings": failed_landings,
            "failed_landings__gt": failed_landings__gt,
            "failed_landings__gte": failed_landings__gte,
            "failed_landings__lt": failed_landings__lt,
            "failed_landings__lte": failed_landings__lte,
            "failed_launches": failed_launches,
            "failed_launches__gt": failed_launches__gt,
            "failed_launches__gte": failed_launches__gte,
            "failed_launches__lt": failed_launches__lt,
            "failed_launches__lte": failed_launches__lte,
            "featured": featured,
            "founding_year": founding_year,
            "founding_year__gt": founding_year__gt,
            "founding_year__gte": founding_year__gte,
            "founding_year__lt": founding_year__lt,
            "founding_year__lte": founding_year__lte,
            "id": id,
            "limit": limit,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "parent__id": parent__id,
            "pending_launches": pending_launches,
            "pending_launches__gt": pending_launches__gt,
            "pending_launches__gte": pending_launches__gte,
            "pending_launches__lt": pending_launches__lt,
            "pending_launches__lte": pending_launches__lte,
            "search": search,
            "spacecraft": spacecraft,
            "successful_landings": successful_landings,
            "successful_landings__gt": successful_landings__gt,
            "successful_landings__gte": successful_landings__gte,
            "successful_landings__lt": successful_landings__lt,
            "successful_landings__lte": successful_landings__lte,
            "successful_launches": successful_launches,
            "successful_launches__gt": successful_launches__gt,
            "successful_launches__gte": successful_launches__gte,
            "successful_launches__lt": successful_launches__lt,
            "successful_launches__lte": successful_launches__lte,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            "type__id": type__id,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/agencies/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicAgencyEndpointList(**response)

    def agencies_retrieve(self, id: int = None, **kwargs) -> AgencyEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/agencies/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AgencyEndpointDetailed(**response)

    async def agencies_retrieve_async(
        self, id: int = None, **kwargs
    ) -> AgencyEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/agencies/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AgencyEndpointDetailed(**response)

    def api_throttle_list(self, **kwargs) -> APIThrottle:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/api-throttle/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return APIThrottle(**response)

    async def api_throttle_list_async(self, **kwargs) -> APIThrottle:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/api-throttle/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return APIThrottle(**response)

    def astronauts_list(
        self,
        age: int = None,
        age__gt: int = None,
        age__gte: int = None,
        age__lt: int = None,
        age__lte: int = None,
        agency_ids: List[float] = None,
        date_of_birth: str = None,
        date_of_birth__gt: str = None,
        date_of_birth__gte: str = None,
        date_of_birth__lt: str = None,
        date_of_birth__lte: str = None,
        date_of_death: str = None,
        date_of_death__gt: str = None,
        date_of_death__gte: str = None,
        date_of_death__lt: str = None,
        date_of_death__lte: str = None,
        first_flight: str = None,
        first_flight__gt: str = None,
        first_flight__gte: str = None,
        first_flight__lt: str = None,
        first_flight__lte: str = None,
        flights_count: int = None,
        flights_count__gt: int = None,
        flights_count__gte: int = None,
        flights_count__lt: int = None,
        flights_count__lte: int = None,
        has_flown: bool = None,
        in_space: bool = None,
        is_human: bool = None,
        landings_count: int = None,
        landings_count__gt: int = None,
        landings_count__gte: int = None,
        landings_count__lt: int = None,
        landings_count__lte: int = None,
        last_flight: str = None,
        last_flight__gt: str = None,
        last_flight__gte: str = None,
        last_flight__lt: str = None,
        last_flight__lte: str = None,
        limit: int = None,
        nationality: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        status_ids: List[float] = None,
        type__id: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicAstronautEndpointList:
        params = {
            "age": age,
            "age__gt": age__gt,
            "age__gte": age__gte,
            "age__lt": age__lt,
            "age__lte": age__lte,
            "agency_ids": agency_ids,
            "date_of_birth": date_of_birth,
            "date_of_birth__gt": date_of_birth__gt,
            "date_of_birth__gte": date_of_birth__gte,
            "date_of_birth__lt": date_of_birth__lt,
            "date_of_birth__lte": date_of_birth__lte,
            "date_of_death": date_of_death,
            "date_of_death__gt": date_of_death__gt,
            "date_of_death__gte": date_of_death__gte,
            "date_of_death__lt": date_of_death__lt,
            "date_of_death__lte": date_of_death__lte,
            "first_flight": first_flight,
            "first_flight__gt": first_flight__gt,
            "first_flight__gte": first_flight__gte,
            "first_flight__lt": first_flight__lt,
            "first_flight__lte": first_flight__lte,
            "flights_count": flights_count,
            "flights_count__gt": flights_count__gt,
            "flights_count__gte": flights_count__gte,
            "flights_count__lt": flights_count__lt,
            "flights_count__lte": flights_count__lte,
            "has_flown": has_flown,
            "in_space": in_space,
            "is_human": is_human,
            "landings_count": landings_count,
            "landings_count__gt": landings_count__gt,
            "landings_count__gte": landings_count__gte,
            "landings_count__lt": landings_count__lt,
            "landings_count__lte": landings_count__lte,
            "last_flight": last_flight,
            "last_flight__gt": last_flight__gt,
            "last_flight__gte": last_flight__gte,
            "last_flight__lt": last_flight__lt,
            "last_flight__lte": last_flight__lte,
            "limit": limit,
            "nationality": nationality,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "status_ids": status_ids,
            "type__id": type__id,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/astronauts/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicAstronautEndpointList(**response)

    async def astronauts_list_async(
        self,
        age: int = None,
        age__gt: int = None,
        age__gte: int = None,
        age__lt: int = None,
        age__lte: int = None,
        agency_ids: List[float] = None,
        date_of_birth: str = None,
        date_of_birth__gt: str = None,
        date_of_birth__gte: str = None,
        date_of_birth__lt: str = None,
        date_of_birth__lte: str = None,
        date_of_death: str = None,
        date_of_death__gt: str = None,
        date_of_death__gte: str = None,
        date_of_death__lt: str = None,
        date_of_death__lte: str = None,
        first_flight: str = None,
        first_flight__gt: str = None,
        first_flight__gte: str = None,
        first_flight__lt: str = None,
        first_flight__lte: str = None,
        flights_count: int = None,
        flights_count__gt: int = None,
        flights_count__gte: int = None,
        flights_count__lt: int = None,
        flights_count__lte: int = None,
        has_flown: bool = None,
        in_space: bool = None,
        is_human: bool = None,
        landings_count: int = None,
        landings_count__gt: int = None,
        landings_count__gte: int = None,
        landings_count__lt: int = None,
        landings_count__lte: int = None,
        last_flight: str = None,
        last_flight__gt: str = None,
        last_flight__gte: str = None,
        last_flight__lt: str = None,
        last_flight__lte: str = None,
        limit: int = None,
        nationality: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        status_ids: List[float] = None,
        type__id: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicAstronautEndpointList:
        params = {
            "age": age,
            "age__gt": age__gt,
            "age__gte": age__gte,
            "age__lt": age__lt,
            "age__lte": age__lte,
            "agency_ids": agency_ids,
            "date_of_birth": date_of_birth,
            "date_of_birth__gt": date_of_birth__gt,
            "date_of_birth__gte": date_of_birth__gte,
            "date_of_birth__lt": date_of_birth__lt,
            "date_of_birth__lte": date_of_birth__lte,
            "date_of_death": date_of_death,
            "date_of_death__gt": date_of_death__gt,
            "date_of_death__gte": date_of_death__gte,
            "date_of_death__lt": date_of_death__lt,
            "date_of_death__lte": date_of_death__lte,
            "first_flight": first_flight,
            "first_flight__gt": first_flight__gt,
            "first_flight__gte": first_flight__gte,
            "first_flight__lt": first_flight__lt,
            "first_flight__lte": first_flight__lte,
            "flights_count": flights_count,
            "flights_count__gt": flights_count__gt,
            "flights_count__gte": flights_count__gte,
            "flights_count__lt": flights_count__lt,
            "flights_count__lte": flights_count__lte,
            "has_flown": has_flown,
            "in_space": in_space,
            "is_human": is_human,
            "landings_count": landings_count,
            "landings_count__gt": landings_count__gt,
            "landings_count__gte": landings_count__gte,
            "landings_count__lt": landings_count__lt,
            "landings_count__lte": landings_count__lte,
            "last_flight": last_flight,
            "last_flight__gt": last_flight__gt,
            "last_flight__gte": last_flight__gte,
            "last_flight__lt": last_flight__lt,
            "last_flight__lte": last_flight__lte,
            "limit": limit,
            "nationality": nationality,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "status_ids": status_ids,
            "type__id": type__id,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/astronauts/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicAstronautEndpointList(**response)

    def astronauts_retrieve(
        self, id: int = None, **kwargs
    ) -> AstronautEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/astronauts/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AstronautEndpointDetailed(**response)

    async def astronauts_retrieve_async(
        self, id: int = None, **kwargs
    ) -> AstronautEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/astronauts/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AstronautEndpointDetailed(**response)

    def celestial_bodies_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicCelestialBodyEndpointList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/celestial_bodies/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicCelestialBodyEndpointList(**response)

    async def celestial_bodies_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicCelestialBodyEndpointList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/celestial_bodies/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicCelestialBodyEndpointList(**response)

    def celestial_bodies_retrieve(
        self, id: int = None, **kwargs
    ) -> CelestialBodyEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/celestial_bodies/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return CelestialBodyEndpointDetailed(**response)

    async def celestial_bodies_retrieve_async(
        self, id: int = None, **kwargs
    ) -> CelestialBodyEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/celestial_bodies/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return CelestialBodyEndpointDetailed(**response)

    def config_agency_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedAgencyTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/agency_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedAgencyTypeList(**response)

    async def config_agency_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedAgencyTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/agency_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedAgencyTypeList(**response)

    def config_agency_types_retrieve(self, id: int = None, **kwargs) -> AgencyType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/agency_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AgencyType(**response)

    async def config_agency_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> AgencyType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/agency_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AgencyType(**response)

    def config_astronaut_roles_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedAstronautRoleList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/astronaut_roles/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedAstronautRoleList(**response)

    async def config_astronaut_roles_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedAstronautRoleList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/astronaut_roles/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedAstronautRoleList(**response)

    def config_astronaut_roles_retrieve(
        self, id: int = None, **kwargs
    ) -> AstronautRole:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/astronaut_roles/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AstronautRole(**response)

    async def config_astronaut_roles_retrieve_async(
        self, id: int = None, **kwargs
    ) -> AstronautRole:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/astronaut_roles/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AstronautRole(**response)

    def config_astronaut_statuses_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedAstronautStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/astronaut_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedAstronautStatusList(**response)

    async def config_astronaut_statuses_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedAstronautStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/astronaut_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedAstronautStatusList(**response)

    def config_astronaut_statuses_retrieve(
        self, id: int = None, **kwargs
    ) -> AstronautStatus:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/astronaut_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AstronautStatus(**response)

    async def config_astronaut_statuses_retrieve_async(
        self, id: int = None, **kwargs
    ) -> AstronautStatus:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/astronaut_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AstronautStatus(**response)

    def config_astronaut_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedAstronautTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/astronaut_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedAstronautTypeList(**response)

    async def config_astronaut_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedAstronautTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/astronaut_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedAstronautTypeList(**response)

    def config_astronaut_types_retrieve(
        self, id: int = None, **kwargs
    ) -> AstronautType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/astronaut_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AstronautType(**response)

    async def config_astronaut_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> AstronautType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/astronaut_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return AstronautType(**response)

    def config_celestial_body_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedCelestialBodyTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/celestial_body_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedCelestialBodyTypeList(**response)

    async def config_celestial_body_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedCelestialBodyTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/celestial_body_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedCelestialBodyTypeList(**response)

    def config_celestial_body_types_retrieve(
        self, id: int = None, **kwargs
    ) -> CelestialBodyType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/celestial_body_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return CelestialBodyType(**response)

    async def config_celestial_body_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> CelestialBodyType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/celestial_body_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return CelestialBodyType(**response)

    def config_countries_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedCountryList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/countries/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedCountryList(**response)

    async def config_countries_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedCountryList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/countries/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedCountryList(**response)

    def config_countries_retrieve(self, id: int = None, **kwargs) -> Country:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/countries/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Country(**response)

    async def config_countries_retrieve_async(
        self, id: int = None, **kwargs
    ) -> Country:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/countries/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Country(**response)

    def config_docking_locations_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedDockingLocationList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/docking_locations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedDockingLocationList(**response)

    async def config_docking_locations_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedDockingLocationList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/docking_locations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedDockingLocationList(**response)

    def config_docking_locations_retrieve(
        self, id: int = None, **kwargs
    ) -> DockingLocation:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/docking_locations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return DockingLocation(**response)

    async def config_docking_locations_retrieve_async(
        self, id: int = None, **kwargs
    ) -> DockingLocation:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/docking_locations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return DockingLocation(**response)

    def config_event_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedEventTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/event_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedEventTypeList(**response)

    async def config_event_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedEventTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/event_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedEventTypeList(**response)

    def config_event_types_retrieve(self, id: int = None, **kwargs) -> EventType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/event_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return EventType(**response)

    async def config_event_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> EventType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/event_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return EventType(**response)

    def config_first_stage_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedFirstStageTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/first_stage_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedFirstStageTypeList(**response)

    async def config_first_stage_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedFirstStageTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/first_stage_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedFirstStageTypeList(**response)

    def config_first_stage_types_retrieve(
        self, id: int = None, **kwargs
    ) -> FirstStageType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/first_stage_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return FirstStageType(**response)

    async def config_first_stage_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> FirstStageType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/first_stage_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return FirstStageType(**response)

    def config_image_licenses_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedImageLicenseList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/image_licenses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedImageLicenseList(**response)

    async def config_image_licenses_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedImageLicenseList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/image_licenses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedImageLicenseList(**response)

    def config_image_licenses_retrieve(self, id: int = None, **kwargs) -> ImageLicense:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/image_licenses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ImageLicense(**response)

    async def config_image_licenses_retrieve_async(
        self, id: int = None, **kwargs
    ) -> ImageLicense:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/image_licenses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ImageLicense(**response)

    def config_image_variant_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedImageVariantTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/image_variant_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedImageVariantTypeList(**response)

    async def config_image_variant_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedImageVariantTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/image_variant_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedImageVariantTypeList(**response)

    def config_image_variant_types_retrieve(
        self, id: int = None, **kwargs
    ) -> ImageVariantType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/image_variant_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ImageVariantType(**response)

    async def config_image_variant_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> ImageVariantType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/image_variant_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ImageVariantType(**response)

    def config_infourl_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedInfoURLTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/infourl_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedInfoURLTypeList(**response)

    async def config_infourl_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedInfoURLTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/infourl_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedInfoURLTypeList(**response)

    def config_infourl_types_retrieve(self, id: int = None, **kwargs) -> InfoURLType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/infourl_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return InfoURLType(**response)

    async def config_infourl_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> InfoURLType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/infourl_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return InfoURLType(**response)

    def config_landing_locations_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLandingLocationList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/landing_locations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLandingLocationList(**response)

    async def config_landing_locations_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLandingLocationList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/landing_locations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLandingLocationList(**response)

    def config_landing_locations_retrieve(
        self, id: int = None, **kwargs
    ) -> LandingLocation:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/landing_locations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LandingLocation(**response)

    async def config_landing_locations_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LandingLocation:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/landing_locations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LandingLocation(**response)

    def config_landing_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLandingTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/landing_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLandingTypeList(**response)

    async def config_landing_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLandingTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/landing_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLandingTypeList(**response)

    def config_landing_types_retrieve(self, id: int = None, **kwargs) -> LandingType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/landing_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LandingType(**response)

    async def config_landing_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LandingType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/landing_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LandingType(**response)

    def config_languages_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLanguageList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/languages/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLanguageList(**response)

    async def config_languages_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLanguageList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/languages/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLanguageList(**response)

    def config_languages_retrieve(self, id: int = None, **kwargs) -> Language:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/languages/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Language(**response)

    async def config_languages_retrieve_async(
        self, id: int = None, **kwargs
    ) -> Language:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/languages/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Language(**response)

    def config_launch_statuses_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLaunchStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/launch_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLaunchStatusList(**response)

    async def config_launch_statuses_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLaunchStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/launch_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLaunchStatusList(**response)

    def config_launch_statuses_retrieve(self, id: int = None, **kwargs) -> LaunchStatus:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/launch_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LaunchStatus(**response)

    async def config_launch_statuses_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LaunchStatus:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/launch_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LaunchStatus(**response)

    def config_launcher_statuses_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLauncherStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/launcher_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLauncherStatusList(**response)

    async def config_launcher_statuses_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedLauncherStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/launcher_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedLauncherStatusList(**response)

    def config_launcher_statuses_retrieve(
        self, id: int = None, **kwargs
    ) -> LauncherStatus:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/launcher_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LauncherStatus(**response)

    async def config_launcher_statuses_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LauncherStatus:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/launcher_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LauncherStatus(**response)

    def config_mission_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedMissionTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/mission_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedMissionTypeList(**response)

    async def config_mission_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedMissionTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/mission_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedMissionTypeList(**response)

    def config_mission_types_retrieve(self, id: int = None, **kwargs) -> MissionType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/mission_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return MissionType(**response)

    async def config_mission_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> MissionType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/mission_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return MissionType(**response)

    def config_net_precisions_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedNetPrecisionList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/net_precisions/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedNetPrecisionList(**response)

    async def config_net_precisions_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedNetPrecisionList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/net_precisions/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedNetPrecisionList(**response)

    def config_net_precisions_retrieve(self, id: int = None, **kwargs) -> NetPrecision:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/net_precisions/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return NetPrecision(**response)

    async def config_net_precisions_retrieve_async(
        self, id: int = None, **kwargs
    ) -> NetPrecision:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/net_precisions/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return NetPrecision(**response)

    def config_notice_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedNoticeTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/notice_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedNoticeTypeList(**response)

    async def config_notice_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedNoticeTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/notice_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedNoticeTypeList(**response)

    def config_notice_types_retrieve(self, id: int = None, **kwargs) -> NoticeType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/notice_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return NoticeType(**response)

    async def config_notice_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> NoticeType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/notice_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return NoticeType(**response)

    def config_orbits_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedOrbitList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/orbits/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedOrbitList(**response)

    async def config_orbits_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedOrbitList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/orbits/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedOrbitList(**response)

    def config_orbits_retrieve(self, id: int = None, **kwargs) -> Orbit:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/orbits/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Orbit(**response)

    async def config_orbits_retrieve_async(self, id: int = None, **kwargs) -> Orbit:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/orbits/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Orbit(**response)

    def config_payload_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPayloadTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/payload_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPayloadTypeList(**response)

    async def config_payload_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPayloadTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/payload_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPayloadTypeList(**response)

    def config_payload_types_retrieve(self, id: int = None, **kwargs) -> PayloadType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/payload_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PayloadType(**response)

    async def config_payload_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> PayloadType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/payload_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PayloadType(**response)

    def config_program_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedProgramTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/program_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedProgramTypeList(**response)

    async def config_program_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedProgramTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/program_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedProgramTypeList(**response)

    def config_program_types_retrieve(self, id: int = None, **kwargs) -> ProgramType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/program_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ProgramType(**response)

    async def config_program_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> ProgramType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/program_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ProgramType(**response)

    def config_road_closure_statuses_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedRoadClosureStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/road_closure_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedRoadClosureStatusList(**response)

    async def config_road_closure_statuses_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedRoadClosureStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/road_closure_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedRoadClosureStatusList(**response)

    def config_road_closure_statuses_retrieve(
        self, id: int = None, **kwargs
    ) -> RoadClosureStatus:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/road_closure_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return RoadClosureStatus(**response)

    async def config_road_closure_statuses_retrieve_async(
        self, id: int = None, **kwargs
    ) -> RoadClosureStatus:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/road_closure_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return RoadClosureStatus(**response)

    def config_space_station_statuses_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedSpaceStationStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/space_station_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedSpaceStationStatusList(**response)

    async def config_space_station_statuses_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedSpaceStationStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/space_station_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedSpaceStationStatusList(**response)

    def config_space_station_statuses_retrieve(
        self, id: int = None, **kwargs
    ) -> SpaceStationStatus:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/space_station_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpaceStationStatus(**response)

    async def config_space_station_statuses_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpaceStationStatus:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/space_station_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpaceStationStatus(**response)

    def config_spacecraft_configuration_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedSpacecraftConfigTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/spacecraft_configuration_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedSpacecraftConfigTypeList(**response)

    async def config_spacecraft_configuration_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedSpacecraftConfigTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/spacecraft_configuration_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedSpacecraftConfigTypeList(**response)

    def config_spacecraft_configuration_types_retrieve(
        self, id: int = None, **kwargs
    ) -> SpacecraftConfigType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/spacecraft_configuration_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftConfigType(**response)

    async def config_spacecraft_configuration_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpacecraftConfigType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/spacecraft_configuration_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftConfigType(**response)

    def config_spacecraft_statuses_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedSpacecraftStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/spacecraft_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedSpacecraftStatusList(**response)

    async def config_spacecraft_statuses_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedSpacecraftStatusList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/spacecraft_statuses/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedSpacecraftStatusList(**response)

    def config_spacecraft_statuses_retrieve(
        self, id: int = None, **kwargs
    ) -> SpacecraftStatus:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/spacecraft_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftStatus(**response)

    async def config_spacecraft_statuses_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpacecraftStatus:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/spacecraft_statuses/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftStatus(**response)

    def config_timeline_event_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedTimelineEventTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/timeline_event_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedTimelineEventTypeList(**response)

    async def config_timeline_event_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedTimelineEventTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/timeline_event_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedTimelineEventTypeList(**response)

    def config_timeline_event_types_retrieve(
        self, id: int = None, **kwargs
    ) -> TimelineEventType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/timeline_event_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return TimelineEventType(**response)

    async def config_timeline_event_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> TimelineEventType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/timeline_event_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return TimelineEventType(**response)

    def config_vidurl_types_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedVidURLTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/config/vidurl_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedVidURLTypeList(**response)

    async def config_vidurl_types_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedVidURLTypeList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/config/vidurl_types/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedVidURLTypeList(**response)

    def config_vidurl_types_retrieve(self, id: int = None, **kwargs) -> VidURLType:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/config/vidurl_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return VidURLType(**response)

    async def config_vidurl_types_retrieve_async(
        self, id: int = None, **kwargs
    ) -> VidURLType:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/config/vidurl_types/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return VidURLType(**response)

    def dashboard_starship_list(
        self, **kwargs
    ) -> List[PolymorphicStarshipDashboardEndpoint]:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/dashboard/starship/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return [PolymorphicStarshipDashboardEndpoint(**item) for item in response]

    async def dashboard_starship_list_async(
        self, **kwargs
    ) -> List[PolymorphicStarshipDashboardEndpoint]:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/dashboard/starship/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return [PolymorphicStarshipDashboardEndpoint(**item) for item in response]

    def docking_events_list(
        self,
        docking__gt: str = None,
        docking__gte: str = None,
        docking__lt: str = None,
        docking__lte: str = None,
        docking_location__id: int = None,
        flight_vehicle_chaser__id: int = None,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        space_station_target__id: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicDockingEventEndpointList:
        params = {
            "docking__gt": docking__gt,
            "docking__gte": docking__gte,
            "docking__lt": docking__lt,
            "docking__lte": docking__lte,
            "docking_location__id": docking_location__id,
            "flight_vehicle_chaser__id": flight_vehicle_chaser__id,
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "space_station_target__id": space_station_target__id,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/docking_events/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicDockingEventEndpointList(**response)

    async def docking_events_list_async(
        self,
        docking__gt: str = None,
        docking__gte: str = None,
        docking__lt: str = None,
        docking__lte: str = None,
        docking_location__id: int = None,
        flight_vehicle_chaser__id: int = None,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        space_station_target__id: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicDockingEventEndpointList:
        params = {
            "docking__gt": docking__gt,
            "docking__gte": docking__gte,
            "docking__lt": docking__lt,
            "docking__lte": docking__lte,
            "docking_location__id": docking_location__id,
            "flight_vehicle_chaser__id": flight_vehicle_chaser__id,
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "space_station_target__id": space_station_target__id,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/docking_events/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicDockingEventEndpointList(**response)

    def docking_events_retrieve(
        self, id: int = None, **kwargs
    ) -> DockingEventEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/docking_events/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return DockingEventEndpointDetailed(**response)

    async def docking_events_retrieve_async(
        self, id: int = None, **kwargs
    ) -> DockingEventEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/docking_events/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return DockingEventEndpointDetailed(**response)

    def events_list(
        self,
        agency__ids: List[int] = None,
        date__gt: str = None,
        date__gt__lt: str = None,
        date__gte: str = None,
        date__lte: str = None,
        day: List[float] = None,
        id: List[int] = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        limit: int = None,
        month: List[float] = None,
        offset: int = None,
        ordering: str = None,
        program: List[int] = None,
        search: str = None,
        slug: str = None,
        type: int = None,
        type__ids: List[int] = None,
        video_url: List[str] = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicEventsEndpointList:
        params = {
            "agency__ids": agency__ids,
            "date__gt": date__gt,
            "date__gt__lt": date__gt__lt,
            "date__gte": date__gte,
            "date__lte": date__lte,
            "day": day,
            "id": id,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "limit": limit,
            "month": month,
            "offset": offset,
            "ordering": ordering,
            "program": program,
            "search": search,
            "slug": slug,
            "type": type,
            "type__ids": type__ids,
            "video_url": video_url,
            "year": year,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/events/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicEventsEndpointList(**response)

    async def events_list_async(
        self,
        agency__ids: List[int] = None,
        date__gt: str = None,
        date__gt__lt: str = None,
        date__gte: str = None,
        date__lte: str = None,
        day: List[float] = None,
        id: List[int] = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        limit: int = None,
        month: List[float] = None,
        offset: int = None,
        ordering: str = None,
        program: List[int] = None,
        search: str = None,
        slug: str = None,
        type: int = None,
        type__ids: List[int] = None,
        video_url: List[str] = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicEventsEndpointList:
        params = {
            "agency__ids": agency__ids,
            "date__gt": date__gt,
            "date__gt__lt": date__gt__lt,
            "date__gte": date__gte,
            "date__lte": date__lte,
            "day": day,
            "id": id,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "limit": limit,
            "month": month,
            "offset": offset,
            "ordering": ordering,
            "program": program,
            "search": search,
            "slug": slug,
            "type": type,
            "type__ids": type__ids,
            "video_url": video_url,
            "year": year,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/events/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicEventsEndpointList(**response)

    def events_retrieve(self, id: int = None, **kwargs) -> EventEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/events/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return EventEndpointDetailed(**response)

    async def events_retrieve_async(
        self, id: int = None, **kwargs
    ) -> EventEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/events/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return EventEndpointDetailed(**response)

    def events_previous_list(
        self,
        agency__ids: List[int] = None,
        date__gt: str = None,
        date__gt__lt: str = None,
        date__gte: str = None,
        date__lte: str = None,
        day: List[float] = None,
        id: List[int] = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        limit: int = None,
        month: List[float] = None,
        offset: int = None,
        ordering: str = None,
        program: List[int] = None,
        search: str = None,
        slug: str = None,
        type: int = None,
        type__ids: List[int] = None,
        video_url: List[str] = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicEventsEndpointList:
        params = {
            "agency__ids": agency__ids,
            "date__gt": date__gt,
            "date__gt__lt": date__gt__lt,
            "date__gte": date__gte,
            "date__lte": date__lte,
            "day": day,
            "id": id,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "limit": limit,
            "month": month,
            "offset": offset,
            "ordering": ordering,
            "program": program,
            "search": search,
            "slug": slug,
            "type": type,
            "type__ids": type__ids,
            "video_url": video_url,
            "year": year,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/events/previous/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicEventsEndpointList(**response)

    async def events_previous_list_async(
        self,
        agency__ids: List[int] = None,
        date__gt: str = None,
        date__gt__lt: str = None,
        date__gte: str = None,
        date__lte: str = None,
        day: List[float] = None,
        id: List[int] = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        limit: int = None,
        month: List[float] = None,
        offset: int = None,
        ordering: str = None,
        program: List[int] = None,
        search: str = None,
        slug: str = None,
        type: int = None,
        type__ids: List[int] = None,
        video_url: List[str] = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicEventsEndpointList:
        params = {
            "agency__ids": agency__ids,
            "date__gt": date__gt,
            "date__gt__lt": date__gt__lt,
            "date__gte": date__gte,
            "date__lte": date__lte,
            "day": day,
            "id": id,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "limit": limit,
            "month": month,
            "offset": offset,
            "ordering": ordering,
            "program": program,
            "search": search,
            "slug": slug,
            "type": type,
            "type__ids": type__ids,
            "video_url": video_url,
            "year": year,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/events/previous/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicEventsEndpointList(**response)

    def events_previous_retrieve(
        self, id: int = None, **kwargs
    ) -> EventEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/events/previous/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return EventEndpointDetailed(**response)

    async def events_previous_retrieve_async(
        self, id: int = None, **kwargs
    ) -> EventEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/events/previous/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return EventEndpointDetailed(**response)

    def events_upcoming_list(
        self,
        agency__ids: List[int] = None,
        date__gt: str = None,
        date__gt__lt: str = None,
        date__gte: str = None,
        date__lte: str = None,
        day: List[float] = None,
        hide_recent_previous: bool = None,
        id: List[int] = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        limit: int = None,
        month: List[float] = None,
        offset: int = None,
        ordering: str = None,
        program: List[int] = None,
        search: str = None,
        slug: str = None,
        type: int = None,
        type__ids: List[int] = None,
        video_url: List[str] = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicEventsEndpointList:
        params = {
            "agency__ids": agency__ids,
            "date__gt": date__gt,
            "date__gt__lt": date__gt__lt,
            "date__gte": date__gte,
            "date__lte": date__lte,
            "day": day,
            "hide_recent_previous": hide_recent_previous,
            "id": id,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "limit": limit,
            "month": month,
            "offset": offset,
            "ordering": ordering,
            "program": program,
            "search": search,
            "slug": slug,
            "type": type,
            "type__ids": type__ids,
            "video_url": video_url,
            "year": year,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/events/upcoming/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicEventsEndpointList(**response)

    async def events_upcoming_list_async(
        self,
        agency__ids: List[int] = None,
        date__gt: str = None,
        date__gt__lt: str = None,
        date__gte: str = None,
        date__lte: str = None,
        day: List[float] = None,
        hide_recent_previous: bool = None,
        id: List[int] = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        limit: int = None,
        month: List[float] = None,
        offset: int = None,
        ordering: str = None,
        program: List[int] = None,
        search: str = None,
        slug: str = None,
        type: int = None,
        type__ids: List[int] = None,
        video_url: List[str] = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicEventsEndpointList:
        params = {
            "agency__ids": agency__ids,
            "date__gt": date__gt,
            "date__gt__lt": date__gt__lt,
            "date__gte": date__gte,
            "date__lte": date__lte,
            "day": day,
            "hide_recent_previous": hide_recent_previous,
            "id": id,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "limit": limit,
            "month": month,
            "offset": offset,
            "ordering": ordering,
            "program": program,
            "search": search,
            "slug": slug,
            "type": type,
            "type__ids": type__ids,
            "video_url": video_url,
            "year": year,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/events/upcoming/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicEventsEndpointList(**response)

    def events_upcoming_retrieve(
        self, id: int = None, **kwargs
    ) -> EventEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/events/upcoming/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return EventEndpointDetailed(**response)

    async def events_upcoming_retrieve_async(
        self, id: int = None, **kwargs
    ) -> EventEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/events/upcoming/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return EventEndpointDetailed(**response)

    def expeditions_list(
        self,
        crew__astronaut: int = None,
        crew__astronaut__agency: int = None,
        end__gt: str = None,
        end__gte: str = None,
        end__lt: str = None,
        end__lte: str = None,
        limit: int = None,
        name: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        space_station: int = None,
        start__gt: str = None,
        start__gte: str = None,
        start__lt: str = None,
        start__lte: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicExpeditionEndpointList:
        params = {
            "crew__astronaut": crew__astronaut,
            "crew__astronaut__agency": crew__astronaut__agency,
            "end__gt": end__gt,
            "end__gte": end__gte,
            "end__lt": end__lt,
            "end__lte": end__lte,
            "limit": limit,
            "name": name,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "space_station": space_station,
            "start__gt": start__gt,
            "start__gte": start__gte,
            "start__lt": start__lt,
            "start__lte": start__lte,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/expeditions/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicExpeditionEndpointList(**response)

    async def expeditions_list_async(
        self,
        crew__astronaut: int = None,
        crew__astronaut__agency: int = None,
        end__gt: str = None,
        end__gte: str = None,
        end__lt: str = None,
        end__lte: str = None,
        limit: int = None,
        name: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        space_station: int = None,
        start__gt: str = None,
        start__gte: str = None,
        start__lt: str = None,
        start__lte: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicExpeditionEndpointList:
        params = {
            "crew__astronaut": crew__astronaut,
            "crew__astronaut__agency": crew__astronaut__agency,
            "end__gt": end__gt,
            "end__gte": end__gte,
            "end__lt": end__lt,
            "end__lte": end__lte,
            "limit": limit,
            "name": name,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "space_station": space_station,
            "start__gt": start__gt,
            "start__gte": start__gte,
            "start__lt": start__lt,
            "start__lte": start__lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/expeditions/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicExpeditionEndpointList(**response)

    def expeditions_retrieve(self, id: int = None, **kwargs) -> ExpeditionDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/expeditions/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ExpeditionDetailed(**response)

    async def expeditions_retrieve_async(
        self, id: int = None, **kwargs
    ) -> ExpeditionDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/expeditions/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ExpeditionDetailed(**response)

    def landings_list(
        self,
        attempt: bool = None,
        firststage_launch__ids: List[str] = None,
        landing_location__ids: List[int] = None,
        landing_type__ids: List[int] = None,
        launcher__ids: List[int] = None,
        launcher_config__ids: List[int] = None,
        launcher_serial_numbers: List[str] = None,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        spacecraft__ids: List[int] = None,
        spacecraft_config__ids: List[int] = None,
        spacecraft_launch__ids: List[str] = None,
        success: bool = None,
        **kwargs,
    ) -> PaginatedPolymorphicLandingEndpointList:
        params = {
            "attempt": attempt,
            "firststage_launch__ids": firststage_launch__ids,
            "landing_location__ids": landing_location__ids,
            "landing_type__ids": landing_type__ids,
            "launcher__ids": launcher__ids,
            "launcher_config__ids": launcher_config__ids,
            "launcher_serial_numbers": launcher_serial_numbers,
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "spacecraft__ids": spacecraft__ids,
            "spacecraft_config__ids": spacecraft_config__ids,
            "spacecraft_launch__ids": spacecraft_launch__ids,
            "success": success,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/landings/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLandingEndpointList(**response)

    async def landings_list_async(
        self,
        attempt: bool = None,
        firststage_launch__ids: List[str] = None,
        landing_location__ids: List[int] = None,
        landing_type__ids: List[int] = None,
        launcher__ids: List[int] = None,
        launcher_config__ids: List[int] = None,
        launcher_serial_numbers: List[str] = None,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        spacecraft__ids: List[int] = None,
        spacecraft_config__ids: List[int] = None,
        spacecraft_launch__ids: List[str] = None,
        success: bool = None,
        **kwargs,
    ) -> PaginatedPolymorphicLandingEndpointList:
        params = {
            "attempt": attempt,
            "firststage_launch__ids": firststage_launch__ids,
            "landing_location__ids": landing_location__ids,
            "landing_type__ids": landing_type__ids,
            "launcher__ids": launcher__ids,
            "launcher_config__ids": launcher_config__ids,
            "launcher_serial_numbers": launcher_serial_numbers,
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "spacecraft__ids": spacecraft__ids,
            "spacecraft_config__ids": spacecraft_config__ids,
            "spacecraft_launch__ids": spacecraft_launch__ids,
            "success": success,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/landings/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLandingEndpointList(**response)

    def landings_retrieve(self, id: int = None, **kwargs) -> LandingEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/landings/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LandingEndpointDetailed(**response)

    async def landings_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LandingEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/landings/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LandingEndpointDetailed(**response)

    def launcher_configuration_families_list(
        self,
        attempted_landings: int = None,
        attempted_landings__gt: int = None,
        attempted_landings__gte: int = None,
        attempted_landings__lt: int = None,
        attempted_landings__lte: int = None,
        consecutive_successful_landings: int = None,
        consecutive_successful_landings__gt: int = None,
        consecutive_successful_landings__gte: int = None,
        consecutive_successful_landings__lt: int = None,
        consecutive_successful_landings__lte: int = None,
        consecutive_successful_launches: int = None,
        consecutive_successful_launches__gt: int = None,
        consecutive_successful_launches__gte: int = None,
        consecutive_successful_launches__lt: int = None,
        consecutive_successful_launches__lte: int = None,
        failed_landings: int = None,
        failed_landings__gt: int = None,
        failed_landings__gte: int = None,
        failed_landings__lt: int = None,
        failed_landings__lte: int = None,
        failed_launches: int = None,
        failed_launches__gt: int = None,
        failed_launches__gte: int = None,
        failed_launches__lt: int = None,
        failed_launches__lte: int = None,
        limit: int = None,
        maiden_flight: str = None,
        maiden_flight__gt: str = None,
        maiden_flight__gte: str = None,
        maiden_flight__lt: str = None,
        maiden_flight__lte: str = None,
        manufacturer__abbrev: str = None,
        manufacturer__abbrev__contains: str = None,
        manufacturer__country_code: str = None,
        manufacturer__id: int = None,
        manufacturer__id__contains: int = None,
        manufacturer__name: str = None,
        manufacturer__name__contains: str = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        pending_launches: int = None,
        pending_launches__gt: int = None,
        pending_launches__gte: int = None,
        pending_launches__lt: int = None,
        pending_launches__lte: int = None,
        search: str = None,
        successful_landings: int = None,
        successful_landings__gt: int = None,
        successful_landings__gte: int = None,
        successful_landings__lt: int = None,
        successful_landings__lte: int = None,
        successful_launches: int = None,
        successful_launches__gt: int = None,
        successful_launches__gte: int = None,
        successful_launches__lt: int = None,
        successful_launches__lte: int = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicLauncherConfigFamilyEndpointList:
        params = {
            "attempted_landings": attempted_landings,
            "attempted_landings__gt": attempted_landings__gt,
            "attempted_landings__gte": attempted_landings__gte,
            "attempted_landings__lt": attempted_landings__lt,
            "attempted_landings__lte": attempted_landings__lte,
            "consecutive_successful_landings": consecutive_successful_landings,
            "consecutive_successful_landings__gt": consecutive_successful_landings__gt,
            "consecutive_successful_landings__gte": consecutive_successful_landings__gte,
            "consecutive_successful_landings__lt": consecutive_successful_landings__lt,
            "consecutive_successful_landings__lte": consecutive_successful_landings__lte,
            "consecutive_successful_launches": consecutive_successful_launches,
            "consecutive_successful_launches__gt": consecutive_successful_launches__gt,
            "consecutive_successful_launches__gte": consecutive_successful_launches__gte,
            "consecutive_successful_launches__lt": consecutive_successful_launches__lt,
            "consecutive_successful_launches__lte": consecutive_successful_launches__lte,
            "failed_landings": failed_landings,
            "failed_landings__gt": failed_landings__gt,
            "failed_landings__gte": failed_landings__gte,
            "failed_landings__lt": failed_landings__lt,
            "failed_landings__lte": failed_landings__lte,
            "failed_launches": failed_launches,
            "failed_launches__gt": failed_launches__gt,
            "failed_launches__gte": failed_launches__gte,
            "failed_launches__lt": failed_launches__lt,
            "failed_launches__lte": failed_launches__lte,
            "limit": limit,
            "maiden_flight": maiden_flight,
            "maiden_flight__gt": maiden_flight__gt,
            "maiden_flight__gte": maiden_flight__gte,
            "maiden_flight__lt": maiden_flight__lt,
            "maiden_flight__lte": maiden_flight__lte,
            "manufacturer__abbrev": manufacturer__abbrev,
            "manufacturer__abbrev__contains": manufacturer__abbrev__contains,
            "manufacturer__country_code": manufacturer__country_code,
            "manufacturer__id": manufacturer__id,
            "manufacturer__id__contains": manufacturer__id__contains,
            "manufacturer__name": manufacturer__name,
            "manufacturer__name__contains": manufacturer__name__contains,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "pending_launches": pending_launches,
            "pending_launches__gt": pending_launches__gt,
            "pending_launches__gte": pending_launches__gte,
            "pending_launches__lt": pending_launches__lt,
            "pending_launches__lte": pending_launches__lte,
            "search": search,
            "successful_landings": successful_landings,
            "successful_landings__gt": successful_landings__gt,
            "successful_landings__gte": successful_landings__gte,
            "successful_landings__lt": successful_landings__lt,
            "successful_landings__lte": successful_landings__lte,
            "successful_launches": successful_launches,
            "successful_launches__gt": successful_launches__gt,
            "successful_launches__gte": successful_launches__gte,
            "successful_launches__lt": successful_launches__lt,
            "successful_launches__lte": successful_launches__lte,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/launcher_configuration_families/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLauncherConfigFamilyEndpointList(**response)

    async def launcher_configuration_families_list_async(
        self,
        attempted_landings: int = None,
        attempted_landings__gt: int = None,
        attempted_landings__gte: int = None,
        attempted_landings__lt: int = None,
        attempted_landings__lte: int = None,
        consecutive_successful_landings: int = None,
        consecutive_successful_landings__gt: int = None,
        consecutive_successful_landings__gte: int = None,
        consecutive_successful_landings__lt: int = None,
        consecutive_successful_landings__lte: int = None,
        consecutive_successful_launches: int = None,
        consecutive_successful_launches__gt: int = None,
        consecutive_successful_launches__gte: int = None,
        consecutive_successful_launches__lt: int = None,
        consecutive_successful_launches__lte: int = None,
        failed_landings: int = None,
        failed_landings__gt: int = None,
        failed_landings__gte: int = None,
        failed_landings__lt: int = None,
        failed_landings__lte: int = None,
        failed_launches: int = None,
        failed_launches__gt: int = None,
        failed_launches__gte: int = None,
        failed_launches__lt: int = None,
        failed_launches__lte: int = None,
        limit: int = None,
        maiden_flight: str = None,
        maiden_flight__gt: str = None,
        maiden_flight__gte: str = None,
        maiden_flight__lt: str = None,
        maiden_flight__lte: str = None,
        manufacturer__abbrev: str = None,
        manufacturer__abbrev__contains: str = None,
        manufacturer__country_code: str = None,
        manufacturer__id: int = None,
        manufacturer__id__contains: int = None,
        manufacturer__name: str = None,
        manufacturer__name__contains: str = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        pending_launches: int = None,
        pending_launches__gt: int = None,
        pending_launches__gte: int = None,
        pending_launches__lt: int = None,
        pending_launches__lte: int = None,
        search: str = None,
        successful_landings: int = None,
        successful_landings__gt: int = None,
        successful_landings__gte: int = None,
        successful_landings__lt: int = None,
        successful_landings__lte: int = None,
        successful_launches: int = None,
        successful_launches__gt: int = None,
        successful_launches__gte: int = None,
        successful_launches__lt: int = None,
        successful_launches__lte: int = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicLauncherConfigFamilyEndpointList:
        params = {
            "attempted_landings": attempted_landings,
            "attempted_landings__gt": attempted_landings__gt,
            "attempted_landings__gte": attempted_landings__gte,
            "attempted_landings__lt": attempted_landings__lt,
            "attempted_landings__lte": attempted_landings__lte,
            "consecutive_successful_landings": consecutive_successful_landings,
            "consecutive_successful_landings__gt": consecutive_successful_landings__gt,
            "consecutive_successful_landings__gte": consecutive_successful_landings__gte,
            "consecutive_successful_landings__lt": consecutive_successful_landings__lt,
            "consecutive_successful_landings__lte": consecutive_successful_landings__lte,
            "consecutive_successful_launches": consecutive_successful_launches,
            "consecutive_successful_launches__gt": consecutive_successful_launches__gt,
            "consecutive_successful_launches__gte": consecutive_successful_launches__gte,
            "consecutive_successful_launches__lt": consecutive_successful_launches__lt,
            "consecutive_successful_launches__lte": consecutive_successful_launches__lte,
            "failed_landings": failed_landings,
            "failed_landings__gt": failed_landings__gt,
            "failed_landings__gte": failed_landings__gte,
            "failed_landings__lt": failed_landings__lt,
            "failed_landings__lte": failed_landings__lte,
            "failed_launches": failed_launches,
            "failed_launches__gt": failed_launches__gt,
            "failed_launches__gte": failed_launches__gte,
            "failed_launches__lt": failed_launches__lt,
            "failed_launches__lte": failed_launches__lte,
            "limit": limit,
            "maiden_flight": maiden_flight,
            "maiden_flight__gt": maiden_flight__gt,
            "maiden_flight__gte": maiden_flight__gte,
            "maiden_flight__lt": maiden_flight__lt,
            "maiden_flight__lte": maiden_flight__lte,
            "manufacturer__abbrev": manufacturer__abbrev,
            "manufacturer__abbrev__contains": manufacturer__abbrev__contains,
            "manufacturer__country_code": manufacturer__country_code,
            "manufacturer__id": manufacturer__id,
            "manufacturer__id__contains": manufacturer__id__contains,
            "manufacturer__name": manufacturer__name,
            "manufacturer__name__contains": manufacturer__name__contains,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "pending_launches": pending_launches,
            "pending_launches__gt": pending_launches__gt,
            "pending_launches__gte": pending_launches__gte,
            "pending_launches__lt": pending_launches__lt,
            "pending_launches__lte": pending_launches__lte,
            "search": search,
            "successful_landings": successful_landings,
            "successful_landings__gt": successful_landings__gt,
            "successful_landings__gte": successful_landings__gte,
            "successful_landings__lt": successful_landings__lt,
            "successful_landings__lte": successful_landings__lte,
            "successful_launches": successful_launches,
            "successful_launches__gt": successful_launches__gt,
            "successful_launches__gte": successful_launches__gte,
            "successful_launches__lt": successful_launches__lt,
            "successful_launches__lte": successful_launches__lte,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/launcher_configuration_families/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLauncherConfigFamilyEndpointList(**response)

    def launcher_configuration_families_retrieve(
        self, id: int = None, **kwargs
    ) -> LauncherConfigFamilyDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/launcher_configuration_families/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LauncherConfigFamilyDetailed(**response)

    async def launcher_configuration_families_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LauncherConfigFamilyDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/launcher_configuration_families/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LauncherConfigFamilyDetailed(**response)

    def launcher_configurations_list(
        self,
        active: bool = None,
        attempted_landings: int = None,
        attempted_landings__gt: int = None,
        attempted_landings__gte: int = None,
        attempted_landings__lt: int = None,
        attempted_landings__lte: int = None,
        consecutive_successful_landings: int = None,
        consecutive_successful_landings__gt: int = None,
        consecutive_successful_landings__gte: int = None,
        consecutive_successful_landings__lt: int = None,
        consecutive_successful_landings__lte: int = None,
        consecutive_successful_launches: int = None,
        consecutive_successful_launches__gt: int = None,
        consecutive_successful_launches__gte: int = None,
        consecutive_successful_launches__lt: int = None,
        consecutive_successful_launches__lte: int = None,
        failed_landings: int = None,
        failed_landings__gt: int = None,
        failed_landings__gte: int = None,
        failed_landings__lt: int = None,
        failed_landings__lte: int = None,
        failed_launches: int = None,
        failed_launches__gt: int = None,
        failed_launches__gte: int = None,
        failed_launches__lt: int = None,
        failed_launches__lte: int = None,
        families: List[int] = None,
        families__contains: List[int] = None,
        full_name: str = None,
        full_name__contains: str = None,
        is_placeholder: bool = None,
        limit: int = None,
        maiden_flight: str = None,
        maiden_flight__gt: str = None,
        maiden_flight__gte: str = None,
        maiden_flight__lt: str = None,
        maiden_flight__lte: str = None,
        manufacturer__name: str = None,
        manufacturer__name__contains: str = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        pending_launches: int = None,
        pending_launches__gt: int = None,
        pending_launches__gte: int = None,
        pending_launches__lt: int = None,
        pending_launches__lte: int = None,
        program: List[int] = None,
        program__contains: List[int] = None,
        search: str = None,
        successful_landings: int = None,
        successful_landings__gt: int = None,
        successful_landings__gte: int = None,
        successful_landings__lt: int = None,
        successful_landings__lte: int = None,
        successful_launches: int = None,
        successful_launches__gt: int = None,
        successful_launches__gte: int = None,
        successful_launches__lt: int = None,
        successful_launches__lte: int = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicLauncherConfigEndpointList:
        params = {
            "active": active,
            "attempted_landings": attempted_landings,
            "attempted_landings__gt": attempted_landings__gt,
            "attempted_landings__gte": attempted_landings__gte,
            "attempted_landings__lt": attempted_landings__lt,
            "attempted_landings__lte": attempted_landings__lte,
            "consecutive_successful_landings": consecutive_successful_landings,
            "consecutive_successful_landings__gt": consecutive_successful_landings__gt,
            "consecutive_successful_landings__gte": consecutive_successful_landings__gte,
            "consecutive_successful_landings__lt": consecutive_successful_landings__lt,
            "consecutive_successful_landings__lte": consecutive_successful_landings__lte,
            "consecutive_successful_launches": consecutive_successful_launches,
            "consecutive_successful_launches__gt": consecutive_successful_launches__gt,
            "consecutive_successful_launches__gte": consecutive_successful_launches__gte,
            "consecutive_successful_launches__lt": consecutive_successful_launches__lt,
            "consecutive_successful_launches__lte": consecutive_successful_launches__lte,
            "failed_landings": failed_landings,
            "failed_landings__gt": failed_landings__gt,
            "failed_landings__gte": failed_landings__gte,
            "failed_landings__lt": failed_landings__lt,
            "failed_landings__lte": failed_landings__lte,
            "failed_launches": failed_launches,
            "failed_launches__gt": failed_launches__gt,
            "failed_launches__gte": failed_launches__gte,
            "failed_launches__lt": failed_launches__lt,
            "failed_launches__lte": failed_launches__lte,
            "families": families,
            "families__contains": families__contains,
            "full_name": full_name,
            "full_name__contains": full_name__contains,
            "is_placeholder": is_placeholder,
            "limit": limit,
            "maiden_flight": maiden_flight,
            "maiden_flight__gt": maiden_flight__gt,
            "maiden_flight__gte": maiden_flight__gte,
            "maiden_flight__lt": maiden_flight__lt,
            "maiden_flight__lte": maiden_flight__lte,
            "manufacturer__name": manufacturer__name,
            "manufacturer__name__contains": manufacturer__name__contains,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "pending_launches": pending_launches,
            "pending_launches__gt": pending_launches__gt,
            "pending_launches__gte": pending_launches__gte,
            "pending_launches__lt": pending_launches__lt,
            "pending_launches__lte": pending_launches__lte,
            "program": program,
            "program__contains": program__contains,
            "search": search,
            "successful_landings": successful_landings,
            "successful_landings__gt": successful_landings__gt,
            "successful_landings__gte": successful_landings__gte,
            "successful_landings__lt": successful_landings__lt,
            "successful_landings__lte": successful_landings__lte,
            "successful_launches": successful_launches,
            "successful_launches__gt": successful_launches__gt,
            "successful_launches__gte": successful_launches__gte,
            "successful_launches__lt": successful_launches__lt,
            "successful_launches__lte": successful_launches__lte,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/launcher_configurations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLauncherConfigEndpointList(**response)

    async def launcher_configurations_list_async(
        self,
        active: bool = None,
        attempted_landings: int = None,
        attempted_landings__gt: int = None,
        attempted_landings__gte: int = None,
        attempted_landings__lt: int = None,
        attempted_landings__lte: int = None,
        consecutive_successful_landings: int = None,
        consecutive_successful_landings__gt: int = None,
        consecutive_successful_landings__gte: int = None,
        consecutive_successful_landings__lt: int = None,
        consecutive_successful_landings__lte: int = None,
        consecutive_successful_launches: int = None,
        consecutive_successful_launches__gt: int = None,
        consecutive_successful_launches__gte: int = None,
        consecutive_successful_launches__lt: int = None,
        consecutive_successful_launches__lte: int = None,
        failed_landings: int = None,
        failed_landings__gt: int = None,
        failed_landings__gte: int = None,
        failed_landings__lt: int = None,
        failed_landings__lte: int = None,
        failed_launches: int = None,
        failed_launches__gt: int = None,
        failed_launches__gte: int = None,
        failed_launches__lt: int = None,
        failed_launches__lte: int = None,
        families: List[int] = None,
        families__contains: List[int] = None,
        full_name: str = None,
        full_name__contains: str = None,
        is_placeholder: bool = None,
        limit: int = None,
        maiden_flight: str = None,
        maiden_flight__gt: str = None,
        maiden_flight__gte: str = None,
        maiden_flight__lt: str = None,
        maiden_flight__lte: str = None,
        manufacturer__name: str = None,
        manufacturer__name__contains: str = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        pending_launches: int = None,
        pending_launches__gt: int = None,
        pending_launches__gte: int = None,
        pending_launches__lt: int = None,
        pending_launches__lte: int = None,
        program: List[int] = None,
        program__contains: List[int] = None,
        search: str = None,
        successful_landings: int = None,
        successful_landings__gt: int = None,
        successful_landings__gte: int = None,
        successful_landings__lt: int = None,
        successful_landings__lte: int = None,
        successful_launches: int = None,
        successful_launches__gt: int = None,
        successful_launches__gte: int = None,
        successful_launches__lt: int = None,
        successful_launches__lte: int = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicLauncherConfigEndpointList:
        params = {
            "active": active,
            "attempted_landings": attempted_landings,
            "attempted_landings__gt": attempted_landings__gt,
            "attempted_landings__gte": attempted_landings__gte,
            "attempted_landings__lt": attempted_landings__lt,
            "attempted_landings__lte": attempted_landings__lte,
            "consecutive_successful_landings": consecutive_successful_landings,
            "consecutive_successful_landings__gt": consecutive_successful_landings__gt,
            "consecutive_successful_landings__gte": consecutive_successful_landings__gte,
            "consecutive_successful_landings__lt": consecutive_successful_landings__lt,
            "consecutive_successful_landings__lte": consecutive_successful_landings__lte,
            "consecutive_successful_launches": consecutive_successful_launches,
            "consecutive_successful_launches__gt": consecutive_successful_launches__gt,
            "consecutive_successful_launches__gte": consecutive_successful_launches__gte,
            "consecutive_successful_launches__lt": consecutive_successful_launches__lt,
            "consecutive_successful_launches__lte": consecutive_successful_launches__lte,
            "failed_landings": failed_landings,
            "failed_landings__gt": failed_landings__gt,
            "failed_landings__gte": failed_landings__gte,
            "failed_landings__lt": failed_landings__lt,
            "failed_landings__lte": failed_landings__lte,
            "failed_launches": failed_launches,
            "failed_launches__gt": failed_launches__gt,
            "failed_launches__gte": failed_launches__gte,
            "failed_launches__lt": failed_launches__lt,
            "failed_launches__lte": failed_launches__lte,
            "families": families,
            "families__contains": families__contains,
            "full_name": full_name,
            "full_name__contains": full_name__contains,
            "is_placeholder": is_placeholder,
            "limit": limit,
            "maiden_flight": maiden_flight,
            "maiden_flight__gt": maiden_flight__gt,
            "maiden_flight__gte": maiden_flight__gte,
            "maiden_flight__lt": maiden_flight__lt,
            "maiden_flight__lte": maiden_flight__lte,
            "manufacturer__name": manufacturer__name,
            "manufacturer__name__contains": manufacturer__name__contains,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "pending_launches": pending_launches,
            "pending_launches__gt": pending_launches__gt,
            "pending_launches__gte": pending_launches__gte,
            "pending_launches__lt": pending_launches__lt,
            "pending_launches__lte": pending_launches__lte,
            "program": program,
            "program__contains": program__contains,
            "search": search,
            "successful_landings": successful_landings,
            "successful_landings__gt": successful_landings__gt,
            "successful_landings__gte": successful_landings__gte,
            "successful_landings__lt": successful_landings__lt,
            "successful_landings__lte": successful_landings__lte,
            "successful_launches": successful_launches,
            "successful_launches__gt": successful_launches__gt,
            "successful_launches__gte": successful_launches__gte,
            "successful_launches__lt": successful_launches__lt,
            "successful_launches__lte": successful_launches__lte,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/launcher_configurations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLauncherConfigEndpointList(**response)

    def launcher_configurations_retrieve(
        self, id: int = None, **kwargs
    ) -> LauncherConfigDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/launcher_configurations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LauncherConfigDetailed(**response)

    async def launcher_configurations_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LauncherConfigDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/launcher_configurations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LauncherConfigDetailed(**response)

    def launchers_list(
        self,
        attempted_landings: int = None,
        attempted_landings__gt: int = None,
        attempted_landings__gte: int = None,
        attempted_landings__lt: int = None,
        attempted_landings__lte: int = None,
        first_launch_date: str = None,
        flight_proven: bool = None,
        flights: int = None,
        flights__gt: int = None,
        flights__gte: int = None,
        flights__lt: int = None,
        flights__lte: int = None,
        id: int = None,
        id__contains: int = None,
        is_placeholder: bool = None,
        last_launch_date: str = None,
        launcher_config__ids: List[int] = None,
        launcher_config__manufacturer__name: str = None,
        launcher_config__manufacturer__name__contains: str = None,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        serial_number: str = None,
        serial_number__contains: str = None,
        status: int = None,
        successful_landings: int = None,
        successful_landings__gt: int = None,
        successful_landings__gte: int = None,
        successful_landings__lt: int = None,
        successful_landings__lte: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicLauncherEndpointList:
        params = {
            "attempted_landings": attempted_landings,
            "attempted_landings__gt": attempted_landings__gt,
            "attempted_landings__gte": attempted_landings__gte,
            "attempted_landings__lt": attempted_landings__lt,
            "attempted_landings__lte": attempted_landings__lte,
            "first_launch_date": first_launch_date,
            "flight_proven": flight_proven,
            "flights": flights,
            "flights__gt": flights__gt,
            "flights__gte": flights__gte,
            "flights__lt": flights__lt,
            "flights__lte": flights__lte,
            "id": id,
            "id__contains": id__contains,
            "is_placeholder": is_placeholder,
            "last_launch_date": last_launch_date,
            "launcher_config__ids": launcher_config__ids,
            "launcher_config__manufacturer__name": launcher_config__manufacturer__name,
            "launcher_config__manufacturer__name__contains": launcher_config__manufacturer__name__contains,
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "serial_number": serial_number,
            "serial_number__contains": serial_number__contains,
            "status": status,
            "successful_landings": successful_landings,
            "successful_landings__gt": successful_landings__gt,
            "successful_landings__gte": successful_landings__gte,
            "successful_landings__lt": successful_landings__lt,
            "successful_landings__lte": successful_landings__lte,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/launchers/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLauncherEndpointList(**response)

    async def launchers_list_async(
        self,
        attempted_landings: int = None,
        attempted_landings__gt: int = None,
        attempted_landings__gte: int = None,
        attempted_landings__lt: int = None,
        attempted_landings__lte: int = None,
        first_launch_date: str = None,
        flight_proven: bool = None,
        flights: int = None,
        flights__gt: int = None,
        flights__gte: int = None,
        flights__lt: int = None,
        flights__lte: int = None,
        id: int = None,
        id__contains: int = None,
        is_placeholder: bool = None,
        last_launch_date: str = None,
        launcher_config__ids: List[int] = None,
        launcher_config__manufacturer__name: str = None,
        launcher_config__manufacturer__name__contains: str = None,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        serial_number: str = None,
        serial_number__contains: str = None,
        status: int = None,
        successful_landings: int = None,
        successful_landings__gt: int = None,
        successful_landings__gte: int = None,
        successful_landings__lt: int = None,
        successful_landings__lte: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicLauncherEndpointList:
        params = {
            "attempted_landings": attempted_landings,
            "attempted_landings__gt": attempted_landings__gt,
            "attempted_landings__gte": attempted_landings__gte,
            "attempted_landings__lt": attempted_landings__lt,
            "attempted_landings__lte": attempted_landings__lte,
            "first_launch_date": first_launch_date,
            "flight_proven": flight_proven,
            "flights": flights,
            "flights__gt": flights__gt,
            "flights__gte": flights__gte,
            "flights__lt": flights__lt,
            "flights__lte": flights__lte,
            "id": id,
            "id__contains": id__contains,
            "is_placeholder": is_placeholder,
            "last_launch_date": last_launch_date,
            "launcher_config__ids": launcher_config__ids,
            "launcher_config__manufacturer__name": launcher_config__manufacturer__name,
            "launcher_config__manufacturer__name__contains": launcher_config__manufacturer__name__contains,
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "serial_number": serial_number,
            "serial_number__contains": serial_number__contains,
            "status": status,
            "successful_landings": successful_landings,
            "successful_landings__gt": successful_landings__gt,
            "successful_landings__gte": successful_landings__gte,
            "successful_landings__lt": successful_landings__lt,
            "successful_landings__lte": successful_landings__lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/launchers/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLauncherEndpointList(**response)

    def launchers_retrieve(self, id: int = None, **kwargs) -> LauncherDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/launchers/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LauncherDetailed(**response)

    async def launchers_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LauncherDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/launchers/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LauncherDetailed(**response)

    def launches_list(
        self,
        agency_launch_attempt_count: int = None,
        agency_launch_attempt_count__gt: int = None,
        agency_launch_attempt_count__gte: int = None,
        agency_launch_attempt_count__lt: int = None,
        agency_launch_attempt_count__lte: int = None,
        agency_launch_attempt_count_year: int = None,
        agency_launch_attempt_count_year__gt: int = None,
        agency_launch_attempt_count_year__gte: int = None,
        agency_launch_attempt_count_year__lt: int = None,
        agency_launch_attempt_count_year__lte: int = None,
        day: List[float] = None,
        id: List[str] = None,
        include_suborbital: bool = None,
        is_crewed: bool = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        launch_designator: List[str] = None,
        launcher_config__id: List[int] = None,
        limit: int = None,
        location__ids: List[int] = None,
        location_launch_attempt_count: int = None,
        location_launch_attempt_count__gt: int = None,
        location_launch_attempt_count__gte: int = None,
        location_launch_attempt_count__lt: int = None,
        location_launch_attempt_count__lte: int = None,
        location_launch_attempt_count_year: int = None,
        location_launch_attempt_count_year__gt: int = None,
        location_launch_attempt_count_year__gte: int = None,
        location_launch_attempt_count_year__lt: int = None,
        location_launch_attempt_count_year__lte: int = None,
        lsp__id: List[int] = None,
        lsp__name: List[str] = None,
        mission__orbit__celestial_body__id: int = None,
        mission__orbit__name: str = None,
        mission__orbit__name__icontains: str = None,
        month: List[float] = None,
        name: str = None,
        net__gt: str = None,
        net__gte: str = None,
        net__lt: str = None,
        net__lte: str = None,
        offset: int = None,
        orbital_launch_attempt_count: int = None,
        orbital_launch_attempt_count__gt: int = None,
        orbital_launch_attempt_count__gte: int = None,
        orbital_launch_attempt_count__lt: int = None,
        orbital_launch_attempt_count__lte: int = None,
        orbital_launch_attempt_count_year: int = None,
        orbital_launch_attempt_count_year__gt: int = None,
        orbital_launch_attempt_count_year__gte: int = None,
        orbital_launch_attempt_count_year__lt: int = None,
        orbital_launch_attempt_count_year__lte: int = None,
        ordering: str = None,
        pad: int = None,
        pad__location: int = None,
        pad__location__celestial_body__id: int = None,
        pad_launch_attempt_count: int = None,
        pad_launch_attempt_count__gt: int = None,
        pad_launch_attempt_count__gte: int = None,
        pad_launch_attempt_count__lt: int = None,
        pad_launch_attempt_count__lte: int = None,
        pad_launch_attempt_count_year: int = None,
        pad_launch_attempt_count_year__gt: int = None,
        pad_launch_attempt_count_year__gte: int = None,
        pad_launch_attempt_count_year__lt: int = None,
        pad_launch_attempt_count_year__lte: int = None,
        program: List[int] = None,
        related_lsp__id: List[int] = None,
        related_lsp__name: List[str] = None,
        rocket__configuration__full_name: str = None,
        rocket__configuration__full_name__icontains: str = None,
        rocket__configuration__id: int = None,
        rocket__configuration__manufacturer__name: str = None,
        rocket__configuration__manufacturer__name__icontains: str = None,
        rocket__configuration__name: str = None,
        rocket__spacecraftflight__spacecraft__id: int = None,
        rocket__spacecraftflight__spacecraft__name: str = None,
        rocket__spacecraftflight__spacecraft__name__icontains: str = None,
        search: str = None,
        serial_number: List[str] = None,
        slug: str = None,
        spacecraft_config__ids: List[int] = None,
        status: int = None,
        status__ids: List[int] = None,
        video_url: List[str] = None,
        window_end__gt: str = None,
        window_end__gte: str = None,
        window_end__lt: str = None,
        window_end__lte: str = None,
        window_start__gt: str = None,
        window_start__gte: str = None,
        window_start__lt: str = None,
        window_start__lte: str = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicLaunchEndpointList:
        params = {
            "agency_launch_attempt_count": agency_launch_attempt_count,
            "agency_launch_attempt_count__gt": agency_launch_attempt_count__gt,
            "agency_launch_attempt_count__gte": agency_launch_attempt_count__gte,
            "agency_launch_attempt_count__lt": agency_launch_attempt_count__lt,
            "agency_launch_attempt_count__lte": agency_launch_attempt_count__lte,
            "agency_launch_attempt_count_year": agency_launch_attempt_count_year,
            "agency_launch_attempt_count_year__gt": agency_launch_attempt_count_year__gt,
            "agency_launch_attempt_count_year__gte": agency_launch_attempt_count_year__gte,
            "agency_launch_attempt_count_year__lt": agency_launch_attempt_count_year__lt,
            "agency_launch_attempt_count_year__lte": agency_launch_attempt_count_year__lte,
            "day": day,
            "id": id,
            "include_suborbital": include_suborbital,
            "is_crewed": is_crewed,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "launch_designator": launch_designator,
            "launcher_config__id": launcher_config__id,
            "limit": limit,
            "location__ids": location__ids,
            "location_launch_attempt_count": location_launch_attempt_count,
            "location_launch_attempt_count__gt": location_launch_attempt_count__gt,
            "location_launch_attempt_count__gte": location_launch_attempt_count__gte,
            "location_launch_attempt_count__lt": location_launch_attempt_count__lt,
            "location_launch_attempt_count__lte": location_launch_attempt_count__lte,
            "location_launch_attempt_count_year": location_launch_attempt_count_year,
            "location_launch_attempt_count_year__gt": location_launch_attempt_count_year__gt,
            "location_launch_attempt_count_year__gte": location_launch_attempt_count_year__gte,
            "location_launch_attempt_count_year__lt": location_launch_attempt_count_year__lt,
            "location_launch_attempt_count_year__lte": location_launch_attempt_count_year__lte,
            "lsp__id": lsp__id,
            "lsp__name": lsp__name,
            "mission__orbit__celestial_body__id": mission__orbit__celestial_body__id,
            "mission__orbit__name": mission__orbit__name,
            "mission__orbit__name__icontains": mission__orbit__name__icontains,
            "month": month,
            "name": name,
            "net__gt": net__gt,
            "net__gte": net__gte,
            "net__lt": net__lt,
            "net__lte": net__lte,
            "offset": offset,
            "orbital_launch_attempt_count": orbital_launch_attempt_count,
            "orbital_launch_attempt_count__gt": orbital_launch_attempt_count__gt,
            "orbital_launch_attempt_count__gte": orbital_launch_attempt_count__gte,
            "orbital_launch_attempt_count__lt": orbital_launch_attempt_count__lt,
            "orbital_launch_attempt_count__lte": orbital_launch_attempt_count__lte,
            "orbital_launch_attempt_count_year": orbital_launch_attempt_count_year,
            "orbital_launch_attempt_count_year__gt": orbital_launch_attempt_count_year__gt,
            "orbital_launch_attempt_count_year__gte": orbital_launch_attempt_count_year__gte,
            "orbital_launch_attempt_count_year__lt": orbital_launch_attempt_count_year__lt,
            "orbital_launch_attempt_count_year__lte": orbital_launch_attempt_count_year__lte,
            "ordering": ordering,
            "pad": pad,
            "pad__location": pad__location,
            "pad__location__celestial_body__id": pad__location__celestial_body__id,
            "pad_launch_attempt_count": pad_launch_attempt_count,
            "pad_launch_attempt_count__gt": pad_launch_attempt_count__gt,
            "pad_launch_attempt_count__gte": pad_launch_attempt_count__gte,
            "pad_launch_attempt_count__lt": pad_launch_attempt_count__lt,
            "pad_launch_attempt_count__lte": pad_launch_attempt_count__lte,
            "pad_launch_attempt_count_year": pad_launch_attempt_count_year,
            "pad_launch_attempt_count_year__gt": pad_launch_attempt_count_year__gt,
            "pad_launch_attempt_count_year__gte": pad_launch_attempt_count_year__gte,
            "pad_launch_attempt_count_year__lt": pad_launch_attempt_count_year__lt,
            "pad_launch_attempt_count_year__lte": pad_launch_attempt_count_year__lte,
            "program": program,
            "related_lsp__id": related_lsp__id,
            "related_lsp__name": related_lsp__name,
            "rocket__configuration__full_name": rocket__configuration__full_name,
            "rocket__configuration__full_name__icontains": rocket__configuration__full_name__icontains,
            "rocket__configuration__id": rocket__configuration__id,
            "rocket__configuration__manufacturer__name": rocket__configuration__manufacturer__name,
            "rocket__configuration__manufacturer__name__icontains": rocket__configuration__manufacturer__name__icontains,
            "rocket__configuration__name": rocket__configuration__name,
            "rocket__spacecraftflight__spacecraft__id": rocket__spacecraftflight__spacecraft__id,
            "rocket__spacecraftflight__spacecraft__name": rocket__spacecraftflight__spacecraft__name,
            "rocket__spacecraftflight__spacecraft__name__icontains": rocket__spacecraftflight__spacecraft__name__icontains,
            "search": search,
            "serial_number": serial_number,
            "slug": slug,
            "spacecraft_config__ids": spacecraft_config__ids,
            "status": status,
            "status__ids": status__ids,
            "video_url": video_url,
            "window_end__gt": window_end__gt,
            "window_end__gte": window_end__gte,
            "window_end__lt": window_end__lt,
            "window_end__lte": window_end__lte,
            "window_start__gt": window_start__gt,
            "window_start__gte": window_start__gte,
            "window_start__lt": window_start__lt,
            "window_start__lte": window_start__lte,
            "year": year,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/launches/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLaunchEndpointList(**response)

    async def launches_list_async(
        self,
        agency_launch_attempt_count: int = None,
        agency_launch_attempt_count__gt: int = None,
        agency_launch_attempt_count__gte: int = None,
        agency_launch_attempt_count__lt: int = None,
        agency_launch_attempt_count__lte: int = None,
        agency_launch_attempt_count_year: int = None,
        agency_launch_attempt_count_year__gt: int = None,
        agency_launch_attempt_count_year__gte: int = None,
        agency_launch_attempt_count_year__lt: int = None,
        agency_launch_attempt_count_year__lte: int = None,
        day: List[float] = None,
        id: List[str] = None,
        include_suborbital: bool = None,
        is_crewed: bool = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        launch_designator: List[str] = None,
        launcher_config__id: List[int] = None,
        limit: int = None,
        location__ids: List[int] = None,
        location_launch_attempt_count: int = None,
        location_launch_attempt_count__gt: int = None,
        location_launch_attempt_count__gte: int = None,
        location_launch_attempt_count__lt: int = None,
        location_launch_attempt_count__lte: int = None,
        location_launch_attempt_count_year: int = None,
        location_launch_attempt_count_year__gt: int = None,
        location_launch_attempt_count_year__gte: int = None,
        location_launch_attempt_count_year__lt: int = None,
        location_launch_attempt_count_year__lte: int = None,
        lsp__id: List[int] = None,
        lsp__name: List[str] = None,
        mission__orbit__celestial_body__id: int = None,
        mission__orbit__name: str = None,
        mission__orbit__name__icontains: str = None,
        month: List[float] = None,
        name: str = None,
        net__gt: str = None,
        net__gte: str = None,
        net__lt: str = None,
        net__lte: str = None,
        offset: int = None,
        orbital_launch_attempt_count: int = None,
        orbital_launch_attempt_count__gt: int = None,
        orbital_launch_attempt_count__gte: int = None,
        orbital_launch_attempt_count__lt: int = None,
        orbital_launch_attempt_count__lte: int = None,
        orbital_launch_attempt_count_year: int = None,
        orbital_launch_attempt_count_year__gt: int = None,
        orbital_launch_attempt_count_year__gte: int = None,
        orbital_launch_attempt_count_year__lt: int = None,
        orbital_launch_attempt_count_year__lte: int = None,
        ordering: str = None,
        pad: int = None,
        pad__location: int = None,
        pad__location__celestial_body__id: int = None,
        pad_launch_attempt_count: int = None,
        pad_launch_attempt_count__gt: int = None,
        pad_launch_attempt_count__gte: int = None,
        pad_launch_attempt_count__lt: int = None,
        pad_launch_attempt_count__lte: int = None,
        pad_launch_attempt_count_year: int = None,
        pad_launch_attempt_count_year__gt: int = None,
        pad_launch_attempt_count_year__gte: int = None,
        pad_launch_attempt_count_year__lt: int = None,
        pad_launch_attempt_count_year__lte: int = None,
        program: List[int] = None,
        related_lsp__id: List[int] = None,
        related_lsp__name: List[str] = None,
        rocket__configuration__full_name: str = None,
        rocket__configuration__full_name__icontains: str = None,
        rocket__configuration__id: int = None,
        rocket__configuration__manufacturer__name: str = None,
        rocket__configuration__manufacturer__name__icontains: str = None,
        rocket__configuration__name: str = None,
        rocket__spacecraftflight__spacecraft__id: int = None,
        rocket__spacecraftflight__spacecraft__name: str = None,
        rocket__spacecraftflight__spacecraft__name__icontains: str = None,
        search: str = None,
        serial_number: List[str] = None,
        slug: str = None,
        spacecraft_config__ids: List[int] = None,
        status: int = None,
        status__ids: List[int] = None,
        video_url: List[str] = None,
        window_end__gt: str = None,
        window_end__gte: str = None,
        window_end__lt: str = None,
        window_end__lte: str = None,
        window_start__gt: str = None,
        window_start__gte: str = None,
        window_start__lt: str = None,
        window_start__lte: str = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicLaunchEndpointList:
        params = {
            "agency_launch_attempt_count": agency_launch_attempt_count,
            "agency_launch_attempt_count__gt": agency_launch_attempt_count__gt,
            "agency_launch_attempt_count__gte": agency_launch_attempt_count__gte,
            "agency_launch_attempt_count__lt": agency_launch_attempt_count__lt,
            "agency_launch_attempt_count__lte": agency_launch_attempt_count__lte,
            "agency_launch_attempt_count_year": agency_launch_attempt_count_year,
            "agency_launch_attempt_count_year__gt": agency_launch_attempt_count_year__gt,
            "agency_launch_attempt_count_year__gte": agency_launch_attempt_count_year__gte,
            "agency_launch_attempt_count_year__lt": agency_launch_attempt_count_year__lt,
            "agency_launch_attempt_count_year__lte": agency_launch_attempt_count_year__lte,
            "day": day,
            "id": id,
            "include_suborbital": include_suborbital,
            "is_crewed": is_crewed,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "launch_designator": launch_designator,
            "launcher_config__id": launcher_config__id,
            "limit": limit,
            "location__ids": location__ids,
            "location_launch_attempt_count": location_launch_attempt_count,
            "location_launch_attempt_count__gt": location_launch_attempt_count__gt,
            "location_launch_attempt_count__gte": location_launch_attempt_count__gte,
            "location_launch_attempt_count__lt": location_launch_attempt_count__lt,
            "location_launch_attempt_count__lte": location_launch_attempt_count__lte,
            "location_launch_attempt_count_year": location_launch_attempt_count_year,
            "location_launch_attempt_count_year__gt": location_launch_attempt_count_year__gt,
            "location_launch_attempt_count_year__gte": location_launch_attempt_count_year__gte,
            "location_launch_attempt_count_year__lt": location_launch_attempt_count_year__lt,
            "location_launch_attempt_count_year__lte": location_launch_attempt_count_year__lte,
            "lsp__id": lsp__id,
            "lsp__name": lsp__name,
            "mission__orbit__celestial_body__id": mission__orbit__celestial_body__id,
            "mission__orbit__name": mission__orbit__name,
            "mission__orbit__name__icontains": mission__orbit__name__icontains,
            "month": month,
            "name": name,
            "net__gt": net__gt,
            "net__gte": net__gte,
            "net__lt": net__lt,
            "net__lte": net__lte,
            "offset": offset,
            "orbital_launch_attempt_count": orbital_launch_attempt_count,
            "orbital_launch_attempt_count__gt": orbital_launch_attempt_count__gt,
            "orbital_launch_attempt_count__gte": orbital_launch_attempt_count__gte,
            "orbital_launch_attempt_count__lt": orbital_launch_attempt_count__lt,
            "orbital_launch_attempt_count__lte": orbital_launch_attempt_count__lte,
            "orbital_launch_attempt_count_year": orbital_launch_attempt_count_year,
            "orbital_launch_attempt_count_year__gt": orbital_launch_attempt_count_year__gt,
            "orbital_launch_attempt_count_year__gte": orbital_launch_attempt_count_year__gte,
            "orbital_launch_attempt_count_year__lt": orbital_launch_attempt_count_year__lt,
            "orbital_launch_attempt_count_year__lte": orbital_launch_attempt_count_year__lte,
            "ordering": ordering,
            "pad": pad,
            "pad__location": pad__location,
            "pad__location__celestial_body__id": pad__location__celestial_body__id,
            "pad_launch_attempt_count": pad_launch_attempt_count,
            "pad_launch_attempt_count__gt": pad_launch_attempt_count__gt,
            "pad_launch_attempt_count__gte": pad_launch_attempt_count__gte,
            "pad_launch_attempt_count__lt": pad_launch_attempt_count__lt,
            "pad_launch_attempt_count__lte": pad_launch_attempt_count__lte,
            "pad_launch_attempt_count_year": pad_launch_attempt_count_year,
            "pad_launch_attempt_count_year__gt": pad_launch_attempt_count_year__gt,
            "pad_launch_attempt_count_year__gte": pad_launch_attempt_count_year__gte,
            "pad_launch_attempt_count_year__lt": pad_launch_attempt_count_year__lt,
            "pad_launch_attempt_count_year__lte": pad_launch_attempt_count_year__lte,
            "program": program,
            "related_lsp__id": related_lsp__id,
            "related_lsp__name": related_lsp__name,
            "rocket__configuration__full_name": rocket__configuration__full_name,
            "rocket__configuration__full_name__icontains": rocket__configuration__full_name__icontains,
            "rocket__configuration__id": rocket__configuration__id,
            "rocket__configuration__manufacturer__name": rocket__configuration__manufacturer__name,
            "rocket__configuration__manufacturer__name__icontains": rocket__configuration__manufacturer__name__icontains,
            "rocket__configuration__name": rocket__configuration__name,
            "rocket__spacecraftflight__spacecraft__id": rocket__spacecraftflight__spacecraft__id,
            "rocket__spacecraftflight__spacecraft__name": rocket__spacecraftflight__spacecraft__name,
            "rocket__spacecraftflight__spacecraft__name__icontains": rocket__spacecraftflight__spacecraft__name__icontains,
            "search": search,
            "serial_number": serial_number,
            "slug": slug,
            "spacecraft_config__ids": spacecraft_config__ids,
            "status": status,
            "status__ids": status__ids,
            "video_url": video_url,
            "window_end__gt": window_end__gt,
            "window_end__gte": window_end__gte,
            "window_end__lt": window_end__lt,
            "window_end__lte": window_end__lte,
            "window_start__gt": window_start__gt,
            "window_start__gte": window_start__gte,
            "window_start__lt": window_start__lt,
            "window_start__lte": window_start__lte,
            "year": year,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/launches/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLaunchEndpointList(**response)

    def launches_retrieve(self, id: str = None, **kwargs) -> LaunchDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/launches/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LaunchDetailed(**response)

    async def launches_retrieve_async(self, id: str = None, **kwargs) -> LaunchDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/launches/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LaunchDetailed(**response)

    def launches_previous_list(
        self,
        agency_launch_attempt_count: int = None,
        agency_launch_attempt_count__gt: int = None,
        agency_launch_attempt_count__gte: int = None,
        agency_launch_attempt_count__lt: int = None,
        agency_launch_attempt_count__lte: int = None,
        agency_launch_attempt_count_year: int = None,
        agency_launch_attempt_count_year__gt: int = None,
        agency_launch_attempt_count_year__gte: int = None,
        agency_launch_attempt_count_year__lt: int = None,
        agency_launch_attempt_count_year__lte: int = None,
        day: List[float] = None,
        id: List[str] = None,
        include_suborbital: bool = None,
        is_crewed: bool = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        launch_designator: List[str] = None,
        launcher_config__id: List[int] = None,
        limit: int = None,
        location__ids: List[int] = None,
        location_launch_attempt_count: int = None,
        location_launch_attempt_count__gt: int = None,
        location_launch_attempt_count__gte: int = None,
        location_launch_attempt_count__lt: int = None,
        location_launch_attempt_count__lte: int = None,
        location_launch_attempt_count_year: int = None,
        location_launch_attempt_count_year__gt: int = None,
        location_launch_attempt_count_year__gte: int = None,
        location_launch_attempt_count_year__lt: int = None,
        location_launch_attempt_count_year__lte: int = None,
        lsp__id: List[int] = None,
        lsp__name: List[str] = None,
        mission__orbit__celestial_body__id: int = None,
        mission__orbit__name: str = None,
        mission__orbit__name__icontains: str = None,
        month: List[float] = None,
        name: str = None,
        net__gt: str = None,
        net__gte: str = None,
        net__lt: str = None,
        net__lte: str = None,
        offset: int = None,
        orbital_launch_attempt_count: int = None,
        orbital_launch_attempt_count__gt: int = None,
        orbital_launch_attempt_count__gte: int = None,
        orbital_launch_attempt_count__lt: int = None,
        orbital_launch_attempt_count__lte: int = None,
        orbital_launch_attempt_count_year: int = None,
        orbital_launch_attempt_count_year__gt: int = None,
        orbital_launch_attempt_count_year__gte: int = None,
        orbital_launch_attempt_count_year__lt: int = None,
        orbital_launch_attempt_count_year__lte: int = None,
        ordering: str = None,
        pad: int = None,
        pad__location: int = None,
        pad__location__celestial_body__id: int = None,
        pad_launch_attempt_count: int = None,
        pad_launch_attempt_count__gt: int = None,
        pad_launch_attempt_count__gte: int = None,
        pad_launch_attempt_count__lt: int = None,
        pad_launch_attempt_count__lte: int = None,
        pad_launch_attempt_count_year: int = None,
        pad_launch_attempt_count_year__gt: int = None,
        pad_launch_attempt_count_year__gte: int = None,
        pad_launch_attempt_count_year__lt: int = None,
        pad_launch_attempt_count_year__lte: int = None,
        program: List[int] = None,
        related_lsp__id: List[int] = None,
        related_lsp__name: List[str] = None,
        rocket__configuration__full_name: str = None,
        rocket__configuration__full_name__icontains: str = None,
        rocket__configuration__id: int = None,
        rocket__configuration__manufacturer__name: str = None,
        rocket__configuration__manufacturer__name__icontains: str = None,
        rocket__configuration__name: str = None,
        rocket__spacecraftflight__spacecraft__id: int = None,
        rocket__spacecraftflight__spacecraft__name: str = None,
        rocket__spacecraftflight__spacecraft__name__icontains: str = None,
        search: str = None,
        serial_number: List[str] = None,
        slug: str = None,
        spacecraft_config__ids: List[int] = None,
        status: int = None,
        status__ids: List[int] = None,
        video_url: List[str] = None,
        window_end__gt: str = None,
        window_end__gte: str = None,
        window_end__lt: str = None,
        window_end__lte: str = None,
        window_start__gt: str = None,
        window_start__gte: str = None,
        window_start__lt: str = None,
        window_start__lte: str = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicLaunchEndpointList:
        params = {
            "agency_launch_attempt_count": agency_launch_attempt_count,
            "agency_launch_attempt_count__gt": agency_launch_attempt_count__gt,
            "agency_launch_attempt_count__gte": agency_launch_attempt_count__gte,
            "agency_launch_attempt_count__lt": agency_launch_attempt_count__lt,
            "agency_launch_attempt_count__lte": agency_launch_attempt_count__lte,
            "agency_launch_attempt_count_year": agency_launch_attempt_count_year,
            "agency_launch_attempt_count_year__gt": agency_launch_attempt_count_year__gt,
            "agency_launch_attempt_count_year__gte": agency_launch_attempt_count_year__gte,
            "agency_launch_attempt_count_year__lt": agency_launch_attempt_count_year__lt,
            "agency_launch_attempt_count_year__lte": agency_launch_attempt_count_year__lte,
            "day": day,
            "id": id,
            "include_suborbital": include_suborbital,
            "is_crewed": is_crewed,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "launch_designator": launch_designator,
            "launcher_config__id": launcher_config__id,
            "limit": limit,
            "location__ids": location__ids,
            "location_launch_attempt_count": location_launch_attempt_count,
            "location_launch_attempt_count__gt": location_launch_attempt_count__gt,
            "location_launch_attempt_count__gte": location_launch_attempt_count__gte,
            "location_launch_attempt_count__lt": location_launch_attempt_count__lt,
            "location_launch_attempt_count__lte": location_launch_attempt_count__lte,
            "location_launch_attempt_count_year": location_launch_attempt_count_year,
            "location_launch_attempt_count_year__gt": location_launch_attempt_count_year__gt,
            "location_launch_attempt_count_year__gte": location_launch_attempt_count_year__gte,
            "location_launch_attempt_count_year__lt": location_launch_attempt_count_year__lt,
            "location_launch_attempt_count_year__lte": location_launch_attempt_count_year__lte,
            "lsp__id": lsp__id,
            "lsp__name": lsp__name,
            "mission__orbit__celestial_body__id": mission__orbit__celestial_body__id,
            "mission__orbit__name": mission__orbit__name,
            "mission__orbit__name__icontains": mission__orbit__name__icontains,
            "month": month,
            "name": name,
            "net__gt": net__gt,
            "net__gte": net__gte,
            "net__lt": net__lt,
            "net__lte": net__lte,
            "offset": offset,
            "orbital_launch_attempt_count": orbital_launch_attempt_count,
            "orbital_launch_attempt_count__gt": orbital_launch_attempt_count__gt,
            "orbital_launch_attempt_count__gte": orbital_launch_attempt_count__gte,
            "orbital_launch_attempt_count__lt": orbital_launch_attempt_count__lt,
            "orbital_launch_attempt_count__lte": orbital_launch_attempt_count__lte,
            "orbital_launch_attempt_count_year": orbital_launch_attempt_count_year,
            "orbital_launch_attempt_count_year__gt": orbital_launch_attempt_count_year__gt,
            "orbital_launch_attempt_count_year__gte": orbital_launch_attempt_count_year__gte,
            "orbital_launch_attempt_count_year__lt": orbital_launch_attempt_count_year__lt,
            "orbital_launch_attempt_count_year__lte": orbital_launch_attempt_count_year__lte,
            "ordering": ordering,
            "pad": pad,
            "pad__location": pad__location,
            "pad__location__celestial_body__id": pad__location__celestial_body__id,
            "pad_launch_attempt_count": pad_launch_attempt_count,
            "pad_launch_attempt_count__gt": pad_launch_attempt_count__gt,
            "pad_launch_attempt_count__gte": pad_launch_attempt_count__gte,
            "pad_launch_attempt_count__lt": pad_launch_attempt_count__lt,
            "pad_launch_attempt_count__lte": pad_launch_attempt_count__lte,
            "pad_launch_attempt_count_year": pad_launch_attempt_count_year,
            "pad_launch_attempt_count_year__gt": pad_launch_attempt_count_year__gt,
            "pad_launch_attempt_count_year__gte": pad_launch_attempt_count_year__gte,
            "pad_launch_attempt_count_year__lt": pad_launch_attempt_count_year__lt,
            "pad_launch_attempt_count_year__lte": pad_launch_attempt_count_year__lte,
            "program": program,
            "related_lsp__id": related_lsp__id,
            "related_lsp__name": related_lsp__name,
            "rocket__configuration__full_name": rocket__configuration__full_name,
            "rocket__configuration__full_name__icontains": rocket__configuration__full_name__icontains,
            "rocket__configuration__id": rocket__configuration__id,
            "rocket__configuration__manufacturer__name": rocket__configuration__manufacturer__name,
            "rocket__configuration__manufacturer__name__icontains": rocket__configuration__manufacturer__name__icontains,
            "rocket__configuration__name": rocket__configuration__name,
            "rocket__spacecraftflight__spacecraft__id": rocket__spacecraftflight__spacecraft__id,
            "rocket__spacecraftflight__spacecraft__name": rocket__spacecraftflight__spacecraft__name,
            "rocket__spacecraftflight__spacecraft__name__icontains": rocket__spacecraftflight__spacecraft__name__icontains,
            "search": search,
            "serial_number": serial_number,
            "slug": slug,
            "spacecraft_config__ids": spacecraft_config__ids,
            "status": status,
            "status__ids": status__ids,
            "video_url": video_url,
            "window_end__gt": window_end__gt,
            "window_end__gte": window_end__gte,
            "window_end__lt": window_end__lt,
            "window_end__lte": window_end__lte,
            "window_start__gt": window_start__gt,
            "window_start__gte": window_start__gte,
            "window_start__lt": window_start__lt,
            "window_start__lte": window_start__lte,
            "year": year,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/launches/previous/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLaunchEndpointList(**response)

    async def launches_previous_list_async(
        self,
        agency_launch_attempt_count: int = None,
        agency_launch_attempt_count__gt: int = None,
        agency_launch_attempt_count__gte: int = None,
        agency_launch_attempt_count__lt: int = None,
        agency_launch_attempt_count__lte: int = None,
        agency_launch_attempt_count_year: int = None,
        agency_launch_attempt_count_year__gt: int = None,
        agency_launch_attempt_count_year__gte: int = None,
        agency_launch_attempt_count_year__lt: int = None,
        agency_launch_attempt_count_year__lte: int = None,
        day: List[float] = None,
        id: List[str] = None,
        include_suborbital: bool = None,
        is_crewed: bool = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        launch_designator: List[str] = None,
        launcher_config__id: List[int] = None,
        limit: int = None,
        location__ids: List[int] = None,
        location_launch_attempt_count: int = None,
        location_launch_attempt_count__gt: int = None,
        location_launch_attempt_count__gte: int = None,
        location_launch_attempt_count__lt: int = None,
        location_launch_attempt_count__lte: int = None,
        location_launch_attempt_count_year: int = None,
        location_launch_attempt_count_year__gt: int = None,
        location_launch_attempt_count_year__gte: int = None,
        location_launch_attempt_count_year__lt: int = None,
        location_launch_attempt_count_year__lte: int = None,
        lsp__id: List[int] = None,
        lsp__name: List[str] = None,
        mission__orbit__celestial_body__id: int = None,
        mission__orbit__name: str = None,
        mission__orbit__name__icontains: str = None,
        month: List[float] = None,
        name: str = None,
        net__gt: str = None,
        net__gte: str = None,
        net__lt: str = None,
        net__lte: str = None,
        offset: int = None,
        orbital_launch_attempt_count: int = None,
        orbital_launch_attempt_count__gt: int = None,
        orbital_launch_attempt_count__gte: int = None,
        orbital_launch_attempt_count__lt: int = None,
        orbital_launch_attempt_count__lte: int = None,
        orbital_launch_attempt_count_year: int = None,
        orbital_launch_attempt_count_year__gt: int = None,
        orbital_launch_attempt_count_year__gte: int = None,
        orbital_launch_attempt_count_year__lt: int = None,
        orbital_launch_attempt_count_year__lte: int = None,
        ordering: str = None,
        pad: int = None,
        pad__location: int = None,
        pad__location__celestial_body__id: int = None,
        pad_launch_attempt_count: int = None,
        pad_launch_attempt_count__gt: int = None,
        pad_launch_attempt_count__gte: int = None,
        pad_launch_attempt_count__lt: int = None,
        pad_launch_attempt_count__lte: int = None,
        pad_launch_attempt_count_year: int = None,
        pad_launch_attempt_count_year__gt: int = None,
        pad_launch_attempt_count_year__gte: int = None,
        pad_launch_attempt_count_year__lt: int = None,
        pad_launch_attempt_count_year__lte: int = None,
        program: List[int] = None,
        related_lsp__id: List[int] = None,
        related_lsp__name: List[str] = None,
        rocket__configuration__full_name: str = None,
        rocket__configuration__full_name__icontains: str = None,
        rocket__configuration__id: int = None,
        rocket__configuration__manufacturer__name: str = None,
        rocket__configuration__manufacturer__name__icontains: str = None,
        rocket__configuration__name: str = None,
        rocket__spacecraftflight__spacecraft__id: int = None,
        rocket__spacecraftflight__spacecraft__name: str = None,
        rocket__spacecraftflight__spacecraft__name__icontains: str = None,
        search: str = None,
        serial_number: List[str] = None,
        slug: str = None,
        spacecraft_config__ids: List[int] = None,
        status: int = None,
        status__ids: List[int] = None,
        video_url: List[str] = None,
        window_end__gt: str = None,
        window_end__gte: str = None,
        window_end__lt: str = None,
        window_end__lte: str = None,
        window_start__gt: str = None,
        window_start__gte: str = None,
        window_start__lt: str = None,
        window_start__lte: str = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicLaunchEndpointList:
        params = {
            "agency_launch_attempt_count": agency_launch_attempt_count,
            "agency_launch_attempt_count__gt": agency_launch_attempt_count__gt,
            "agency_launch_attempt_count__gte": agency_launch_attempt_count__gte,
            "agency_launch_attempt_count__lt": agency_launch_attempt_count__lt,
            "agency_launch_attempt_count__lte": agency_launch_attempt_count__lte,
            "agency_launch_attempt_count_year": agency_launch_attempt_count_year,
            "agency_launch_attempt_count_year__gt": agency_launch_attempt_count_year__gt,
            "agency_launch_attempt_count_year__gte": agency_launch_attempt_count_year__gte,
            "agency_launch_attempt_count_year__lt": agency_launch_attempt_count_year__lt,
            "agency_launch_attempt_count_year__lte": agency_launch_attempt_count_year__lte,
            "day": day,
            "id": id,
            "include_suborbital": include_suborbital,
            "is_crewed": is_crewed,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "launch_designator": launch_designator,
            "launcher_config__id": launcher_config__id,
            "limit": limit,
            "location__ids": location__ids,
            "location_launch_attempt_count": location_launch_attempt_count,
            "location_launch_attempt_count__gt": location_launch_attempt_count__gt,
            "location_launch_attempt_count__gte": location_launch_attempt_count__gte,
            "location_launch_attempt_count__lt": location_launch_attempt_count__lt,
            "location_launch_attempt_count__lte": location_launch_attempt_count__lte,
            "location_launch_attempt_count_year": location_launch_attempt_count_year,
            "location_launch_attempt_count_year__gt": location_launch_attempt_count_year__gt,
            "location_launch_attempt_count_year__gte": location_launch_attempt_count_year__gte,
            "location_launch_attempt_count_year__lt": location_launch_attempt_count_year__lt,
            "location_launch_attempt_count_year__lte": location_launch_attempt_count_year__lte,
            "lsp__id": lsp__id,
            "lsp__name": lsp__name,
            "mission__orbit__celestial_body__id": mission__orbit__celestial_body__id,
            "mission__orbit__name": mission__orbit__name,
            "mission__orbit__name__icontains": mission__orbit__name__icontains,
            "month": month,
            "name": name,
            "net__gt": net__gt,
            "net__gte": net__gte,
            "net__lt": net__lt,
            "net__lte": net__lte,
            "offset": offset,
            "orbital_launch_attempt_count": orbital_launch_attempt_count,
            "orbital_launch_attempt_count__gt": orbital_launch_attempt_count__gt,
            "orbital_launch_attempt_count__gte": orbital_launch_attempt_count__gte,
            "orbital_launch_attempt_count__lt": orbital_launch_attempt_count__lt,
            "orbital_launch_attempt_count__lte": orbital_launch_attempt_count__lte,
            "orbital_launch_attempt_count_year": orbital_launch_attempt_count_year,
            "orbital_launch_attempt_count_year__gt": orbital_launch_attempt_count_year__gt,
            "orbital_launch_attempt_count_year__gte": orbital_launch_attempt_count_year__gte,
            "orbital_launch_attempt_count_year__lt": orbital_launch_attempt_count_year__lt,
            "orbital_launch_attempt_count_year__lte": orbital_launch_attempt_count_year__lte,
            "ordering": ordering,
            "pad": pad,
            "pad__location": pad__location,
            "pad__location__celestial_body__id": pad__location__celestial_body__id,
            "pad_launch_attempt_count": pad_launch_attempt_count,
            "pad_launch_attempt_count__gt": pad_launch_attempt_count__gt,
            "pad_launch_attempt_count__gte": pad_launch_attempt_count__gte,
            "pad_launch_attempt_count__lt": pad_launch_attempt_count__lt,
            "pad_launch_attempt_count__lte": pad_launch_attempt_count__lte,
            "pad_launch_attempt_count_year": pad_launch_attempt_count_year,
            "pad_launch_attempt_count_year__gt": pad_launch_attempt_count_year__gt,
            "pad_launch_attempt_count_year__gte": pad_launch_attempt_count_year__gte,
            "pad_launch_attempt_count_year__lt": pad_launch_attempt_count_year__lt,
            "pad_launch_attempt_count_year__lte": pad_launch_attempt_count_year__lte,
            "program": program,
            "related_lsp__id": related_lsp__id,
            "related_lsp__name": related_lsp__name,
            "rocket__configuration__full_name": rocket__configuration__full_name,
            "rocket__configuration__full_name__icontains": rocket__configuration__full_name__icontains,
            "rocket__configuration__id": rocket__configuration__id,
            "rocket__configuration__manufacturer__name": rocket__configuration__manufacturer__name,
            "rocket__configuration__manufacturer__name__icontains": rocket__configuration__manufacturer__name__icontains,
            "rocket__configuration__name": rocket__configuration__name,
            "rocket__spacecraftflight__spacecraft__id": rocket__spacecraftflight__spacecraft__id,
            "rocket__spacecraftflight__spacecraft__name": rocket__spacecraftflight__spacecraft__name,
            "rocket__spacecraftflight__spacecraft__name__icontains": rocket__spacecraftflight__spacecraft__name__icontains,
            "search": search,
            "serial_number": serial_number,
            "slug": slug,
            "spacecraft_config__ids": spacecraft_config__ids,
            "status": status,
            "status__ids": status__ids,
            "video_url": video_url,
            "window_end__gt": window_end__gt,
            "window_end__gte": window_end__gte,
            "window_end__lt": window_end__lt,
            "window_end__lte": window_end__lte,
            "window_start__gt": window_start__gt,
            "window_start__gte": window_start__gte,
            "window_start__lt": window_start__lt,
            "window_start__lte": window_start__lte,
            "year": year,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/launches/previous/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLaunchEndpointList(**response)

    def launches_previous_retrieve(self, id: str = None, **kwargs) -> LaunchDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/launches/previous/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LaunchDetailed(**response)

    async def launches_previous_retrieve_async(
        self, id: str = None, **kwargs
    ) -> LaunchDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/launches/previous/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LaunchDetailed(**response)

    def launches_upcoming_list(
        self,
        agency_launch_attempt_count: int = None,
        agency_launch_attempt_count__gt: int = None,
        agency_launch_attempt_count__gte: int = None,
        agency_launch_attempt_count__lt: int = None,
        agency_launch_attempt_count__lte: int = None,
        agency_launch_attempt_count_year: int = None,
        agency_launch_attempt_count_year__gt: int = None,
        agency_launch_attempt_count_year__gte: int = None,
        agency_launch_attempt_count_year__lt: int = None,
        agency_launch_attempt_count_year__lte: int = None,
        day: List[float] = None,
        hide_recent_previous: bool = None,
        id: List[str] = None,
        include_suborbital: bool = None,
        is_crewed: bool = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        launch_designator: List[str] = None,
        launcher_config__id: List[int] = None,
        limit: int = None,
        location__ids: List[int] = None,
        location_launch_attempt_count: int = None,
        location_launch_attempt_count__gt: int = None,
        location_launch_attempt_count__gte: int = None,
        location_launch_attempt_count__lt: int = None,
        location_launch_attempt_count__lte: int = None,
        location_launch_attempt_count_year: int = None,
        location_launch_attempt_count_year__gt: int = None,
        location_launch_attempt_count_year__gte: int = None,
        location_launch_attempt_count_year__lt: int = None,
        location_launch_attempt_count_year__lte: int = None,
        lsp__id: List[int] = None,
        lsp__name: List[str] = None,
        mission__orbit__celestial_body__id: int = None,
        mission__orbit__name: str = None,
        mission__orbit__name__icontains: str = None,
        month: List[float] = None,
        name: str = None,
        net__gt: str = None,
        net__gte: str = None,
        net__lt: str = None,
        net__lte: str = None,
        offset: int = None,
        orbital_launch_attempt_count: int = None,
        orbital_launch_attempt_count__gt: int = None,
        orbital_launch_attempt_count__gte: int = None,
        orbital_launch_attempt_count__lt: int = None,
        orbital_launch_attempt_count__lte: int = None,
        orbital_launch_attempt_count_year: int = None,
        orbital_launch_attempt_count_year__gt: int = None,
        orbital_launch_attempt_count_year__gte: int = None,
        orbital_launch_attempt_count_year__lt: int = None,
        orbital_launch_attempt_count_year__lte: int = None,
        ordering: str = None,
        pad: int = None,
        pad__location: int = None,
        pad__location__celestial_body__id: int = None,
        pad_launch_attempt_count: int = None,
        pad_launch_attempt_count__gt: int = None,
        pad_launch_attempt_count__gte: int = None,
        pad_launch_attempt_count__lt: int = None,
        pad_launch_attempt_count__lte: int = None,
        pad_launch_attempt_count_year: int = None,
        pad_launch_attempt_count_year__gt: int = None,
        pad_launch_attempt_count_year__gte: int = None,
        pad_launch_attempt_count_year__lt: int = None,
        pad_launch_attempt_count_year__lte: int = None,
        program: List[int] = None,
        related_lsp__id: List[int] = None,
        related_lsp__name: List[str] = None,
        rocket__configuration__full_name: str = None,
        rocket__configuration__full_name__icontains: str = None,
        rocket__configuration__id: int = None,
        rocket__configuration__manufacturer__name: str = None,
        rocket__configuration__manufacturer__name__icontains: str = None,
        rocket__configuration__name: str = None,
        rocket__spacecraftflight__spacecraft__id: int = None,
        rocket__spacecraftflight__spacecraft__name: str = None,
        rocket__spacecraftflight__spacecraft__name__icontains: str = None,
        search: str = None,
        serial_number: List[str] = None,
        slug: str = None,
        spacecraft_config__ids: List[int] = None,
        status: int = None,
        status__ids: List[int] = None,
        video_url: List[str] = None,
        window_end__gt: str = None,
        window_end__gte: str = None,
        window_end__lt: str = None,
        window_end__lte: str = None,
        window_start__gt: str = None,
        window_start__gte: str = None,
        window_start__lt: str = None,
        window_start__lte: str = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicLaunchEndpointList:
        params = {
            "agency_launch_attempt_count": agency_launch_attempt_count,
            "agency_launch_attempt_count__gt": agency_launch_attempt_count__gt,
            "agency_launch_attempt_count__gte": agency_launch_attempt_count__gte,
            "agency_launch_attempt_count__lt": agency_launch_attempt_count__lt,
            "agency_launch_attempt_count__lte": agency_launch_attempt_count__lte,
            "agency_launch_attempt_count_year": agency_launch_attempt_count_year,
            "agency_launch_attempt_count_year__gt": agency_launch_attempt_count_year__gt,
            "agency_launch_attempt_count_year__gte": agency_launch_attempt_count_year__gte,
            "agency_launch_attempt_count_year__lt": agency_launch_attempt_count_year__lt,
            "agency_launch_attempt_count_year__lte": agency_launch_attempt_count_year__lte,
            "day": day,
            "hide_recent_previous": hide_recent_previous,
            "id": id,
            "include_suborbital": include_suborbital,
            "is_crewed": is_crewed,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "launch_designator": launch_designator,
            "launcher_config__id": launcher_config__id,
            "limit": limit,
            "location__ids": location__ids,
            "location_launch_attempt_count": location_launch_attempt_count,
            "location_launch_attempt_count__gt": location_launch_attempt_count__gt,
            "location_launch_attempt_count__gte": location_launch_attempt_count__gte,
            "location_launch_attempt_count__lt": location_launch_attempt_count__lt,
            "location_launch_attempt_count__lte": location_launch_attempt_count__lte,
            "location_launch_attempt_count_year": location_launch_attempt_count_year,
            "location_launch_attempt_count_year__gt": location_launch_attempt_count_year__gt,
            "location_launch_attempt_count_year__gte": location_launch_attempt_count_year__gte,
            "location_launch_attempt_count_year__lt": location_launch_attempt_count_year__lt,
            "location_launch_attempt_count_year__lte": location_launch_attempt_count_year__lte,
            "lsp__id": lsp__id,
            "lsp__name": lsp__name,
            "mission__orbit__celestial_body__id": mission__orbit__celestial_body__id,
            "mission__orbit__name": mission__orbit__name,
            "mission__orbit__name__icontains": mission__orbit__name__icontains,
            "month": month,
            "name": name,
            "net__gt": net__gt,
            "net__gte": net__gte,
            "net__lt": net__lt,
            "net__lte": net__lte,
            "offset": offset,
            "orbital_launch_attempt_count": orbital_launch_attempt_count,
            "orbital_launch_attempt_count__gt": orbital_launch_attempt_count__gt,
            "orbital_launch_attempt_count__gte": orbital_launch_attempt_count__gte,
            "orbital_launch_attempt_count__lt": orbital_launch_attempt_count__lt,
            "orbital_launch_attempt_count__lte": orbital_launch_attempt_count__lte,
            "orbital_launch_attempt_count_year": orbital_launch_attempt_count_year,
            "orbital_launch_attempt_count_year__gt": orbital_launch_attempt_count_year__gt,
            "orbital_launch_attempt_count_year__gte": orbital_launch_attempt_count_year__gte,
            "orbital_launch_attempt_count_year__lt": orbital_launch_attempt_count_year__lt,
            "orbital_launch_attempt_count_year__lte": orbital_launch_attempt_count_year__lte,
            "ordering": ordering,
            "pad": pad,
            "pad__location": pad__location,
            "pad__location__celestial_body__id": pad__location__celestial_body__id,
            "pad_launch_attempt_count": pad_launch_attempt_count,
            "pad_launch_attempt_count__gt": pad_launch_attempt_count__gt,
            "pad_launch_attempt_count__gte": pad_launch_attempt_count__gte,
            "pad_launch_attempt_count__lt": pad_launch_attempt_count__lt,
            "pad_launch_attempt_count__lte": pad_launch_attempt_count__lte,
            "pad_launch_attempt_count_year": pad_launch_attempt_count_year,
            "pad_launch_attempt_count_year__gt": pad_launch_attempt_count_year__gt,
            "pad_launch_attempt_count_year__gte": pad_launch_attempt_count_year__gte,
            "pad_launch_attempt_count_year__lt": pad_launch_attempt_count_year__lt,
            "pad_launch_attempt_count_year__lte": pad_launch_attempt_count_year__lte,
            "program": program,
            "related_lsp__id": related_lsp__id,
            "related_lsp__name": related_lsp__name,
            "rocket__configuration__full_name": rocket__configuration__full_name,
            "rocket__configuration__full_name__icontains": rocket__configuration__full_name__icontains,
            "rocket__configuration__id": rocket__configuration__id,
            "rocket__configuration__manufacturer__name": rocket__configuration__manufacturer__name,
            "rocket__configuration__manufacturer__name__icontains": rocket__configuration__manufacturer__name__icontains,
            "rocket__configuration__name": rocket__configuration__name,
            "rocket__spacecraftflight__spacecraft__id": rocket__spacecraftflight__spacecraft__id,
            "rocket__spacecraftflight__spacecraft__name": rocket__spacecraftflight__spacecraft__name,
            "rocket__spacecraftflight__spacecraft__name__icontains": rocket__spacecraftflight__spacecraft__name__icontains,
            "search": search,
            "serial_number": serial_number,
            "slug": slug,
            "spacecraft_config__ids": spacecraft_config__ids,
            "status": status,
            "status__ids": status__ids,
            "video_url": video_url,
            "window_end__gt": window_end__gt,
            "window_end__gte": window_end__gte,
            "window_end__lt": window_end__lt,
            "window_end__lte": window_end__lte,
            "window_start__gt": window_start__gt,
            "window_start__gte": window_start__gte,
            "window_start__lt": window_start__lt,
            "window_start__lte": window_start__lte,
            "year": year,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/launches/upcoming/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLaunchEndpointList(**response)

    async def launches_upcoming_list_async(
        self,
        agency_launch_attempt_count: int = None,
        agency_launch_attempt_count__gt: int = None,
        agency_launch_attempt_count__gte: int = None,
        agency_launch_attempt_count__lt: int = None,
        agency_launch_attempt_count__lte: int = None,
        agency_launch_attempt_count_year: int = None,
        agency_launch_attempt_count_year__gt: int = None,
        agency_launch_attempt_count_year__gte: int = None,
        agency_launch_attempt_count_year__lt: int = None,
        agency_launch_attempt_count_year__lte: int = None,
        day: List[float] = None,
        hide_recent_previous: bool = None,
        id: List[str] = None,
        include_suborbital: bool = None,
        is_crewed: bool = None,
        last_updated__gte: str = None,
        last_updated__lte: str = None,
        launch_designator: List[str] = None,
        launcher_config__id: List[int] = None,
        limit: int = None,
        location__ids: List[int] = None,
        location_launch_attempt_count: int = None,
        location_launch_attempt_count__gt: int = None,
        location_launch_attempt_count__gte: int = None,
        location_launch_attempt_count__lt: int = None,
        location_launch_attempt_count__lte: int = None,
        location_launch_attempt_count_year: int = None,
        location_launch_attempt_count_year__gt: int = None,
        location_launch_attempt_count_year__gte: int = None,
        location_launch_attempt_count_year__lt: int = None,
        location_launch_attempt_count_year__lte: int = None,
        lsp__id: List[int] = None,
        lsp__name: List[str] = None,
        mission__orbit__celestial_body__id: int = None,
        mission__orbit__name: str = None,
        mission__orbit__name__icontains: str = None,
        month: List[float] = None,
        name: str = None,
        net__gt: str = None,
        net__gte: str = None,
        net__lt: str = None,
        net__lte: str = None,
        offset: int = None,
        orbital_launch_attempt_count: int = None,
        orbital_launch_attempt_count__gt: int = None,
        orbital_launch_attempt_count__gte: int = None,
        orbital_launch_attempt_count__lt: int = None,
        orbital_launch_attempt_count__lte: int = None,
        orbital_launch_attempt_count_year: int = None,
        orbital_launch_attempt_count_year__gt: int = None,
        orbital_launch_attempt_count_year__gte: int = None,
        orbital_launch_attempt_count_year__lt: int = None,
        orbital_launch_attempt_count_year__lte: int = None,
        ordering: str = None,
        pad: int = None,
        pad__location: int = None,
        pad__location__celestial_body__id: int = None,
        pad_launch_attempt_count: int = None,
        pad_launch_attempt_count__gt: int = None,
        pad_launch_attempt_count__gte: int = None,
        pad_launch_attempt_count__lt: int = None,
        pad_launch_attempt_count__lte: int = None,
        pad_launch_attempt_count_year: int = None,
        pad_launch_attempt_count_year__gt: int = None,
        pad_launch_attempt_count_year__gte: int = None,
        pad_launch_attempt_count_year__lt: int = None,
        pad_launch_attempt_count_year__lte: int = None,
        program: List[int] = None,
        related_lsp__id: List[int] = None,
        related_lsp__name: List[str] = None,
        rocket__configuration__full_name: str = None,
        rocket__configuration__full_name__icontains: str = None,
        rocket__configuration__id: int = None,
        rocket__configuration__manufacturer__name: str = None,
        rocket__configuration__manufacturer__name__icontains: str = None,
        rocket__configuration__name: str = None,
        rocket__spacecraftflight__spacecraft__id: int = None,
        rocket__spacecraftflight__spacecraft__name: str = None,
        rocket__spacecraftflight__spacecraft__name__icontains: str = None,
        search: str = None,
        serial_number: List[str] = None,
        slug: str = None,
        spacecraft_config__ids: List[int] = None,
        status: int = None,
        status__ids: List[int] = None,
        video_url: List[str] = None,
        window_end__gt: str = None,
        window_end__gte: str = None,
        window_end__lt: str = None,
        window_end__lte: str = None,
        window_start__gt: str = None,
        window_start__gte: str = None,
        window_start__lt: str = None,
        window_start__lte: str = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicLaunchEndpointList:
        params = {
            "agency_launch_attempt_count": agency_launch_attempt_count,
            "agency_launch_attempt_count__gt": agency_launch_attempt_count__gt,
            "agency_launch_attempt_count__gte": agency_launch_attempt_count__gte,
            "agency_launch_attempt_count__lt": agency_launch_attempt_count__lt,
            "agency_launch_attempt_count__lte": agency_launch_attempt_count__lte,
            "agency_launch_attempt_count_year": agency_launch_attempt_count_year,
            "agency_launch_attempt_count_year__gt": agency_launch_attempt_count_year__gt,
            "agency_launch_attempt_count_year__gte": agency_launch_attempt_count_year__gte,
            "agency_launch_attempt_count_year__lt": agency_launch_attempt_count_year__lt,
            "agency_launch_attempt_count_year__lte": agency_launch_attempt_count_year__lte,
            "day": day,
            "hide_recent_previous": hide_recent_previous,
            "id": id,
            "include_suborbital": include_suborbital,
            "is_crewed": is_crewed,
            "last_updated__gte": last_updated__gte,
            "last_updated__lte": last_updated__lte,
            "launch_designator": launch_designator,
            "launcher_config__id": launcher_config__id,
            "limit": limit,
            "location__ids": location__ids,
            "location_launch_attempt_count": location_launch_attempt_count,
            "location_launch_attempt_count__gt": location_launch_attempt_count__gt,
            "location_launch_attempt_count__gte": location_launch_attempt_count__gte,
            "location_launch_attempt_count__lt": location_launch_attempt_count__lt,
            "location_launch_attempt_count__lte": location_launch_attempt_count__lte,
            "location_launch_attempt_count_year": location_launch_attempt_count_year,
            "location_launch_attempt_count_year__gt": location_launch_attempt_count_year__gt,
            "location_launch_attempt_count_year__gte": location_launch_attempt_count_year__gte,
            "location_launch_attempt_count_year__lt": location_launch_attempt_count_year__lt,
            "location_launch_attempt_count_year__lte": location_launch_attempt_count_year__lte,
            "lsp__id": lsp__id,
            "lsp__name": lsp__name,
            "mission__orbit__celestial_body__id": mission__orbit__celestial_body__id,
            "mission__orbit__name": mission__orbit__name,
            "mission__orbit__name__icontains": mission__orbit__name__icontains,
            "month": month,
            "name": name,
            "net__gt": net__gt,
            "net__gte": net__gte,
            "net__lt": net__lt,
            "net__lte": net__lte,
            "offset": offset,
            "orbital_launch_attempt_count": orbital_launch_attempt_count,
            "orbital_launch_attempt_count__gt": orbital_launch_attempt_count__gt,
            "orbital_launch_attempt_count__gte": orbital_launch_attempt_count__gte,
            "orbital_launch_attempt_count__lt": orbital_launch_attempt_count__lt,
            "orbital_launch_attempt_count__lte": orbital_launch_attempt_count__lte,
            "orbital_launch_attempt_count_year": orbital_launch_attempt_count_year,
            "orbital_launch_attempt_count_year__gt": orbital_launch_attempt_count_year__gt,
            "orbital_launch_attempt_count_year__gte": orbital_launch_attempt_count_year__gte,
            "orbital_launch_attempt_count_year__lt": orbital_launch_attempt_count_year__lt,
            "orbital_launch_attempt_count_year__lte": orbital_launch_attempt_count_year__lte,
            "ordering": ordering,
            "pad": pad,
            "pad__location": pad__location,
            "pad__location__celestial_body__id": pad__location__celestial_body__id,
            "pad_launch_attempt_count": pad_launch_attempt_count,
            "pad_launch_attempt_count__gt": pad_launch_attempt_count__gt,
            "pad_launch_attempt_count__gte": pad_launch_attempt_count__gte,
            "pad_launch_attempt_count__lt": pad_launch_attempt_count__lt,
            "pad_launch_attempt_count__lte": pad_launch_attempt_count__lte,
            "pad_launch_attempt_count_year": pad_launch_attempt_count_year,
            "pad_launch_attempt_count_year__gt": pad_launch_attempt_count_year__gt,
            "pad_launch_attempt_count_year__gte": pad_launch_attempt_count_year__gte,
            "pad_launch_attempt_count_year__lt": pad_launch_attempt_count_year__lt,
            "pad_launch_attempt_count_year__lte": pad_launch_attempt_count_year__lte,
            "program": program,
            "related_lsp__id": related_lsp__id,
            "related_lsp__name": related_lsp__name,
            "rocket__configuration__full_name": rocket__configuration__full_name,
            "rocket__configuration__full_name__icontains": rocket__configuration__full_name__icontains,
            "rocket__configuration__id": rocket__configuration__id,
            "rocket__configuration__manufacturer__name": rocket__configuration__manufacturer__name,
            "rocket__configuration__manufacturer__name__icontains": rocket__configuration__manufacturer__name__icontains,
            "rocket__configuration__name": rocket__configuration__name,
            "rocket__spacecraftflight__spacecraft__id": rocket__spacecraftflight__spacecraft__id,
            "rocket__spacecraftflight__spacecraft__name": rocket__spacecraftflight__spacecraft__name,
            "rocket__spacecraftflight__spacecraft__name__icontains": rocket__spacecraftflight__spacecraft__name__icontains,
            "search": search,
            "serial_number": serial_number,
            "slug": slug,
            "spacecraft_config__ids": spacecraft_config__ids,
            "status": status,
            "status__ids": status__ids,
            "video_url": video_url,
            "window_end__gt": window_end__gt,
            "window_end__gte": window_end__gte,
            "window_end__lt": window_end__lt,
            "window_end__lte": window_end__lte,
            "window_start__gt": window_start__gt,
            "window_start__gte": window_start__gte,
            "window_start__lt": window_start__lt,
            "window_start__lte": window_start__lte,
            "year": year,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/launches/upcoming/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLaunchEndpointList(**response)

    def launches_upcoming_retrieve(self, id: str = None, **kwargs) -> LaunchDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/launches/upcoming/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LaunchDetailed(**response)

    async def launches_upcoming_retrieve_async(
        self, id: str = None, **kwargs
    ) -> LaunchDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/launches/upcoming/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LaunchDetailed(**response)

    def locations_list(
        self,
        country_code: str = None,
        id: int = None,
        limit: int = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        total_landing_count: int = None,
        total_landing_count__gt: int = None,
        total_landing_count__gte: int = None,
        total_landing_count__lt: int = None,
        total_landing_count__lte: int = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicLocationEndpointList:
        params = {
            "country_code": country_code,
            "id": id,
            "limit": limit,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "total_landing_count": total_landing_count,
            "total_landing_count__gt": total_landing_count__gt,
            "total_landing_count__gte": total_landing_count__gte,
            "total_landing_count__lt": total_landing_count__lt,
            "total_landing_count__lte": total_landing_count__lte,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/locations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLocationEndpointList(**response)

    async def locations_list_async(
        self,
        country_code: str = None,
        id: int = None,
        limit: int = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        total_landing_count: int = None,
        total_landing_count__gt: int = None,
        total_landing_count__gte: int = None,
        total_landing_count__lt: int = None,
        total_landing_count__lte: int = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicLocationEndpointList:
        params = {
            "country_code": country_code,
            "id": id,
            "limit": limit,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "total_landing_count": total_landing_count,
            "total_landing_count__gt": total_landing_count__gt,
            "total_landing_count__gte": total_landing_count__gte,
            "total_landing_count__lt": total_landing_count__lt,
            "total_landing_count__lte": total_landing_count__lte,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/locations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicLocationEndpointList(**response)

    def locations_retrieve(
        self, id: int = None, **kwargs
    ) -> LocationSerializerWithPads:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/locations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LocationSerializerWithPads(**response)

    async def locations_retrieve_async(
        self, id: int = None, **kwargs
    ) -> LocationSerializerWithPads:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/locations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return LocationSerializerWithPads(**response)

    def mission_patches_list(
        self,
        agency__id: int = None,
        agency__name: str = None,
        agency__name__contains: str = None,
        id: int = None,
        ids: List[int] = None,
        limit: int = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicMissionPatchEndpointList:
        params = {
            "agency__id": agency__id,
            "agency__name": agency__name,
            "agency__name__contains": agency__name__contains,
            "id": id,
            "ids": ids,
            "limit": limit,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/mission_patches/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicMissionPatchEndpointList(**response)

    async def mission_patches_list_async(
        self,
        agency__id: int = None,
        agency__name: str = None,
        agency__name__contains: str = None,
        id: int = None,
        ids: List[int] = None,
        limit: int = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicMissionPatchEndpointList:
        params = {
            "agency__id": agency__id,
            "agency__name": agency__name,
            "agency__name__contains": agency__name__contains,
            "id": id,
            "ids": ids,
            "limit": limit,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/mission_patches/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicMissionPatchEndpointList(**response)

    def mission_patches_retrieve(
        self, id: int = None, **kwargs
    ) -> MissionPatchDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/mission_patches/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return MissionPatchDetailed(**response)

    async def mission_patches_retrieve_async(
        self, id: int = None, **kwargs
    ) -> MissionPatchDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/mission_patches/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return MissionPatchDetailed(**response)

    def pads_list(
        self,
        agencies_ids: List[int] = None,
        id: int = None,
        id__contains: int = None,
        latitude__gt: float = None,
        latitude__gte: float = None,
        latitude__lt: float = None,
        latitude__lte: float = None,
        limit: int = None,
        location__id: int = None,
        location__name: str = None,
        location__name__contains: str = None,
        longitude__gt: float = None,
        longitude__gte: float = None,
        longitude__lt: float = None,
        longitude__lte: float = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        orbital_launch_attempt_count: int = None,
        orbital_launch_attempt_count__gt: int = None,
        orbital_launch_attempt_count__gte: int = None,
        orbital_launch_attempt_count__lt: int = None,
        orbital_launch_attempt_count__lte: int = None,
        ordering: str = None,
        search: str = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        **kwargs,
    ) -> PaginatedPadList:
        params = {
            "agencies_ids": agencies_ids,
            "id": id,
            "id__contains": id__contains,
            "latitude__gt": latitude__gt,
            "latitude__gte": latitude__gte,
            "latitude__lt": latitude__lt,
            "latitude__lte": latitude__lte,
            "limit": limit,
            "location__id": location__id,
            "location__name": location__name,
            "location__name__contains": location__name__contains,
            "longitude__gt": longitude__gt,
            "longitude__gte": longitude__gte,
            "longitude__lt": longitude__lt,
            "longitude__lte": longitude__lte,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "orbital_launch_attempt_count": orbital_launch_attempt_count,
            "orbital_launch_attempt_count__gt": orbital_launch_attempt_count__gt,
            "orbital_launch_attempt_count__gte": orbital_launch_attempt_count__gte,
            "orbital_launch_attempt_count__lt": orbital_launch_attempt_count__lt,
            "orbital_launch_attempt_count__lte": orbital_launch_attempt_count__lte,
            "ordering": ordering,
            "search": search,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/pads/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPadList(**response)

    async def pads_list_async(
        self,
        agencies_ids: List[int] = None,
        id: int = None,
        id__contains: int = None,
        latitude__gt: float = None,
        latitude__gte: float = None,
        latitude__lt: float = None,
        latitude__lte: float = None,
        limit: int = None,
        location__id: int = None,
        location__name: str = None,
        location__name__contains: str = None,
        longitude__gt: float = None,
        longitude__gte: float = None,
        longitude__lt: float = None,
        longitude__lte: float = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        orbital_launch_attempt_count: int = None,
        orbital_launch_attempt_count__gt: int = None,
        orbital_launch_attempt_count__gte: int = None,
        orbital_launch_attempt_count__lt: int = None,
        orbital_launch_attempt_count__lte: int = None,
        ordering: str = None,
        search: str = None,
        total_launch_count: int = None,
        total_launch_count__gt: int = None,
        total_launch_count__gte: int = None,
        total_launch_count__lt: int = None,
        total_launch_count__lte: int = None,
        **kwargs,
    ) -> PaginatedPadList:
        params = {
            "agencies_ids": agencies_ids,
            "id": id,
            "id__contains": id__contains,
            "latitude__gt": latitude__gt,
            "latitude__gte": latitude__gte,
            "latitude__lt": latitude__lt,
            "latitude__lte": latitude__lte,
            "limit": limit,
            "location__id": location__id,
            "location__name": location__name,
            "location__name__contains": location__name__contains,
            "longitude__gt": longitude__gt,
            "longitude__gte": longitude__gte,
            "longitude__lt": longitude__lt,
            "longitude__lte": longitude__lte,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "orbital_launch_attempt_count": orbital_launch_attempt_count,
            "orbital_launch_attempt_count__gt": orbital_launch_attempt_count__gt,
            "orbital_launch_attempt_count__gte": orbital_launch_attempt_count__gte,
            "orbital_launch_attempt_count__lt": orbital_launch_attempt_count__lt,
            "orbital_launch_attempt_count__lte": orbital_launch_attempt_count__lte,
            "ordering": ordering,
            "search": search,
            "total_launch_count": total_launch_count,
            "total_launch_count__gt": total_launch_count__gt,
            "total_launch_count__gte": total_launch_count__gte,
            "total_launch_count__lt": total_launch_count__lt,
            "total_launch_count__lte": total_launch_count__lte,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/pads/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPadList(**response)

    def pads_retrieve(self, id: int = None, **kwargs) -> Pad:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/pads/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Pad(**response)

    async def pads_retrieve_async(self, id: int = None, **kwargs) -> Pad:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/pads/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Pad(**response)

    def payload_flights_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        payload: int = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicPayloadFlightEndpointList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "payload": payload,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/payload_flights/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicPayloadFlightEndpointList(**response)

    async def payload_flights_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        payload: int = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicPayloadFlightEndpointList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "payload": payload,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/payload_flights/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicPayloadFlightEndpointList(**response)

    def payload_flights_retrieve(
        self, id: int = None, **kwargs
    ) -> PayloadFlightDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/payload_flights/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PayloadFlightDetailed(**response)

    async def payload_flights_retrieve_async(
        self, id: int = None, **kwargs
    ) -> PayloadFlightDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/payload_flights/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PayloadFlightDetailed(**response)

    def payloads_list(
        self,
        limit: int = None,
        manufacturer__id: int = None,
        manufacturer__name: str = None,
        name: str = None,
        offset: int = None,
        operator: int = None,
        operator__id: int = None,
        operator__name: str = None,
        ordering: str = None,
        program__id: int = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicPayloadEndpointList:
        params = {
            "limit": limit,
            "manufacturer__id": manufacturer__id,
            "manufacturer__name": manufacturer__name,
            "name": name,
            "offset": offset,
            "operator": operator,
            "operator__id": operator__id,
            "operator__name": operator__name,
            "ordering": ordering,
            "program__id": program__id,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/payloads/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicPayloadEndpointList(**response)

    async def payloads_list_async(
        self,
        limit: int = None,
        manufacturer__id: int = None,
        manufacturer__name: str = None,
        name: str = None,
        offset: int = None,
        operator: int = None,
        operator__id: int = None,
        operator__name: str = None,
        ordering: str = None,
        program__id: int = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicPayloadEndpointList:
        params = {
            "limit": limit,
            "manufacturer__id": manufacturer__id,
            "manufacturer__name": manufacturer__name,
            "name": name,
            "offset": offset,
            "operator": operator,
            "operator__id": operator__id,
            "operator__name": operator__name,
            "ordering": ordering,
            "program__id": program__id,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/payloads/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicPayloadEndpointList(**response)

    def payloads_retrieve(self, id: int = None, **kwargs) -> PayloadDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/payloads/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PayloadDetailed(**response)

    async def payloads_retrieve_async(
        self, id: int = None, **kwargs
    ) -> PayloadDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/payloads/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PayloadDetailed(**response)

    def programs_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicProgramEndpointList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/programs/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicProgramEndpointList(**response)

    async def programs_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicProgramEndpointList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/programs/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicProgramEndpointList(**response)

    def programs_retrieve(self, id: int = None, **kwargs) -> ProgramNormal:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/programs/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ProgramNormal(**response)

    async def programs_retrieve_async(self, id: int = None, **kwargs) -> ProgramNormal:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/programs/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return ProgramNormal(**response)

    def space_stations_list(
        self,
        docked_vehicles: int = None,
        docked_vehicles__gt: int = None,
        docked_vehicles__gte: int = None,
        docked_vehicles__lt: int = None,
        docked_vehicles__lte: int = None,
        id: int = None,
        limit: int = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        onboard_crew: int = None,
        onboard_crew__gt: int = None,
        onboard_crew__gte: int = None,
        onboard_crew__lt: int = None,
        onboard_crew__lte: int = None,
        orbit: int = None,
        ordering: str = None,
        owner__ids: List[int] = None,
        owners: List[int] = None,
        search: str = None,
        status: int = None,
        status__ids: List[int] = None,
        type: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpaceStationEndpointList:
        params = {
            "docked_vehicles": docked_vehicles,
            "docked_vehicles__gt": docked_vehicles__gt,
            "docked_vehicles__gte": docked_vehicles__gte,
            "docked_vehicles__lt": docked_vehicles__lt,
            "docked_vehicles__lte": docked_vehicles__lte,
            "id": id,
            "limit": limit,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "onboard_crew": onboard_crew,
            "onboard_crew__gt": onboard_crew__gt,
            "onboard_crew__gte": onboard_crew__gte,
            "onboard_crew__lt": onboard_crew__lt,
            "onboard_crew__lte": onboard_crew__lte,
            "orbit": orbit,
            "ordering": ordering,
            "owner__ids": owner__ids,
            "owners": owners,
            "search": search,
            "status": status,
            "status__ids": status__ids,
            "type": type,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/space_stations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpaceStationEndpointList(**response)

    async def space_stations_list_async(
        self,
        docked_vehicles: int = None,
        docked_vehicles__gt: int = None,
        docked_vehicles__gte: int = None,
        docked_vehicles__lt: int = None,
        docked_vehicles__lte: int = None,
        id: int = None,
        limit: int = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        onboard_crew: int = None,
        onboard_crew__gt: int = None,
        onboard_crew__gte: int = None,
        onboard_crew__lt: int = None,
        onboard_crew__lte: int = None,
        orbit: int = None,
        ordering: str = None,
        owner__ids: List[int] = None,
        owners: List[int] = None,
        search: str = None,
        status: int = None,
        status__ids: List[int] = None,
        type: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpaceStationEndpointList:
        params = {
            "docked_vehicles": docked_vehicles,
            "docked_vehicles__gt": docked_vehicles__gt,
            "docked_vehicles__gte": docked_vehicles__gte,
            "docked_vehicles__lt": docked_vehicles__lt,
            "docked_vehicles__lte": docked_vehicles__lte,
            "id": id,
            "limit": limit,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "onboard_crew": onboard_crew,
            "onboard_crew__gt": onboard_crew__gt,
            "onboard_crew__gte": onboard_crew__gte,
            "onboard_crew__lt": onboard_crew__lt,
            "onboard_crew__lte": onboard_crew__lte,
            "orbit": orbit,
            "ordering": ordering,
            "owner__ids": owner__ids,
            "owners": owners,
            "search": search,
            "status": status,
            "status__ids": status__ids,
            "type": type,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/space_stations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpaceStationEndpointList(**response)

    def space_stations_retrieve(
        self, id: int = None, **kwargs
    ) -> SpaceStationDetailedEndpoint:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/space_stations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpaceStationDetailedEndpoint(**response)

    async def space_stations_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpaceStationDetailedEndpoint:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/space_stations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpaceStationDetailedEndpoint(**response)

    def spacecraft_list(
        self,
        in_space: bool = None,
        is_placeholder: bool = None,
        limit: int = None,
        name: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        spacecraft_config: int = None,
        status: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacecraftEndpointList:
        params = {
            "in_space": in_space,
            "is_placeholder": is_placeholder,
            "limit": limit,
            "name": name,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "spacecraft_config": spacecraft_config,
            "status": status,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/spacecraft/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacecraftEndpointList(**response)

    async def spacecraft_list_async(
        self,
        in_space: bool = None,
        is_placeholder: bool = None,
        limit: int = None,
        name: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        spacecraft_config: int = None,
        status: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacecraftEndpointList:
        params = {
            "in_space": in_space,
            "is_placeholder": is_placeholder,
            "limit": limit,
            "name": name,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "spacecraft_config": spacecraft_config,
            "status": status,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/spacecraft/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacecraftEndpointList(**response)

    def spacecraft_retrieve(
        self, id: int = None, **kwargs
    ) -> SpacecraftEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/spacecraft/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftEndpointDetailed(**response)

    async def spacecraft_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpacecraftEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/spacecraft/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftEndpointDetailed(**response)

    def spacecraft_configuration_families_list(
        self,
        limit: int = None,
        manufacturer: int = None,
        name: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacecraftConfigFamilyEndpointList:
        params = {
            "limit": limit,
            "manufacturer": manufacturer,
            "name": name,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/spacecraft_configuration_families/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacecraftConfigFamilyEndpointList(**response)

    async def spacecraft_configuration_families_list_async(
        self,
        limit: int = None,
        manufacturer: int = None,
        name: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacecraftConfigFamilyEndpointList:
        params = {
            "limit": limit,
            "manufacturer": manufacturer,
            "name": name,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/spacecraft_configuration_families/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacecraftConfigFamilyEndpointList(**response)

    def spacecraft_configuration_families_retrieve(
        self, id: int = None, **kwargs
    ) -> SpacecraftConfigFamilyEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/spacecraft_configuration_families/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftConfigFamilyEndpointDetailed(**response)

    async def spacecraft_configuration_families_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpacecraftConfigFamilyEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/spacecraft_configuration_families/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftConfigFamilyEndpointDetailed(**response)

    def spacecraft_configurations_list(
        self,
        agency: int = None,
        human_rated: bool = None,
        in_use: bool = None,
        limit: int = None,
        name: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacecraftConfigurationEndpointList:
        params = {
            "agency": agency,
            "human_rated": human_rated,
            "in_use": in_use,
            "limit": limit,
            "name": name,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/spacecraft_configurations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacecraftConfigurationEndpointList(**response)

    async def spacecraft_configurations_list_async(
        self,
        agency: int = None,
        human_rated: bool = None,
        in_use: bool = None,
        limit: int = None,
        name: str = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacecraftConfigurationEndpointList:
        params = {
            "agency": agency,
            "human_rated": human_rated,
            "in_use": in_use,
            "limit": limit,
            "name": name,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/spacecraft_configurations/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacecraftConfigurationEndpointList(**response)

    def spacecraft_configurations_retrieve(
        self, id: int = None, **kwargs
    ) -> SpacecraftConfigDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/spacecraft_configurations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftConfigDetailed(**response)

    async def spacecraft_configurations_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpacecraftConfigDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/spacecraft_configurations/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftConfigDetailed(**response)

    def spacecraft_flights_list(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        spacecraft: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacecraftFlightEndpointList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "spacecraft": spacecraft,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/spacecraft_flights/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacecraftFlightEndpointList(**response)

    async def spacecraft_flights_list_async(
        self,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        search: str = None,
        spacecraft: int = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacecraftFlightEndpointList:
        params = {
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "search": search,
            "spacecraft": spacecraft,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/spacecraft_flights/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacecraftFlightEndpointList(**response)

    def spacecraft_flights_retrieve(
        self, id: int = None, **kwargs
    ) -> SpacecraftFlightDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/spacecraft_flights/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftFlightDetailed(**response)

    async def spacecraft_flights_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpacecraftFlightDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/spacecraft_flights/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacecraftFlightDetailed(**response)

    def spacewalks_list(
        self,
        astronaut__ids: List[int] = None,
        day: List[float] = None,
        end: str = None,
        end__gt: str = None,
        end__gte: str = None,
        end__lt: str = None,
        end__lte: str = None,
        event__ids: List[int] = None,
        id: int = None,
        ids: List[int] = None,
        launch__ids: List[str] = None,
        limit: int = None,
        month: List[float] = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        owner__ids: List[float] = None,
        program__ids: List[int] = None,
        program__name: str = None,
        program__name__contains: str = None,
        search: str = None,
        spacestation__ids: List[int] = None,
        start__gt: str = None,
        start__gte: str = None,
        start__lt: str = None,
        start__lte: str = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacewalkEndpointList:
        params = {
            "astronaut__ids": astronaut__ids,
            "day": day,
            "end": end,
            "end__gt": end__gt,
            "end__gte": end__gte,
            "end__lt": end__lt,
            "end__lte": end__lte,
            "event__ids": event__ids,
            "id": id,
            "ids": ids,
            "launch__ids": launch__ids,
            "limit": limit,
            "month": month,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "owner__ids": owner__ids,
            "program__ids": program__ids,
            "program__name": program__name,
            "program__name__contains": program__name__contains,
            "search": search,
            "spacestation__ids": spacestation__ids,
            "start__gt": start__gt,
            "start__gte": start__gte,
            "start__lt": start__lt,
            "start__lte": start__lte,
            "year": year,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/spacewalks/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacewalkEndpointList(**response)

    async def spacewalks_list_async(
        self,
        astronaut__ids: List[int] = None,
        day: List[float] = None,
        end: str = None,
        end__gt: str = None,
        end__gte: str = None,
        end__lt: str = None,
        end__lte: str = None,
        event__ids: List[int] = None,
        id: int = None,
        ids: List[int] = None,
        launch__ids: List[str] = None,
        limit: int = None,
        month: List[float] = None,
        name: str = None,
        name__contains: str = None,
        offset: int = None,
        ordering: str = None,
        owner__ids: List[float] = None,
        program__ids: List[int] = None,
        program__name: str = None,
        program__name__contains: str = None,
        search: str = None,
        spacestation__ids: List[int] = None,
        start__gt: str = None,
        start__gte: str = None,
        start__lt: str = None,
        start__lte: str = None,
        year: List[float] = None,
        **kwargs,
    ) -> PaginatedPolymorphicSpacewalkEndpointList:
        params = {
            "astronaut__ids": astronaut__ids,
            "day": day,
            "end": end,
            "end__gt": end__gt,
            "end__gte": end__gte,
            "end__lt": end__lt,
            "end__lte": end__lte,
            "event__ids": event__ids,
            "id": id,
            "ids": ids,
            "launch__ids": launch__ids,
            "limit": limit,
            "month": month,
            "name": name,
            "name__contains": name__contains,
            "offset": offset,
            "ordering": ordering,
            "owner__ids": owner__ids,
            "program__ids": program__ids,
            "program__name": program__name,
            "program__name__contains": program__name__contains,
            "search": search,
            "spacestation__ids": spacestation__ids,
            "start__gt": start__gt,
            "start__gte": start__gte,
            "start__lt": start__lt,
            "start__lte": start__lte,
            "year": year,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/spacewalks/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedPolymorphicSpacewalkEndpointList(**response)

    def spacewalks_retrieve(
        self, id: int = None, **kwargs
    ) -> SpacewalkEndpointDetailed:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/spacewalks/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacewalkEndpointDetailed(**response)

    async def spacewalks_retrieve_async(
        self, id: int = None, **kwargs
    ) -> SpacewalkEndpointDetailed:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/spacewalks/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return SpacewalkEndpointDetailed(**response)

    def updates_list(
        self,
        created_on: str = None,
        launch: str = None,
        launch__launch_service_provider: int = None,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        program: int = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedUpdateList:
        params = {
            "created_on": created_on,
            "launch": launch,
            "launch__launch_service_provider": launch__launch_service_provider,
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "program": program,
            "search": search,
            **kwargs,
        }
        response = self.get(
            f"/2.3.0/updates/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedUpdateList(**response)

    async def updates_list_async(
        self,
        created_on: str = None,
        launch: str = None,
        launch__launch_service_provider: int = None,
        limit: int = None,
        offset: int = None,
        ordering: str = None,
        program: int = None,
        search: str = None,
        **kwargs,
    ) -> PaginatedUpdateList:
        params = {
            "created_on": created_on,
            "launch": launch,
            "launch__launch_service_provider": launch__launch_service_provider,
            "limit": limit,
            "offset": offset,
            "ordering": ordering,
            "program": program,
            "search": search,
            **kwargs,
        }
        response = await self.getAsync(
            f"/2.3.0/updates/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return PaginatedUpdateList(**response)

    def updates_retrieve(self, id: int = None, **kwargs) -> Update:
        params = {**kwargs}
        response = self.get(
            f"/2.3.0/updates/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Update(**response)

    async def updates_retrieve_async(self, id: int = None, **kwargs) -> Update:
        params = {**kwargs}
        response = await self.getAsync(
            f"/2.3.0/updates/{id}/",
            query={k: v for k, v in params.items() if v is not None},
        )
        return Update(**response)
