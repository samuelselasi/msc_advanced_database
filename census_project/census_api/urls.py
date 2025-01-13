from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (ActivityAbroadCodesViewSet, BathingFacilitiesViewSet, CookingFuelViewSet,
        CookingSpaceViewSet, CropTypeViewSet, DistrictTypesViewSet, DistrictsViewSet, DwellingTypeViewSet,
        EmploymentSectorViewSet, EmploymentStatusViewSet, EnumeratorViewSet, EthnicityViewSet, FarmMeasurementUnitViewSet,
        FloorViewSet, HouseholdRosterAbsentViewSet, HouseholdRosterEmigratedViewSet,
        HouseholdRosterPresentViewSet, LanguageLiteracyViewSet, LightingViewSet,
        LiquidWasteDisposalViewSet, LivestockOrFishViewSet, LocalitiesViewSet, MaritalStatusViewSet,
        MortalityViewSet, NationalityViewSet, OuterWallViewSet, OwnershipTypeViewSet, QuestionnaireViewSet,
        RegionAndCountryCodesViewSet, RelationshipCodesViewSet, ReligionViewSet, ResidenceTypeViewSet,
        RoofViewSet, SchoolingLevelViewSet, SolidWasteDisposalViewSet, SubdistrictsViewSet,
        SupervisorViewSet, TenureViewSet, ToiletFacilitiesViewSet, ToiletFacilitiesSharedViewSet,
        WaterSupplyDomesticViewSet, WaterSupplyDrinkingViewSet)


router = DefaultRouter()

router.register(r'activity_abroad_codes', ActivityAbroadCodesViewSet)
router.register(r'bathingfacilities', BathingFacilitiesViewSet)
router.register(r'cookingfuel', CookingFuelViewSet)
router.register(r'cookingspace', CookingSpaceViewSet)
router.register(r'croptype', CropTypeViewSet)
router.register(r'districttypes', DistrictTypesViewSet)
router.register(r'districts', DistrictsViewSet)
router.register(r'dwellingtype', DwellingTypeViewSet)
router.register(r'employmentsector', EmploymentSectorViewSet)
router.register(r'employmentstatus', EmploymentStatusViewSet)
router.register(r'enumerator', EnumeratorViewSet)
router.register(r'ethnicity', EthnicityViewSet)
router.register(r'farmmeasurementunit', FarmMeasurementUnitViewSet)
router.register(r'floor', FloorViewSet)
router.register(r'householdrosterabsent', HouseholdRosterAbsentViewSet)
router.register(r'householdrosteremigrated', HouseholdRosterEmigratedViewSet)
router.register(r'householdrosterpresent', HouseholdRosterPresentViewSet)
router.register(r'languageliteracy', LanguageLiteracyViewSet)
router.register(r'lighting', LightingViewSet)
router.register(r'liquidwastedisposal', LiquidWasteDisposalViewSet)
router.register(r'livestockorfish', LivestockOrFishViewSet)
router.register(r'localities', LocalitiesViewSet)
router.register(r'maritalstatus', MaritalStatusViewSet)
router.register(r'mortality', MortalityViewSet)
router.register(r'nationality', NationalityViewSet)
router.register(r'outerwall', OuterWallViewSet)
router.register(r'ownershiptype', OwnershipTypeViewSet)
router.register(r'questionnaire', QuestionnaireViewSet)
router.register(r'regionandcountrycodes', RegionAndCountryCodesViewSet)
router.register(r'relationshipcodes', RelationshipCodesViewSet)
router.register(r'religion', ReligionViewSet)
router.register(r'residencetype', ResidenceTypeViewSet)
router.register(r'roof', RoofViewSet)
router.register(r'schoolinglevel', SchoolingLevelViewSet)
router.register(r'solidwastedisposal', SolidWasteDisposalViewSet)
router.register(r'subdistricts', SubdistrictsViewSet)
router.register(r'supervisor', SupervisorViewSet)
router.register(r'tenure', TenureViewSet)
router.register(r'toiletfacilities', ToiletFacilitiesViewSet)
router.register(r'toiletfaciliesshared', ToiletFacilitiesSharedViewSet)
router.register(r'watersupplydomestic', WaterSupplyDomesticViewSet)
router.register(r'watersupplydrinking', WaterSupplyDrinkingViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Ensure this is included
]
