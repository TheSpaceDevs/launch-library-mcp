from fastmcp import FastMCP
from typing import List, Optional
import yaml
import json

from .launch_library_client import LaunchLibClient

mcp_llv2 = FastMCP("launch-library")

LLV2_BASE_URL = "https://ll.thespacedevs.com/"


@mcp_llv2.tool()
async def launches_list(
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
) -> str:
    """Get weather alerts for a US state.
    All arguments are optional and can be used to filter the results.
    Args:
        agency_launch_attempt_count (int): Filter by agency launch attempt count.
        agency_launch_attempt_count__gt (int): Filter by agency launch attempt count greater than.
        agency_launch_attempt_count__gte (int): Filter by agency launch attempt count greater than or equal to.
        agency_launch_attempt_count__lt (int): Filter by agency launch attempt count less than.
        agency_launch_attempt_count__lte (int): Filter by agency launch attempt count less than or equal to.
        agency_launch_attempt_count_year (int): Filter by agency launch attempt count year.
        agency_launch_attempt_count_year__gt (int): Filter by agency launch attempt count year greater than.
        agency_launch_attempt_count_year__gte (int): Filter by agency launch attempt count year greater than or equal to.
        agency_launch_attempt_count_year__lt (int): Filter by agency launch attempt count year less than.
        agency_launch_attempt_count_year__lte (int): Filter by agency launch attempt count year less than or equal to.
        day (List[float]): List of days to filter launches.
        id (List[str]): List of IDs to filter launches.
        include_suborbital (bool): Include suborbital launches in the results.
        is_crewed (bool): Filter by crewed status.
        last_updated__gte (str): Filter by last updated date greater than or equal to.
        last_updated__lte (str): Filter by last updated date less than or equal to.
        launch_designator (List[str]): List of launch designators to filter launches.
        launcher_config__id (List[int]): List of launcher configuration IDs to filter launches.
        limit (int): Maximum number of results to return.
        location__ids (List[int]): List of location IDs to filter launches.
        location_launch_attempt_count (int): Filter by location launch attempt count.
        location_launch_attempt_count__gt (int): Filter by location launch attempt count greater than.
        location_launch_attempt_count__gte (int): Filter by location launch attempt count greater than or equal to.
        location_launch_attempt_count__lt (int): Filter by location launch attempt count less than.
        location_launch_attempt_count__lte (int): Filter by location launch attempt count less than or equal to.
        location_launch_attempt_count_year (int): Filter by location launch attempt count year.
        location_launch_attempt_count_year__gt (int): Filter by location launch attempt count year greater than.
        location_launch_attempt_count_year__gte (int): Filter by location launch attempt count year greater than or equal to.
        location_launch_attempt_count_year__lt (int): Filter by location launch attempt count year less than.
        location_launch_attempt_count_year__lte (int): Filter by location launch attempt count year less than or equal to.
        lsp__id (List[int]): List of launch service provider IDs to filter launches.
        lsp__name (List[str]): List of launch service provider names to filter launches.
        mission__orbit__celestial_body__id (int): Filter by mission orbit celestial body ID.
        mission__orbit__name (str): Filter by mission orbit name.
        mission__orbit__name__icontains (str): Filter by mission orbit name containing the specified string.
        month (List[float]): List of months to filter launches.
        name (str): Filter by launch name.
        net__gt (str): Filter by net date greater than.
        net__gte (str): Filter by net date greater than or equal to.
        net__lt (str): Filter by net date less than.
        net__lte (str): Filter by net date less than or equal to.
        offset (int): Offset for pagination.
        orbital_launch_attempt_count (int): Filter by orbital launch attempt count.
        orbital_launch_attempt_count__gt (int): Filter by orbital launch attempt count greater than.
        orbital_launch_attempt_count__gte (int): Filter by orbital launch attempt count greater than or equal to.
        orbital_launch_attempt_count__lt (int): Filter by orbital launch attempt count less than.
        orbital_launch_attempt_count__lte (int): Filter by orbital launch attempt count less than or equal to.
        orbital_launch_attempt_count_year (int): Filter by orbital launch attempt count year.
        orbital_launch_attempt_count_year__gt (int): Filter by orbital launch attempt count year greater than.
        orbital_launch_attempt_count_year__gte (int): Filter by orbital launch attempt count year greater than or equal to.
        orbital_launch_attempt_count_year__lt (int): Filter by orbital launch attempt count year less than.
        orbital_launch_attempt_count_year__lte (int): Filter by orbital launch attempt count year less than or equal to.
        pad (int): Filter by pad ID.
        pad__location (int): Filter by pad location ID.
        pad__location__celestial_body__id (int): Filter by pad location celestial body ID.
        pad_launch_attempt_count (int): Filter by pad launch attempt count.
        pad_launch_attempt_count__gt (int): Filter by pad launch attempt count greater than.
        pad_launch_attempt_count__gte (int): Filter by pad launch attempt count greater than or equal to.
        pad_launch_attempt_count__lt (int): Filter by pad launch attempt count less than.
        pad_launch_attempt_count__lte (int): Filter by pad launch attempt count less than or equal to.
        pad_launch_attempt_count_year (int): Filter by pad launch attempt count year.
        pad_launch_attempt_count_year__gt (int): Filter by pad launch attempt count year greater than.
        pad_launch_attempt_count_year__gte (int): Filter by pad launch attempt count year greater than or equal to.
        pad_launch_attempt_count_year__lt (int): Filter by pad launch attempt count year less than.
        pad_launch_attempt_count_year__lte (int): Filter by pad launch attempt count year less than or equal to.
        program (List[int]): List of program IDs to filter launches.
        related_lsp__id (List[int]): List of related launch service provider IDs to filter launches.
        related_lsp__name (List[str]): List of related launch service provider names to filter launches.
        rocket__configuration__full_name (str): Filter by rocket configuration full name.
        rocket__configuration__full_name__icontains (str): Filter by rocket configuration full name containing the specified string.
        search (str): Search term to filter launches.
        serial_number (List[str]): List of serial numbers to filter launches.
        slug (str): Filter by launch slug.
        spacecraft_config__ids (List[int]): List of spacecraft configuration IDs to filter launches.
        status (int): Filter by launch status.
        status__ids (List[int]): List of launch status IDs to filter launches.
        video_url (List[str]): List of video URLs to filter launches.
        window_end__gt (str): Filter by window end date greater than.
        window_end__gte (str): Filter by window end date greater than or equal to.
        window_end__lt (str): Filter by window end date less than.
        window_end__lte (str): Filter by window end date less than or equal to.
        window_start__gt (str): Filter by window start date greater than.
        window_start__gte (str): Filter by window start date greater than or equal to.
        window_start__lt (str): Filter by window start date less than.
        window_start__lte (str): Filter by window start date less than or equal to.
    Returns:
        str: YAML formatted string containing the launch data.
    """
    result = await LaunchLibClient().launches_list_async(
        agency_launch_attempt_count=agency_launch_attempt_count,
        agency_launch_attempt_count__gt=agency_launch_attempt_count__gt,
        agency_launch_attempt_count__gte=agency_launch_attempt_count__gte,
        agency_launch_attempt_count__lt=agency_launch_attempt_count__lt,
        agency_launch_attempt_count__lte=agency_launch_attempt_count__lte,
        agency_launch_attempt_count_year=agency_launch_attempt_count_year,
        agency_launch_attempt_count_year__gt=agency_launch_attempt_count_year__gt,
        agency_launch_attempt_count_year__gte=agency_launch_attempt_count_year__gte,
        agency_launch_attempt_count_year__lt=agency_launch_attempt_count_year__lt,
        agency_launch_attempt_count_year__lte=agency_launch_attempt_count_year__lte,
        day=day,
        id=id,
        include_suborbital=include_suborbital,
        is_crewed=is_crewed,
        last_updated__gte=last_updated__gte,
        last_updated__lte=last_updated__lte,
        launch_designator=launch_designator,
        launcher_config__id=launcher_config__id,
        limit=limit,
        location__ids=location__ids,
        location_launch_attempt_count=location_launch_attempt_count,
        location_launch_attempt_count__gt=location_launch_attempt_count__gt,
        location_launch_attempt_count__gte=location_launch_attempt_count__gte,
        location_launch_attempt_count__lt=location_launch_attempt_count__lt,
        location_launch_attempt_count__lte=location_launch_attempt_count__lte,
        location_launch_attempt_count_year=location_launch_attempt_count_year,
        location_launch_attempt_count_year__gt=location_launch_attempt_count_year__gt,
        location_launch_attempt_count_year__gte=location_launch_attempt_count_year__gte,
        location_launch_attempt_count_year__lt=location_launch_attempt_count_year__lt,
        location_launch_attempt_count_year__lte=location_launch_attempt_count_year__lte,
        lsp__id=lsp__id,
        lsp__name=lsp__name,
        mission__orbit__celestial_body__id=mission__orbit__celestial_body__id,
        mission__orbit__name=mission__orbit__name,
        mission__orbit__name__icontains=mission__orbit__name__icontains,
        month=month,
        name=name,
        net__gt=net__gt,
        net__gte=net__gte,
        net__lt=net__lt,
        net__lte=net__lte,
        offset=offset,
        orbital_launch_attempt_count=orbital_launch_attempt_count,
        orbital_launch_attempt_count__gt=orbital_launch_attempt_count__gt,
        orbital_launch_attempt_count__gte=orbital_launch_attempt_count__gte,
        orbital_launch_attempt_count__lt=orbital_launch_attempt_count__lt,
        orbital_launch_attempt_count__lte=orbital_launch_attempt_count__lte,
        orbital_launch_attempt_count_year=orbital_launch_attempt_count_year,
        orbital_launch_attempt_count_year__gt=orbital_launch_attempt_count_year__gt,
        orbital_launch_attempt_count_year__gte=orbital_launch_attempt_count_year__gte,
        orbital_launch_attempt_count_year__lt=orbital_launch_attempt_count_year__lt,
        orbital_launch_attempt_count_year__lte=orbital_launch_attempt_count_year__lte,
        ordering=ordering,
        pad=pad,
        pad__location=pad__location,
        pad__location__celestial_body__id=pad__location__celestial_body__id,
        pad_launch_attempt_count=pad_launch_attempt_count,
        pad_launch_attempt_count__gt=pad_launch_attempt_count__gt,
        pad_launch_attempt_count__gte=pad_launch_attempt_count__gte,
        pad_launch_attempt_count__lt=pad_launch_attempt_count__lt,
        pad_launch_attempt_count__lte=pad_launch_attempt_count__lte,
        pad_launch_attempt_count_year=pad_launch_attempt_count_year,
        pad_launch_attempt_count_year__gt=pad_launch_attempt_count_year__gt,
        pad_launch_attempt_count_year__gte=pad_launch_attempt_count_year__gte,
        pad_launch_attempt_count_year__lt=pad_launch_attempt_count_year__lt,
        pad_launch_attempt_count_year__lte=pad_launch_attempt_count_year__lte,
        program=program,
        related_lsp__id=related_lsp__id,
        related_lsp__name=related_lsp__name,
        rocket__configuration__full_name=rocket__configuration__full_name,
        rocket__configuration__full_name__icontains=rocket__configuration__full_name__icontains,
        rocket__configuration__id=rocket__configuration__id,
        rocket__configuration__manufacturer__name=rocket__configuration__manufacturer__name,
        rocket__configuration__manufacturer__name__icontains=rocket__configuration__manufacturer__name__icontains,
        rocket__configuration__name=rocket__configuration__name,
        rocket__spacecraftflight__spacecraft__id=rocket__spacecraftflight__spacecraft__id,
        rocket__spacecraftflight__spacecraft__name=rocket__spacecraftflight__spacecraft__name,
        rocket__spacecraftflight__spacecraft__name__icontains=rocket__spacecraftflight__spacecraft__name__icontains,
        search=search,
        serial_number=serial_number,
        slug=slug,
        spacecraft_config__ids=spacecraft_config__ids,
        status=status,
        status__ids=status__ids,
        video_url=video_url,
        window_end__gt=window_end__gt,
        window_end__gte=window_end__gte,
        window_end__lt=window_end__lt,
        window_end__lte=window_end__lte,
        window_start__gt=window_start__gt,
        window_start__gte=window_start__gte,
        window_start__lt=window_start__lt,
        window_start__lte=window_start__lte,
    )
    items = []
    for x in result.results:
        items.append(
            {
                "id": x.id,
                "net": f"{x.net} presision: {x.net_precision.name}",
                "name": x.name,
                "slug": x.slug,
                "status": x.status.abbrev,
                "rocket": x.rocket.configuration.full_name,
                "orbit": x.mission.orbit.abbrev,
                "provider": x.launch_service_provider.name,
                "location": x.pad.location.name,
                "launch_designator": x.launch_designator,
                "window": (
                    f"{x.window_start} -{x.window_end}"
                    if x.window_start and x.window_end
                    else None
                ),
            }
        )
    return yaml.dump(
        {
            "count": result.count,
            "next": result.next,
            "previous": result.previous,
            "launches": items,
        },
        allow_unicode=True,
        sort_keys=False,
    )


@mcp_llv2.tool()
async def launches_detailed(
    id: Optional[str] = None,
):
    """Get detailed information about a specific launch by ID.
    Args:
        id (str): The ID of the launch to retrieve.
    Returns:
        str: JSON formatted string containing the detailed launch data.
    """
    result = await LaunchLibClient().launches_retrieve_async(id=id)
    return json.dumps(result.model_dump())
