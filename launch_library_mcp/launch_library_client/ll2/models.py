from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Union, List


class VidURLs(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    url: Optional[str] = None


class VidURLType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class Language(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    code: Optional[str] = None


class VidURL(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    priority: Optional[int] = None
    source: Optional[str] = None
    publisher: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    feature_image: Optional[str] = None
    url: Optional[str] = None
    type: Optional[Union[VidURLType]] = None
    language: Optional[Union[Language]] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    live: Optional[bool] = None


class Update(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    profile_image: Optional[str] = None
    comment: Optional[str] = None
    info_url: Optional[str] = None
    created_by: Optional[str] = None
    created_on: Optional[str] = None


class TimelineEventType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    abbrev: Optional[str] = None
    description: Optional[str] = None


class TimelineEvent(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    type: Optional[Union[TimelineEventType]] = None
    relative_time: Optional[str] = None


class SpacecraftStatus(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class SpacecraftConfigType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class SpacecraftConfigFamilyMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    name: Optional[str] = None


class AgencyType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class AgencyMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    abbrev: Optional[str] = None
    type: Optional[AgencyType] = None


class SpacecraftConfigFamilyNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    manufacturer: Optional[Union[AgencyMini]] = None
    parent: Optional[Union[SpacecraftConfigFamilyMini]] = None
    maiden_flight: Optional[str] = None


class ImageVariantType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class ImageVariant(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    type: Optional[ImageVariantType] = None
    image_url: Optional[str] = None


class ImageLicense(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    link: Optional[str] = None


class Image(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    image_url: Optional[str] = None
    thumbnail_url: Optional[str] = None
    credit: Optional[str] = None
    license: Optional[ImageLicense] = None
    single_use: Optional[bool] = None
    variants: Optional[List[ImageVariant]] = None


class SpacecraftConfigNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    type: Optional[SpacecraftConfigType] = None
    agency: Optional[AgencyMini] = None
    family: Optional[List[SpacecraftConfigFamilyNormal]] = None
    in_use: Optional[bool] = None
    image: Optional[Union[Image]] = None


class SpacecraftNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    serial_number: Optional[str] = None
    is_placeholder: Optional[bool] = None
    image: Optional[Union[Image]] = None
    in_space: Optional[bool] = None
    time_in_space: Optional[str] = None
    time_docked: Optional[str] = None
    flights_count: Optional[int] = None
    mission_ends_count: Optional[int] = None
    status: Optional[SpacecraftStatus] = None
    description: Optional[str] = None
    spacecraft_config: Optional[SpacecraftConfigNormal] = None
    fastest_turnaround: Optional[str] = None


class SocialMedia(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    url: Optional[str] = None
    logo: Optional[Union[Image]] = None


class SocialMediaLink(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    social_media: Optional[SocialMedia] = None
    url: Optional[str] = None


class LauncherConfigFamilyMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    name: Optional[str] = None


class LauncherConfigList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    families: Optional[List[LauncherConfigFamilyMini]] = None
    full_name: Optional[str] = None
    variant: Optional[str] = None


class RocketNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    configuration: Optional[LauncherConfigList] = None


class RoadClosureStatus(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class RoadClosure(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    title: Optional[str] = None
    status: Optional[RoadClosureStatus] = None
    window_start: Optional[str] = None
    window_end: Optional[str] = None


class ProgramType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class MissionPatch(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    image_url: Optional[str] = None
    agency: Optional[Union[AgencyMini]] = None
    response_mode: Optional[str] = Field(default="normal")


class ProgramNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None
    description: Optional[str] = None
    agencies: Optional[List[AgencyMini]] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    mission_patches: Optional[List[MissionPatch]] = None
    type: Optional[ProgramType] = None


class Country(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    alpha_2_code: Optional[str] = None
    alpha_3_code: Optional[str] = None
    nationality_name: Optional[str] = None
    nationality_name_composed: Optional[str] = None


class CelestialBodyType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class CelestialBodyDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[CelestialBodyType] = None
    diameter: Optional[float] = None
    mass: Optional[float] = None
    gravity: Optional[float] = None
    length_of_day: Optional[str] = None
    atmosphere: Optional[bool] = None
    image: Optional[Image] = None
    description: Optional[str] = None
    wiki_url: Optional[str] = None
    total_attempted_launches: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    total_attempted_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None


class Location(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    celestial_body: Optional[CelestialBodyDetailed] = None
    active: Optional[bool] = None
    country: Optional[Union[Country]] = None
    description: Optional[str] = None
    image: Optional[Union[Image]] = None
    map_image: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    timezone_name: Optional[str] = None
    total_launch_count: Optional[int] = None
    total_landing_count: Optional[int] = None


class AgencyNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    abbrev: Optional[str] = None
    type: Optional[AgencyType] = None
    featured: Optional[bool] = None
    country: Optional[List[Country]] = None
    description: Optional[str] = None
    administrator: Optional[str] = None
    founding_year: Optional[int] = None
    launchers: Optional[str] = None
    spacecraft: Optional[str] = None
    parent: Optional[str] = None
    image: Optional[Union[Image]] = None
    logo: Optional[Union[Image]] = None
    social_logo: Optional[Union[Image]] = None


class Pad(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    active: Optional[bool] = None
    agencies: Optional[List[AgencyNormal]] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None
    description: Optional[str] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None
    map_url: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    country: Optional[Union[Country]] = None
    map_image: Optional[str] = None
    total_launch_count: Optional[int] = None
    orbital_launch_attempt_count: Optional[int] = None
    fastest_turnaround: Optional[str] = None
    location: Optional[Union[Location]] = None


class CelestialBodyMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    name: Optional[str] = None


class Orbit(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    abbrev: Optional[str] = None
    celestial_body: Optional[CelestialBodyMini] = None


class NoticeType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class Notice(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    type: Optional[NoticeType] = None
    date: Optional[str] = None
    url: Optional[str] = None


class NetPrecision(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    abbrev: Optional[str] = None
    description: Optional[str] = None


class InfoURLType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class InfoURL(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    priority: Optional[int] = None
    source: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    feature_image: Optional[str] = None
    url: Optional[str] = None
    type: Optional[Union[InfoURLType]] = None
    language: Optional[Union[Language]] = None


class AgencyDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    abbrev: Optional[str] = None
    type: Optional[AgencyType] = None
    featured: Optional[bool] = None
    country: Optional[List[Country]] = None
    description: Optional[str] = None
    administrator: Optional[str] = None
    founding_year: Optional[int] = None
    launchers: Optional[str] = None
    spacecraft: Optional[str] = None
    parent: Optional[str] = None
    image: Optional[Union[Image]] = None
    logo: Optional[Union[Image]] = None
    social_logo: Optional[Union[Image]] = None
    total_launch_count: Optional[int] = None
    consecutive_successful_launches: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    pending_launches: Optional[int] = None
    consecutive_successful_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    attempted_landings: Optional[int] = None
    successful_landings_spacecraft: Optional[int] = None
    failed_landings_spacecraft: Optional[int] = None
    attempted_landings_spacecraft: Optional[int] = None
    successful_landings_payload: Optional[int] = None
    failed_landings_payload: Optional[int] = None
    attempted_landings_payload: Optional[int] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None
    social_media_links: Optional[List[SocialMediaLink]] = None


class Mission(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    image: Optional[Union[Image]] = None
    orbit: Optional[Orbit] = None
    agencies: Optional[List[AgencyDetailed]] = None
    info_urls: Optional[List[InfoURL]] = None
    vid_urls: Optional[List[VidURL]] = None


class LauncherStatus(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class LauncherDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    flight_proven: Optional[bool] = None
    serial_number: Optional[str] = None
    is_placeholder: Optional[bool] = None
    status: Optional[Union[LauncherStatus]] = None
    image: Optional[Union[Image]] = None
    details: Optional[str] = None
    successful_landings: Optional[int] = None
    attempted_landings: Optional[int] = None
    flights: Optional[int] = None
    last_launch_date: Optional[str] = None
    first_launch_date: Optional[str] = None
    fastest_turnaround: Optional[str] = None
    launcher_config: Optional[Union[LauncherConfigList]] = None


class LaunchStatus(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    abbrev: Optional[str] = None
    description: Optional[str] = None


class LaunchNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[str] = None
    url: Optional[str] = None
    name: Optional[str] = None
    response_mode: Optional[str] = Field(default="normal")
    slug: Optional[str] = None
    launch_designator: Optional[str] = None
    status: Optional[Union[LaunchStatus]] = None
    last_updated: Optional[str] = None
    net: Optional[str] = None
    net_precision: Optional[Union[NetPrecision]] = None
    window_end: Optional[str] = None
    window_start: Optional[str] = None
    image: Optional[Union[Image]] = None
    infographic: Optional[str] = None
    probability: Optional[int] = None
    weather_concerns: Optional[str] = None
    failreason: Optional[str] = None
    hashtag: Optional[str] = None
    launch_service_provider: Optional[AgencyMini] = None
    rocket: Optional[Union[RocketNormal]] = None
    mission: Optional[Union[Mission]] = None
    pad: Optional[Union[Pad]] = None
    webcast_live: Optional[bool] = None
    program: Optional[List[ProgramNormal]] = None
    orbital_launch_attempt_count: Optional[int] = None
    location_launch_attempt_count: Optional[int] = None
    pad_launch_attempt_count: Optional[int] = None
    agency_launch_attempt_count: Optional[int] = None
    orbital_launch_attempt_count_year: Optional[int] = None
    location_launch_attempt_count_year: Optional[int] = None
    pad_launch_attempt_count_year: Optional[int] = None
    agency_launch_attempt_count_year: Optional[int] = None


class EventType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class EventNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    info_urls: Optional[List[InfoURL]] = None
    vid_urls: Optional[List[VidURL]] = None
    image: Optional[Union[Image]] = None
    date: Optional[str] = None
    slug: Optional[str] = None
    type: Optional[EventType] = None
    description: Optional[str] = None
    webcast_live: Optional[bool] = None
    location: Optional[str] = None
    date_precision: Optional[Union[NetPrecision]] = None


class LaunchAndEventsNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    launches: Optional[List[LaunchNormal]] = None
    events: Optional[List[EventNormal]] = None


class StarshipDashboardNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    updates: Optional[List[Update]] = None
    live_streams: Optional[List[VidURLs]] = None
    road_closures: Optional[List[RoadClosure]] = None
    notices: Optional[List[Notice]] = None
    vehicles: Optional[List[LauncherDetailed]] = None
    orbiters: Optional[List[SpacecraftNormal]] = None
    upcoming: Optional[LaunchAndEventsNormal] = None
    previous: Optional[LaunchAndEventsNormal] = None


class LaunchBasic(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[str] = None
    url: Optional[str] = None
    name: Optional[str] = None
    response_mode: Optional[str] = Field(default="list")
    slug: Optional[str] = None
    launch_designator: Optional[str] = None
    status: Optional[Union[LaunchStatus]] = None
    last_updated: Optional[str] = None
    net: Optional[str] = None
    net_precision: Optional[Union[NetPrecision]] = None
    window_end: Optional[str] = None
    window_start: Optional[str] = None
    image: Optional[Union[Image]] = None
    infographic: Optional[str] = None


class EventEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    info_urls: Optional[List[InfoURL]] = None
    vid_urls: Optional[List[VidURL]] = None
    image: Optional[Union[Image]] = None
    date: Optional[str] = None
    slug: Optional[str] = None
    type: Optional[EventType] = None
    description: Optional[str] = None
    webcast_live: Optional[bool] = None
    location: Optional[str] = None
    date_precision: Optional[Union[NetPrecision]] = None
    response_mode: Optional[str] = Field(default="list")
    duration: Optional[str] = None


class LaunchAndEventsList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    launches: Optional[List[LaunchBasic]] = None
    events: Optional[List[EventEndpointList]] = None


class StarshipDashboardList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    updates: Optional[List[Update]] = None
    live_streams: Optional[List[VidURLs]] = None
    road_closures: Optional[List[RoadClosure]] = None
    notices: Optional[List[Notice]] = None
    vehicles: Optional[List[LauncherDetailed]] = None
    orbiters: Optional[List[SpacecraftNormal]] = None
    upcoming: Optional[LaunchAndEventsList] = None
    previous: Optional[LaunchAndEventsList] = None


class LocationSerializerNoCelestialBody(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    active: Optional[bool] = None
    country: Optional[Union[Country]] = None
    description: Optional[str] = None
    image: Optional[Union[Image]] = None
    map_image: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    timezone_name: Optional[str] = None
    total_launch_count: Optional[int] = None
    total_landing_count: Optional[int] = None


class LandingType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    abbrev: Optional[str] = None
    description: Optional[str] = None


class CelestialBodyNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[CelestialBodyType] = None
    diameter: Optional[float] = None
    mass: Optional[float] = None
    gravity: Optional[float] = None
    length_of_day: Optional[str] = None
    atmosphere: Optional[bool] = None
    image: Optional[Image] = None
    description: Optional[str] = None
    wiki_url: Optional[str] = None


class LandingLocation(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    active: Optional[bool] = None
    abbrev: Optional[str] = None
    description: Optional[str] = None
    location: Optional[LocationSerializerNoCelestialBody] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    image: Optional[Union[Image]] = None
    successful_landings: Optional[int] = None
    attempted_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    celestial_body: Optional[CelestialBodyNormal] = None


class Landing(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    attempt: Optional[bool] = None
    success: Optional[bool] = None
    description: Optional[str] = None
    downrange_distance: Optional[float] = None
    landing_location: Optional[LandingLocation] = None
    type: Optional[LandingType] = None


class SpacecraftFlightNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    mission_end: Optional[str] = None
    spacecraft: Optional[SpacecraftNormal] = None
    launch: Optional[LaunchNormal] = None
    landing: Optional[Landing] = None
    duration: Optional[str] = None
    turn_around_time: Optional[str] = None
    response_mode: Optional[str] = Field(default="normal")


class SpacecraftConfigFamilyDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    manufacturer: Optional[AgencyNormal] = None
    parent: Optional[Union[SpacecraftConfigFamilyNormal]] = None
    maiden_flight: Optional[str] = None
    spacecraft_flown: Optional[int] = None
    total_launch_count: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    attempted_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None


class SpacecraftConfigDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    type: Optional[SpacecraftConfigType] = None
    agency: Optional[AgencyNormal] = None
    family: Optional[List[SpacecraftConfigFamilyDetailed]] = None
    in_use: Optional[bool] = None
    image: Optional[Union[Image]] = None
    capability: Optional[str] = None
    history: Optional[str] = None
    details: Optional[str] = None
    maiden_flight: Optional[str] = None
    height: Optional[float] = None
    diameter: Optional[float] = None
    human_rated: Optional[bool] = None
    crew_capacity: Optional[int] = None
    payload_capacity: Optional[int] = None
    payload_return_capacity: Optional[int] = None
    flight_life: Optional[str] = None
    wiki_link: Optional[str] = None
    info_link: Optional[str] = None
    spacecraft_flown: Optional[int] = None
    total_launch_count: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    attempted_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    fastest_turnaround: Optional[str] = None


class SpacecraftDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    serial_number: Optional[str] = None
    is_placeholder: Optional[bool] = None
    image: Optional[Union[Image]] = None
    in_space: Optional[bool] = None
    time_in_space: Optional[str] = None
    time_docked: Optional[str] = None
    flights_count: Optional[int] = None
    mission_ends_count: Optional[int] = None
    status: Optional[SpacecraftStatus] = None
    description: Optional[str] = None
    spacecraft_config: Optional[SpacecraftConfigDetailed] = None
    fastest_turnaround: Optional[str] = None


class SpaceStationType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class SpaceStationStatus(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class SpaceStationNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None
    status: Optional[SpaceStationStatus] = None
    founded: Optional[str] = None
    deorbited: Optional[str] = None
    description: Optional[str] = None
    orbit: Optional[str] = None
    type: Optional[SpaceStationType] = None


class SpaceStationMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None


class ProgramMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None


class PayloadType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class PayloadNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[PayloadType] = None
    manufacturer: Optional[AgencyNormal] = None
    operator: Optional[AgencyNormal] = None
    image: Optional[Union[Image]] = None
    wiki_link: Optional[str] = None
    info_link: Optional[str] = None
    program: Optional[List[ProgramMini]] = None
    cost: Optional[int] = None
    mass: Optional[float] = None
    description: Optional[str] = None


class PayloadMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[PayloadType] = None
    manufacturer: Optional[AgencyMini] = None
    operator: Optional[AgencyMini] = None
    image: Optional[Union[Image]] = None


class PayloadFlightNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[int] = None
    payload: Optional[PayloadNormal] = None
    launch: Optional[LaunchNormal] = None
    landing: Optional[Landing] = None


class DockingLocation(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    spacestation: Optional[SpaceStationMini] = None
    spacecraft: Optional[SpacecraftConfigNormal] = None
    payload: Optional[PayloadMini] = None


class DockingEventForChaserNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    docking: Optional[str] = None
    departure: Optional[str] = None
    docking_location: Optional[DockingLocation] = None
    space_station_target: Optional[SpaceStationNormal] = None
    flight_vehicle_target: Optional[SpacecraftFlightNormal] = None
    payload_flight_target: Optional[PayloadFlightNormal] = None


class AstronautType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class AstronautStatus(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class AstronautRole(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    role: Optional[str] = None
    priority: Optional[int] = None


class AstronautDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    status: Optional[AstronautStatus] = None
    agency: Optional[Union[AgencyMini]] = None
    image: Optional[Union[Image]] = None
    response_mode: Optional[str] = Field(default="list")
    type: Optional[AstronautType] = None
    in_space: Optional[bool] = None
    time_in_space: Optional[str] = None
    eva_time: Optional[str] = None
    age: Optional[int] = None
    date_of_birth: Optional[str] = None
    date_of_death: Optional[str] = None
    nationality: Optional[List[Country]] = None
    bio: Optional[str] = None
    wiki: Optional[str] = None
    last_flight: Optional[str] = None
    first_flight: Optional[str] = None
    social_media_links: Optional[List[SocialMediaLink]] = None


class AstronautFlight(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    role: Optional[AstronautRole] = None
    astronaut: Optional[AstronautDetailed] = None


class SpacecraftFlightDetailedSerializerNoLaunch(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    mission_end: Optional[str] = None
    spacecraft: Optional[SpacecraftDetailed] = None
    landing: Optional[Landing] = None
    duration: Optional[str] = None
    turn_around_time: Optional[str] = None
    response_mode: Optional[str] = Field(default="detailed")
    launch_crew: Optional[List[AstronautFlight]] = None
    onboard_crew: Optional[List[AstronautFlight]] = None
    landing_crew: Optional[List[AstronautFlight]] = None
    docking_events: Optional[List[DockingEventForChaserNormal]] = None


class PayloadDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[PayloadType] = None
    manufacturer: Optional[AgencyDetailed] = None
    operator: Optional[AgencyDetailed] = None
    image: Optional[Union[Image]] = None
    wiki_link: Optional[str] = None
    info_link: Optional[str] = None
    program: Optional[List[ProgramNormal]] = None
    cost: Optional[int] = None
    mass: Optional[float] = None
    description: Optional[str] = None


class PayloadFlightSerializerNoLaunch(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[int] = None
    payload: Optional[PayloadDetailed] = None
    landing: Optional[Landing] = None
    docking_events: Optional[List[DockingEventForChaserNormal]] = None


class LauncherNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    flight_proven: Optional[bool] = None
    serial_number: Optional[str] = None
    is_placeholder: Optional[bool] = None
    status: Optional[Union[LauncherStatus]] = None
    image: Optional[Union[Image]] = None
    details: Optional[str] = None
    successful_landings: Optional[int] = None
    attempted_landings: Optional[int] = None
    flights: Optional[int] = None
    last_launch_date: Optional[str] = None
    first_launch_date: Optional[str] = None
    fastest_turnaround: Optional[str] = None


class LauncherConfigFamilyNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    name: Optional[str] = None
    manufacturer: Optional[List[AgencyNormal]] = None
    parent: Optional[Union[LauncherConfigFamilyMini]] = None


class LauncherConfigFamilyDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    name: Optional[str] = None
    manufacturer: Optional[List[AgencyDetailed]] = None
    parent: Optional[Union[LauncherConfigFamilyNormal]] = None
    description: Optional[str] = None
    active: Optional[bool] = None
    maiden_flight: Optional[str] = None
    total_launch_count: Optional[int] = None
    consecutive_successful_launches: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    pending_launches: Optional[int] = None
    attempted_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    consecutive_successful_landings: Optional[int] = None


class LauncherConfigDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    families: Optional[List[LauncherConfigFamilyDetailed]] = None
    full_name: Optional[str] = None
    variant: Optional[str] = None
    active: Optional[bool] = None
    is_placeholder: Optional[bool] = None
    manufacturer: Optional[Union[AgencyDetailed]] = None
    program: Optional[List[ProgramNormal]] = None
    reusable: Optional[bool] = None
    image: Optional[Union[Image]] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None
    description: Optional[str] = None
    alias: Optional[str] = None
    min_stage: Optional[int] = None
    max_stage: Optional[int] = None
    length: Optional[float] = None
    diameter: Optional[float] = None
    maiden_flight: Optional[str] = None
    launch_cost: Optional[int] = None
    launch_mass: Optional[float] = None
    leo_capacity: Optional[float] = None
    gto_capacity: Optional[float] = None
    geo_capacity: Optional[float] = None
    sso_capacity: Optional[float] = None
    to_thrust: Optional[float] = None
    apogee: Optional[float] = None
    total_launch_count: Optional[int] = None
    consecutive_successful_launches: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    pending_launches: Optional[int] = None
    attempted_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    consecutive_successful_landings: Optional[int] = None
    fastest_turnaround: Optional[str] = None


class LaunchMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[str] = None
    url: Optional[str] = None
    name: Optional[str] = None


class FirstStageNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    type: Optional[str] = None
    reused: Optional[bool] = None
    launcher_flight_number: Optional[int] = None
    launcher: Optional[LauncherNormal] = None
    previous_flight_date: Optional[str] = None
    turn_around_time: Optional[str] = None
    landing: Optional[Landing] = None
    previous_flight: Optional[LaunchMini] = None


class RocketDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    configuration: Optional[LauncherConfigDetailed] = None
    launcher_stage: Optional[List[FirstStageNormal]] = None
    spacecraft_stage: Optional[List[SpacecraftFlightDetailedSerializerNoLaunch]] = None
    payloads: Optional[List[PayloadFlightSerializerNoLaunch]] = None


class LaunchDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[str] = None
    url: Optional[str] = None
    name: Optional[str] = None
    response_mode: Optional[str] = Field(default="detailed")
    slug: Optional[str] = None
    launch_designator: Optional[str] = None
    status: Optional[Union[LaunchStatus]] = None
    last_updated: Optional[str] = None
    net: Optional[str] = None
    net_precision: Optional[Union[NetPrecision]] = None
    window_end: Optional[str] = None
    window_start: Optional[str] = None
    image: Optional[Union[Image]] = None
    infographic: Optional[str] = None
    probability: Optional[int] = None
    weather_concerns: Optional[str] = None
    failreason: Optional[str] = None
    hashtag: Optional[str] = None
    launch_service_provider: Optional[AgencyDetailed] = None
    rocket: Optional[Union[RocketDetailed]] = None
    mission: Optional[Union[Mission]] = None
    pad: Optional[Union[Pad]] = None
    webcast_live: Optional[bool] = None
    program: Optional[List[ProgramNormal]] = None
    orbital_launch_attempt_count: Optional[int] = None
    location_launch_attempt_count: Optional[int] = None
    pad_launch_attempt_count: Optional[int] = None
    agency_launch_attempt_count: Optional[int] = None
    orbital_launch_attempt_count_year: Optional[int] = None
    location_launch_attempt_count_year: Optional[int] = None
    pad_launch_attempt_count_year: Optional[int] = None
    agency_launch_attempt_count_year: Optional[int] = None
    flightclub_url: Optional[str] = None
    updates: Optional[List[Update]] = None
    info_urls: Optional[List[InfoURL]] = None
    vid_urls: Optional[List[VidURL]] = None
    timeline: Optional[List[TimelineEvent]] = None
    pad_turnaround: Optional[str] = None
    mission_patches: Optional[List[MissionPatch]] = None


class LaunchAndEventsDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    launches: Optional[List[LaunchDetailed]] = None
    events: Optional[List[EventNormal]] = None


class StarshipDashboardDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    updates: Optional[List[Update]] = None
    live_streams: Optional[List[VidURLs]] = None
    road_closures: Optional[List[RoadClosure]] = None
    notices: Optional[List[Notice]] = None
    vehicles: Optional[List[LauncherDetailed]] = None
    orbiters: Optional[List[SpacecraftNormal]] = None
    upcoming: Optional[LaunchAndEventsDetailed] = None
    previous: Optional[LaunchAndEventsDetailed] = None


class SpacewalkNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[str] = None
    location: Optional[str] = None
    crew: Optional[List[AstronautFlight]] = None


class SpacewalkList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[str] = None
    location: Optional[str] = None


class ExpeditionMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None


class EventMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    info_urls: Optional[List[InfoURL]] = None
    vid_urls: Optional[List[VidURL]] = None
    image: Optional[Union[Image]] = None
    date: Optional[str] = None


class SpacewalkEndpointNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[str] = None
    location: Optional[str] = None
    crew: Optional[List[AstronautFlight]] = None
    spacestation: Optional[Union[SpaceStationMini]] = None
    expedition: Optional[Union[ExpeditionMini]] = None
    spacecraft_flight: Optional[Union[SpacecraftFlightNormal]] = None
    event: Optional[Union[EventMini]] = None
    program: Optional[List[ProgramMini]] = None


class SpacecraftFlightDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    mission_end: Optional[str] = None
    spacecraft: Optional[SpacecraftDetailed] = None
    launch: Optional[LaunchNormal] = None
    landing: Optional[Landing] = None
    duration: Optional[str] = None
    turn_around_time: Optional[str] = None
    response_mode: Optional[str] = Field(default="detailed")
    launch_crew: Optional[List[AstronautFlight]] = None
    onboard_crew: Optional[List[AstronautFlight]] = None
    landing_crew: Optional[List[AstronautFlight]] = None
    docking_events: Optional[List[DockingEventForChaserNormal]] = None


class ExpeditionNormalSerializerForSpacewalk(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    spacestation: Optional[SpaceStationNormal] = None
    mission_patches: Optional[List[MissionPatch]] = None


class SpacewalkEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    duration: Optional[str] = None
    location: Optional[str] = None
    crew: Optional[List[AstronautFlight]] = None
    spacestation: Optional[Union[SpaceStationNormal]] = None
    expedition: Optional[Union[ExpeditionNormalSerializerForSpacewalk]] = None
    spacecraft_flight: Optional[Union[SpacecraftFlightDetailed]] = None
    event: Optional[Union[EventNormal]] = None
    program: Optional[List[ProgramNormal]] = None


class SpacecraftFlightNormalSerializerNoLanding(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    mission_end: Optional[str] = None
    spacecraft: Optional[SpacecraftNormal] = None
    launch: Optional[LaunchNormal] = None
    duration: Optional[str] = None
    turn_around_time: Optional[str] = None
    response_mode: Optional[str] = Field(default="normal")


class SpacecraftFlightMiniSerializerNoLanding(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    mission_end: Optional[str] = None
    spacecraft: Optional[SpacecraftNormal] = None
    launch: Optional[LaunchMini] = None
    duration: Optional[str] = None
    turn_around_time: Optional[str] = None


class SpacecraftFlightMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    mission_end: Optional[str] = None
    spacecraft: Optional[SpacecraftNormal] = None
    launch: Optional[LaunchMini] = None
    landing: Optional[Landing] = None
    duration: Optional[str] = None
    turn_around_time: Optional[str] = None


class SpacecraftFlightForDockingEvent(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    spacecraft: Optional[SpacecraftDetailed] = None
    launch: Optional[LaunchNormal] = None


class SpacecraftFlightDetailedSerializerNoLanding(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    mission_end: Optional[str] = None
    spacecraft: Optional[SpacecraftDetailed] = None
    launch: Optional[LaunchNormal] = None
    duration: Optional[str] = None
    turn_around_time: Optional[str] = None
    response_mode: Optional[str] = Field(default="detailed")
    launch_crew: Optional[List[AstronautFlight]] = None
    onboard_crew: Optional[List[AstronautFlight]] = None
    landing_crew: Optional[List[AstronautFlight]] = None
    docking_events: Optional[List[DockingEventForChaserNormal]] = None


class SpacecraftEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    serial_number: Optional[str] = None
    is_placeholder: Optional[bool] = None
    image: Optional[Union[Image]] = None
    in_space: Optional[bool] = None
    time_in_space: Optional[str] = None
    time_docked: Optional[str] = None
    flights_count: Optional[int] = None
    mission_ends_count: Optional[int] = None
    status: Optional[SpacecraftStatus] = None
    description: Optional[str] = None
    spacecraft_config: Optional[SpacecraftConfigDetailed] = None
    fastest_turnaround: Optional[str] = None
    flights: Optional[List[SpacecraftFlightNormal]] = None


class SpacecraftConfigFamilyEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    manufacturer: Optional[AgencyNormal] = None
    parent: Optional[Union[SpacecraftConfigFamilyNormal]] = None
    maiden_flight: Optional[str] = None
    spacecraft_flown: Optional[int] = None
    total_launch_count: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    attempted_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    spacecraft: Optional[List[SpacecraftConfigNormal]] = None


class SpaceStationEndpoint(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None
    status: Optional[SpaceStationStatus] = None
    founded: Optional[str] = None
    deorbited: Optional[str] = None
    description: Optional[str] = None
    orbit: Optional[str] = None
    type: Optional[SpaceStationType] = None
    owners: Optional[List[AgencyNormal]] = None
    response_mode: Optional[str] = Field(default="normal")
    active_expeditions: Optional[List[ExpeditionMini]] = None


class DockingEventDetailedSerializerForSpacestation(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    docking: Optional[str] = None
    departure: Optional[str] = None
    flight_vehicle_chaser: Optional[SpacecraftFlightForDockingEvent] = None
    space_station_chaser: Optional[SpaceStationNormal] = None
    payload_flight_chaser: Optional[PayloadFlightNormal] = None


class DockingLocationSerializerForSpacestation(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    currently_docked: Optional[DockingEventDetailedSerializerForSpacestation] = None


class SpaceStationDetailedEndpoint(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None
    status: Optional[SpaceStationStatus] = None
    founded: Optional[str] = None
    deorbited: Optional[str] = None
    description: Optional[str] = None
    orbit: Optional[str] = None
    type: Optional[SpaceStationType] = None
    owners: Optional[List[AgencyNormal]] = None
    response_mode: Optional[str] = Field(default="detailed")
    active_expeditions: Optional[List[ExpeditionMini]] = None
    height: Optional[float] = None
    width: Optional[float] = None
    mass: Optional[float] = None
    volume: Optional[int] = None
    onboard_crew: Optional[int] = None
    docked_vehicles: Optional[int] = None
    docking_location: Optional[List[DockingLocationSerializerForSpacestation]] = None
    active_docking_events: Optional[List[DockingEventForChaserNormal]] = None


class SpaceStationDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None
    status: Optional[SpaceStationStatus] = None
    founded: Optional[str] = None
    deorbited: Optional[str] = None
    description: Optional[str] = None
    orbit: Optional[str] = None
    type: Optional[SpaceStationType] = None
    owners: Optional[List[AgencyNormal]] = None


PolymorphicStarshipDashboardEndpoint = Optional[
    Union[StarshipDashboardList, StarshipDashboardNormal, StarshipDashboardDetailed]
]


PolymorphicSpacewalkEndpoint = Optional[
    Union[SpacewalkList, SpacewalkEndpointNormal, SpacewalkEndpointDetailed]
]


PolymorphicSpacecraftFlightEndpoint = Optional[
    Union[SpacecraftFlightNormal, SpacecraftFlightDetailed]
]


PolymorphicSpacecraftEndpoint = Optional[
    Union[SpacecraftNormal, SpacecraftEndpointDetailed]
]


PolymorphicSpacecraftConfigurationEndpoint = Optional[
    Union[SpacecraftConfigNormal, SpacecraftConfigDetailed]
]


PolymorphicSpacecraftConfigFamilyEndpoint = Optional[
    Union[
        SpacecraftConfigFamilyMini,
        SpacecraftConfigFamilyNormal,
        SpacecraftConfigFamilyEndpointDetailed,
    ]
]


PolymorphicSpaceStationEndpoint = Optional[
    Union[SpaceStationEndpoint, SpaceStationDetailedEndpoint]
]


PolymorphicProgramEndpoint = Optional[Union[ProgramMini, ProgramNormal]]


class PayloadFlightMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[int] = None
    payload: Optional[PayloadMini] = None
    launch: Optional[LaunchMini] = None
    landing: Optional[Landing] = None


class PayloadFlightDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[int] = None
    payload: Optional[PayloadDetailed] = None
    launch: Optional[LaunchNormal] = None
    landing: Optional[Landing] = None
    docking_events: Optional[List[DockingEventForChaserNormal]] = None


PolymorphicPayloadFlightEndpoint = Optional[
    Union[PayloadFlightMini, PayloadFlightNormal, PayloadFlightDetailed]
]


PolymorphicPayloadEndpoint = Optional[
    Union[PayloadMini, PayloadNormal, PayloadDetailed]
]


class ExpeditionNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    response_mode: Optional[str] = Field(default="normal")
    spacestation: Optional[SpaceStationNormal] = None
    mission_patches: Optional[List[MissionPatch]] = None
    spacewalks: Optional[List[SpacewalkList]] = None


class MissionPatchDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None
    priority: Optional[int] = None
    image_url: Optional[str] = None
    agency: Optional[Union[AgencyDetailed]] = None
    response_mode: Optional[str] = Field(default="detailed")
    launches: Optional[List[LaunchNormal]] = None
    expeditions: Optional[List[ExpeditionNormal]] = None
    program: Optional[List[ProgramNormal]] = None


PolymorphicMissionPatchEndpoint = Optional[Union[MissionPatch, MissionPatchDetailed]]


class PadSerializerNoLocation(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    active: Optional[bool] = None
    agencies: Optional[List[AgencyMini]] = None
    name: Optional[str] = None
    image: Optional[Union[Image]] = None
    description: Optional[str] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None
    map_url: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    country: Optional[Union[Country]] = None
    map_image: Optional[str] = None
    total_launch_count: Optional[int] = None
    orbital_launch_attempt_count: Optional[int] = None
    fastest_turnaround: Optional[str] = None


class LocationSerializerWithPads(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    celestial_body: Optional[CelestialBodyDetailed] = None
    active: Optional[bool] = None
    country: Optional[Union[Country]] = None
    description: Optional[str] = None
    image: Optional[Union[Image]] = None
    map_image: Optional[str] = None
    longitude: Optional[float] = None
    latitude: Optional[float] = None
    timezone_name: Optional[str] = None
    total_launch_count: Optional[int] = None
    total_landing_count: Optional[int] = None
    pads: Optional[List[PadSerializerNoLocation]] = None


PolymorphicLocationEndpoint = Optional[Union[Location, LocationSerializerWithPads]]


class LauncherMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    url: Optional[str] = None
    flight_proven: Optional[bool] = None
    serial_number: Optional[str] = None
    is_placeholder: Optional[bool] = None
    status: Optional[Union[LauncherStatus]] = None
    image: Optional[Union[Image]] = None


PolymorphicLauncherEndpoint = Optional[
    Union[LauncherMini, LauncherNormal, LauncherDetailed]
]


PolymorphicLauncherConfigFamilyEndpoint = Optional[
    Union[
        LauncherConfigFamilyMini,
        LauncherConfigFamilyNormal,
        LauncherConfigFamilyDetailed,
    ]
]


class LauncherConfigNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    families: Optional[List[LauncherConfigFamilyNormal]] = None
    full_name: Optional[str] = None
    variant: Optional[str] = None
    active: Optional[bool] = None
    is_placeholder: Optional[bool] = None
    manufacturer: Optional[Union[AgencyNormal]] = None
    program: Optional[List[ProgramNormal]] = None
    reusable: Optional[bool] = None
    image: Optional[Union[Image]] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None


PolymorphicLauncherConfigEndpoint = Optional[
    Union[LauncherConfigList, LauncherConfigNormal, LauncherConfigDetailed]
]


PolymorphicLaunchEndpoint = Optional[Union[LaunchBasic, LaunchNormal, LaunchDetailed]]


class PayloadFlightNormalSerializerNoLanding(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="normal")
    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[int] = None
    payload: Optional[PayloadNormal] = None
    launch: Optional[LaunchNormal] = None


class PayloadFlightMiniSerializerNoLanding(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="list")
    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[int] = None
    payload: Optional[PayloadMini] = None
    launch: Optional[LaunchMini] = None


class PayloadFlightDetailedSerializerNoLanding(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    destination: Optional[str] = None
    amount: Optional[int] = None
    payload: Optional[PayloadDetailed] = None
    launch: Optional[LaunchNormal] = None
    docking_events: Optional[List[DockingEventForChaserNormal]] = None


class FirstStageNormalSerializerNoLanding(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    type: Optional[str] = None
    reused: Optional[bool] = None
    launcher_flight_number: Optional[int] = None
    launcher: Optional[LauncherNormal] = None
    previous_flight_date: Optional[str] = None
    turn_around_time: Optional[str] = None
    previous_flight: Optional[LaunchMini] = None


class LandingEndpointNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    attempt: Optional[bool] = None
    success: Optional[bool] = None
    description: Optional[str] = None
    downrange_distance: Optional[float] = None
    landing_location: Optional[LandingLocation] = None
    type: Optional[LandingType] = None
    response_mode: Optional[str] = Field(default="normal")
    firststage: Optional[FirstStageNormalSerializerNoLanding] = None
    spacecraftflight: Optional[SpacecraftFlightNormalSerializerNoLanding] = None
    payloadflight: Optional[PayloadFlightNormalSerializerNoLanding] = None


class FirstStageMini(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    type: Optional[str] = None
    reused: Optional[bool] = None
    launcher_flight_number: Optional[int] = None
    launcher: Optional[LauncherMini] = None
    previous_flight_date: Optional[str] = None
    turn_around_time: Optional[str] = None


class LandingEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    attempt: Optional[bool] = None
    success: Optional[bool] = None
    description: Optional[str] = None
    downrange_distance: Optional[float] = None
    landing_location: Optional[LandingLocation] = None
    type: Optional[LandingType] = None
    response_mode: Optional[str] = Field(default="list")
    firststage: Optional[FirstStageMini] = None
    spacecraftflight: Optional[SpacecraftFlightMiniSerializerNoLanding] = None
    payloadflight: Optional[PayloadFlightMiniSerializerNoLanding] = None


class FirstStageDetailedSerializerNoLanding(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    type: Optional[str] = None
    reused: Optional[bool] = None
    launcher_flight_number: Optional[int] = None
    launcher: Optional[LauncherNormal] = None
    previous_flight_date: Optional[str] = None
    turn_around_time: Optional[str] = None
    previous_flight: Optional[LaunchNormal] = None


class LandingEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    attempt: Optional[bool] = None
    success: Optional[bool] = None
    description: Optional[str] = None
    downrange_distance: Optional[float] = None
    landing_location: Optional[LandingLocation] = None
    type: Optional[LandingType] = None
    response_mode: Optional[str] = Field(default="detailed")
    firststage: Optional[FirstStageDetailedSerializerNoLanding] = None
    spacecraftflight: Optional[SpacecraftFlightDetailedSerializerNoLanding] = None
    payloadflight: Optional[PayloadFlightDetailedSerializerNoLanding] = None


PolymorphicLandingEndpoint = Optional[
    Union[LandingEndpointList, LandingEndpointNormal, LandingEndpointDetailed]
]


class ExpeditionDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    response_mode: Optional[str] = Field(default="detailed")
    spacestation: Optional[SpaceStationDetailed] = None
    mission_patches: Optional[List[MissionPatch]] = None
    spacewalks: Optional[List[SpacewalkList]] = None
    crew: Optional[List[AstronautFlight]] = None


PolymorphicExpeditionEndpoint = Optional[Union[ExpeditionNormal, ExpeditionDetailed]]


class EventEndpointNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    info_urls: Optional[List[InfoURL]] = None
    vid_urls: Optional[List[VidURL]] = None
    image: Optional[Union[Image]] = None
    date: Optional[str] = None
    slug: Optional[str] = None
    type: Optional[EventType] = None
    description: Optional[str] = None
    webcast_live: Optional[bool] = None
    location: Optional[str] = None
    date_precision: Optional[Union[NetPrecision]] = None
    response_mode: Optional[str] = Field(default="normal")
    duration: Optional[str] = None
    updates: Optional[List[Update]] = None
    last_updated: Optional[str] = None


class AstronautNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    status: Optional[AstronautStatus] = None
    agency: Optional[Union[AgencyMini]] = None
    image: Optional[Union[Image]] = None


class EventEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    info_urls: Optional[List[InfoURL]] = None
    vid_urls: Optional[List[VidURL]] = None
    image: Optional[Union[Image]] = None
    date: Optional[str] = None
    slug: Optional[str] = None
    type: Optional[EventType] = None
    description: Optional[str] = None
    webcast_live: Optional[bool] = None
    location: Optional[str] = None
    date_precision: Optional[Union[NetPrecision]] = None
    response_mode: Optional[str] = Field(default="detailed")
    duration: Optional[str] = None
    updates: Optional[List[Update]] = None
    last_updated: Optional[str] = None
    agencies: Optional[List[AgencyMini]] = None
    launches: Optional[List[LaunchBasic]] = None
    expeditions: Optional[List[ExpeditionNormal]] = None
    spacestations: Optional[List[SpaceStationNormal]] = None
    program: Optional[List[ProgramNormal]] = None
    astronauts: Optional[List[AstronautNormal]] = None


PolymorphicEventsEndpoint = Optional[
    Union[EventEndpointList, EventEndpointNormal, EventEndpointDetailed]
]


class DockingEventEndpointNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    docking: Optional[str] = None
    departure: Optional[str] = None
    docking_location: Optional[DockingLocation] = None
    space_station_target: Optional[SpaceStationMini] = None
    flight_vehicle_target: Optional[SpacecraftFlightMini] = None
    payload_flight_target: Optional[PayloadFlightMini] = None
    response_mode: Optional[str] = Field(default="normal")
    flight_vehicle_chaser: Optional[SpacecraftFlightMini] = None
    space_station_chaser: Optional[SpaceStationMini] = None
    payload_flight_chaser: Optional[PayloadFlightMini] = None


class DockingEventEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    docking: Optional[str] = None
    departure: Optional[str] = None
    docking_location: Optional[DockingLocation] = None
    space_station_target: Optional[SpaceStationMini] = None
    flight_vehicle_target: Optional[SpacecraftFlightMini] = None
    payload_flight_target: Optional[PayloadFlightMini] = None
    response_mode: Optional[str] = Field(default="detailed")
    flight_vehicle_chaser: Optional[SpacecraftFlightNormal] = None
    space_station_chaser: Optional[SpaceStationNormal] = None
    payload_flight_chaser: Optional[PayloadFlightNormal] = None


PolymorphicDockingEventEndpoint = Optional[
    Union[DockingEventEndpointNormal, DockingEventEndpointDetailed]
]


class CelestialBodyEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[CelestialBodyType] = None
    diameter: Optional[float] = None
    mass: Optional[float] = None
    gravity: Optional[float] = None
    length_of_day: Optional[str] = None
    atmosphere: Optional[bool] = None
    image: Optional[Image] = None
    description: Optional[str] = None
    wiki_url: Optional[str] = None
    total_attempted_launches: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    total_attempted_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    locations: Optional[List[LocationSerializerNoCelestialBody]] = None


PolymorphicCelestialBodyEndpoint = Optional[
    Union[CelestialBodyMini, CelestialBodyNormal, CelestialBodyEndpointDetailed]
]


class AstronautEndpointNormal(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    status: Optional[AstronautStatus] = None
    agency: Optional[Union[AgencyMini]] = None
    image: Optional[Union[Image]] = None
    response_mode: Optional[str] = Field(default="normal")
    type: Optional[AstronautType] = None
    in_space: Optional[bool] = None
    time_in_space: Optional[str] = None
    eva_time: Optional[str] = None
    age: Optional[int] = None
    date_of_birth: Optional[str] = None
    date_of_death: Optional[str] = None
    nationality: Optional[List[Country]] = None
    bio: Optional[str] = None
    wiki: Optional[str] = None
    last_flight: Optional[str] = None
    first_flight: Optional[str] = None
    social_media_links: Optional[List[SocialMediaLink]] = None
    flights_count: Optional[int] = None
    landings_count: Optional[int] = None
    spacewalks_count: Optional[int] = None


class AstronautEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    status: Optional[AstronautStatus] = None
    agency: Optional[Union[AgencyMini]] = None
    image: Optional[Union[Image]] = None
    response_mode: Optional[str] = Field(default="detailed")
    type: Optional[AstronautType] = None
    in_space: Optional[bool] = None
    time_in_space: Optional[str] = None
    eva_time: Optional[str] = None
    age: Optional[int] = None
    date_of_birth: Optional[str] = None
    date_of_death: Optional[str] = None
    nationality: Optional[List[Country]] = None
    bio: Optional[str] = None
    wiki: Optional[str] = None
    last_flight: Optional[str] = None
    first_flight: Optional[str] = None
    social_media_links: Optional[List[SocialMediaLink]] = None
    flights_count: Optional[int] = None
    landings_count: Optional[int] = None
    spacewalks_count: Optional[int] = None
    flights: Optional[List[LaunchNormal]] = None
    landings: Optional[List[SpacecraftFlightNormal]] = None
    spacewalks: Optional[List[SpacewalkNormal]] = None


PolymorphicAstronautEndpoint = Optional[
    Union[AstronautDetailed, AstronautEndpointNormal, AstronautEndpointDetailed]
]


class LauncherConfigDetailedSerializerNoManufacturer(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    families: Optional[List[LauncherConfigFamilyDetailed]] = None
    full_name: Optional[str] = None
    variant: Optional[str] = None
    active: Optional[bool] = None
    is_placeholder: Optional[bool] = None
    program: Optional[List[ProgramNormal]] = None
    reusable: Optional[bool] = None
    image: Optional[Union[Image]] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None
    description: Optional[str] = None
    alias: Optional[str] = None
    min_stage: Optional[int] = None
    max_stage: Optional[int] = None
    length: Optional[float] = None
    diameter: Optional[float] = None
    maiden_flight: Optional[str] = None
    launch_cost: Optional[int] = None
    launch_mass: Optional[float] = None
    leo_capacity: Optional[float] = None
    gto_capacity: Optional[float] = None
    geo_capacity: Optional[float] = None
    sso_capacity: Optional[float] = None
    to_thrust: Optional[float] = None
    apogee: Optional[float] = None
    total_launch_count: Optional[int] = None
    consecutive_successful_launches: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    pending_launches: Optional[int] = None
    attempted_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    consecutive_successful_landings: Optional[int] = None
    fastest_turnaround: Optional[str] = None


class AgencyEndpointDetailed(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    response_mode: Optional[str] = Field(default="detailed")
    id: Optional[int] = None
    url: Optional[str] = None
    name: Optional[str] = None
    abbrev: Optional[str] = None
    type: Optional[AgencyType] = None
    featured: Optional[bool] = None
    country: Optional[List[Country]] = None
    description: Optional[str] = None
    administrator: Optional[str] = None
    founding_year: Optional[int] = None
    launchers: Optional[str] = None
    spacecraft: Optional[str] = None
    parent: Optional[str] = None
    image: Optional[Union[Image]] = None
    logo: Optional[Union[Image]] = None
    social_logo: Optional[Union[Image]] = None
    total_launch_count: Optional[int] = None
    consecutive_successful_launches: Optional[int] = None
    successful_launches: Optional[int] = None
    failed_launches: Optional[int] = None
    pending_launches: Optional[int] = None
    consecutive_successful_landings: Optional[int] = None
    successful_landings: Optional[int] = None
    failed_landings: Optional[int] = None
    attempted_landings: Optional[int] = None
    successful_landings_spacecraft: Optional[int] = None
    failed_landings_spacecraft: Optional[int] = None
    attempted_landings_spacecraft: Optional[int] = None
    successful_landings_payload: Optional[int] = None
    failed_landings_payload: Optional[int] = None
    attempted_landings_payload: Optional[int] = None
    info_url: Optional[str] = None
    wiki_url: Optional[str] = None
    social_media_links: Optional[List[SocialMediaLink]] = None
    launcher_list: Optional[List[LauncherConfigDetailedSerializerNoManufacturer]] = None
    spacecraft_list: Optional[List[SpacecraftConfigDetailed]] = None


PolymorphicAgencyEndpoint = Optional[
    Union[AgencyMini, AgencyNormal, AgencyEndpointDetailed]
]


class PaginatedVidURLTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[VidURLType]] = None


class PaginatedUpdateList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[Update]] = None


class PaginatedTimelineEventTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[TimelineEventType]] = None


class PaginatedSpacecraftStatusList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[SpacecraftStatus]] = None


class PaginatedSpacecraftConfigTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[SpacecraftConfigType]] = None


class PaginatedSpaceStationStatusList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[SpaceStationStatus]] = None


class PaginatedRoadClosureStatusList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[RoadClosureStatus]] = None


class PaginatedProgramTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[ProgramType]] = None


class PaginatedPolymorphicSpacewalkEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicSpacewalkEndpoint]] = None


class PaginatedPolymorphicSpacecraftFlightEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicSpacecraftFlightEndpoint]] = None


class PaginatedPolymorphicSpacecraftEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicSpacecraftEndpoint]] = None


class PaginatedPolymorphicSpacecraftConfigurationEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicSpacecraftConfigurationEndpoint]] = None


class PaginatedPolymorphicSpacecraftConfigFamilyEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicSpacecraftConfigFamilyEndpoint]] = None


class PaginatedPolymorphicSpaceStationEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicSpaceStationEndpoint]] = None


class PaginatedPolymorphicProgramEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicProgramEndpoint]] = None


class PaginatedPolymorphicPayloadFlightEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicPayloadFlightEndpoint]] = None


class PaginatedPolymorphicPayloadEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicPayloadEndpoint]] = None


class PaginatedPolymorphicMissionPatchEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicMissionPatchEndpoint]] = None


class PaginatedPolymorphicLocationEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicLocationEndpoint]] = None


class PaginatedPolymorphicLauncherEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicLauncherEndpoint]] = None


class PaginatedPolymorphicLauncherConfigFamilyEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicLauncherConfigFamilyEndpoint]] = None


class PaginatedPolymorphicLauncherConfigEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicLauncherConfigEndpoint]] = None


class PaginatedPolymorphicLaunchEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicLaunchEndpoint]] = None


class PaginatedPolymorphicLandingEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicLandingEndpoint]] = None


class PaginatedPolymorphicExpeditionEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicExpeditionEndpoint]] = None


class PaginatedPolymorphicEventsEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicEventsEndpoint]] = None


class PaginatedPolymorphicDockingEventEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicDockingEventEndpoint]] = None


class PaginatedPolymorphicCelestialBodyEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicCelestialBodyEndpoint]] = None


class PaginatedPolymorphicAstronautEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicAstronautEndpoint]] = None


class PaginatedPolymorphicAgencyEndpointList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PolymorphicAgencyEndpoint]] = None


class PaginatedPayloadTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[PayloadType]] = None


