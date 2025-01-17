from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from .models import (ActivityAbroadCodes, BathingFacilities, CookingFuel, CookingSpace, CropType, DistrictTypes,
        Districts, DwellingType, EmploymentSector, EmploymentStatus, Enumerator,
        Ethnicity, FarmMeasurementUnit, Floor, HouseholdRosterAbsent,
        HouseholdRosterEmigrated, HouseholdRosterPresent, LanguageLiteracy,
        Lighting, LiquidWasteDisposal, LivestockOrFish, Localities, MaritalStatus,
        Mortality, Nationality, OuterWall, OwnershipType, Questionnaire,
        RegionAndCountryCodes, RelationshipCodes, Religion, ResidenceType, Roof,
        SchoolingLevel, SolidWasteDisposal, Subdistricts, Supervisor, Tenure,
        ToiletFacilities, ToiletFacilitiesShared, WaterSupplyDomestic, WaterSupplyDrinking)
from .serializers import (ActivityAbroadCodesSerializer, BathingFacilitiesSerializer, CookingFuelSerializer, CookingSpaceSerializer,
        CropTypeSerializer, DistrictTypesSerializer, DistrictsSerializer,
        DwellingTypeSerializer, EmploymentSectorSerializer, EmploymentStatusSerializer,
        EnumeratorSerializer, EthnicitySerializer, FarmMeasurementUnitSerializer,
        FloorSerializer, HouseholdRosterAbsentSerializer, HouseholdRosterEmigratedSerializer,
        HouseholdRosterPresentSerializer, LanguageLiteracySerializer, LightingSerializer,
        LiquidWasteDisposalSerializer, LivestockOrFishSerializer, LocalitiesSerializer,
        MaritalStatusSerializer, MortalitySerializer, NationalitySerializer,
        OuterWallSerializer, OwnershipTypeSerializer, QuestionnaireSerializer,
        RegionAndCountryCodesSerializer, RelationshipCodesSerializer, ReligionSerializer,
        ResidenceTypeSerializer, RoofSerializer, SchoolingLevelSerializer,
        SolidWasteDisposalSerializer, SubdistrictsSerializer, SupervisorSerializer,
        TenureSerializer, ToiletFacilitiesSerializer, ToiletFacilitiesSharedSerializer,
        WaterSupplyDomesticSerializer, WaterSupplyDrinkingSerializer)

def api_dashboard(request):
    return render(request, 'index.html')

class ActivityAbroadCodesViewSet(viewsets.ModelViewSet):
    queryset = ActivityAbroadCodes.objects.all()
    serializer_class = ActivityAbroadCodesSerializer

class BathingFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = BathingFacilities.objects.all()
    serializer_class = BathingFacilitiesSerializer

class CookingFuelViewSet(viewsets.ModelViewSet):
    queryset = CookingFuel.objects.all()
    serializer_class = CookingFuelSerializer

class CookingSpaceViewSet(viewsets.ModelViewSet):
    queryset = CookingSpace.objects.all()
    serializer_class = CookingSpaceSerializer

class CropTypeViewSet(viewsets.ModelViewSet):
    queryset = CropType.objects.all()
    serializer_class = CropTypeSerializer

class DistrictTypesViewSet(viewsets.ModelViewSet):
    queryset = DistrictTypes.objects.all()
    serializer_class = DistrictTypesSerializer

class DistrictsViewSet(viewsets.ModelViewSet):
    queryset = Districts.objects.all()
    serializer_class = DistrictsSerializer

class DwellingTypeViewSet(viewsets.ModelViewSet):
    queryset = DwellingType.objects.all()
    serializer_class = DwellingTypeSerializer

class EmploymentSectorViewSet(viewsets.ModelViewSet):
    queryset = EmploymentSector.objects.all()
    serializer_class = EmploymentSectorSerializer

class EmploymentStatusViewSet(viewsets.ModelViewSet):
    queryset = EmploymentStatus.objects.all()
    serializer_class = EmploymentStatusSerializer

class EnumeratorViewSet(viewsets.ModelViewSet):
    queryset = Enumerator.objects.all()
    serializer_class = EnumeratorSerializer

class EthnicityViewSet(viewsets.ModelViewSet):
    queryset = Ethnicity.objects.all()
    serializer_class = EthnicitySerializer