class PaginatedPadList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[Pad]] = None


class PaginatedOrbitList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[Orbit]] = None


class PaginatedNoticeTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[NoticeType]] = None


class PaginatedNetPrecisionList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[NetPrecision]] = None


class MissionType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class PaginatedMissionTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[MissionType]] = None


class PaginatedLauncherStatusList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[LauncherStatus]] = None


class PaginatedLaunchStatusList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[LaunchStatus]] = None


class PaginatedLanguageList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[Language]] = None


class PaginatedLandingTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[LandingType]] = None


class PaginatedLandingLocationList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[LandingLocation]] = None


class PaginatedInfoURLTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[InfoURLType]] = None


class PaginatedImageVariantTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[ImageVariantType]] = None


class PaginatedImageLicenseList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[ImageLicense]] = None


class FirstStageType(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: Optional[int] = None
    name: Optional[str] = None


class PaginatedFirstStageTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[FirstStageType]] = None


class PaginatedEventTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[EventType]] = None


class PaginatedDockingLocationList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[DockingLocation]] = None


class PaginatedCountryList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[Country]] = None


class PaginatedCelestialBodyTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[CelestialBodyType]] = None


class PaginatedAstronautTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[AstronautType]] = None


class PaginatedAstronautStatusList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[AstronautStatus]] = None


class PaginatedAstronautRoleList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[AstronautRole]] = None


class PaginatedAgencyTypeList(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    count: Optional[int] = Field(default=123)
    next: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=400&limit=100"
    )
    previous: Optional[str] = Field(
        default="http://api.example.org/accounts/?offset=200&limit=100"
    )
    results: Optional[List[AgencyType]] = None


class APIThrottle(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    your_request_limit: Optional[int] = None
    limit_frequency_secs: Optional[int] = None
    current_use: Optional[int] = None
    next_use_secs: Optional[int] = None
    ident: Optional[str] = None