class FarmMeasurementUnitViewSet(viewsets.ModelViewSet):
    queryset = FarmMeasurementUnit.objects.all()
    serializer_class = FarmMeasurementUnitSerializer

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class HouseholdRosterAbsentViewSet(viewsets.ModelViewSet):
    queryset = HouseholdRosterAbsent.objects.all()
    serializer_class = HouseholdRosterAbsentSerializer

class HouseholdRosterEmigratedViewSet(viewsets.ModelViewSet):
    queryset = HouseholdRosterEmigrated.objects.all()
    serializer_class = HouseholdRosterEmigratedSerializer

class HouseholdRosterPresentViewSet(viewsets.ModelViewSet):
    queryset = HouseholdRosterPresent.objects.all()
    serializer_class = HouseholdRosterPresentSerializer

class LanguageLiteracyViewSet(viewsets.ModelViewSet):
    queryset = LanguageLiteracy.objects.all()
    serializer_class = LanguageLiteracySerializer

class LightingViewSet(viewsets.ModelViewSet):
    queryset = Lighting.objects.all()
    serializer_class = LightingSerializer

class LiquidWasteDisposalViewSet(viewsets.ModelViewSet):
    queryset = LiquidWasteDisposal.objects.all()
    serializer_class = LiquidWasteDisposalSerializer

class LivestockOrFishViewSet(viewsets.ModelViewSet):
    queryset = LivestockOrFish.objects.all()
    serializer_class = LivestockOrFishSerializer

class LocalitiesViewSet(viewsets.ModelViewSet):
    queryset = Localities.objects.all()
    serializer_class = LocalitiesSerializer

class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer

class MortalityViewSet(viewsets.ModelViewSet):
    queryset = Mortality.objects.all()
    serializer_class = MortalitySerializer

class NationalityViewSet(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer

class OuterWallViewSet(viewsets.ModelViewSet):
    queryset = OuterWall.objects.all()
    serializer_class = OuterWallSerializer

class OwnershipTypeViewSet(viewsets.ModelViewSet):
    queryset = OwnershipType.objects.all()
    serializer_class = OwnershipTypeSerializer

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class RegionAndCountryCodesViewSet(viewsets.ModelViewSet):
    queryset = RegionAndCountryCodes.objects.all()
    serializer_class = RegionAndCountryCodesSerializer

class RelationshipCodesViewSet(viewsets.ModelViewSet):
    queryset = RelationshipCodes.objects.all()
    serializer_class = RelationshipCodesSerializer

class ReligionViewSet(viewsets.ModelViewSet):
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer

class ResidenceTypeViewSet(viewsets.ModelViewSet):
    queryset = ResidenceType.objects.all()
    serializer_class = ResidenceTypeSerializer

class RoofViewSet(viewsets.ModelViewSet):
    queryset = Roof.objects.all()
    serializer_class = RoofSerializer

class SchoolingLevelViewSet(viewsets.ModelViewSet):
    queryset = SchoolingLevel.objects.all()
    serializer_class = SchoolingLevelSerializer

class SolidWasteDisposalViewSet(viewsets.ModelViewSet):
    queryset = SolidWasteDisposal.objects.all()
    serializer_class = SolidWasteDisposalSerializer

class SubdistrictsViewSet(viewsets.ModelViewSet):
    queryset = Subdistricts.objects.all()
    serializer_class = SubdistrictsSerializer

class SupervisorViewSet(viewsets.ModelViewSet):
    queryset = Supervisor.objects.all()
    serializer_class = SupervisorSerializer

class TenureViewSet(viewsets.ModelViewSet):
    queryset = Tenure.objects.all()
    serializer_class = TenureSerializer

class ToiletFacilitiesViewSet(viewsets.ModelViewSet):
    queryset = ToiletFacilities.objects.all()
    serializer_class = ToiletFacilitiesSerializer

class ToiletFacilitiesSharedViewSet(viewsets.ModelViewSet):
    queryset = ToiletFacilitiesShared.objects.all()
    serializer_class = ToiletFacilitiesSharedSerializer

class WaterSupplyDomesticViewSet(viewsets.ModelViewSet):
    queryset = WaterSupplyDomestic.objects.all()
    serializer_class = WaterSupplyDomesticSerializer

class WaterSupplyDrinkingViewSet(viewsets.ModelViewSet):
    queryset = WaterSupplyDrinking.objects.all()
    serializer_class = WaterSupplyDrinkingSerializer
