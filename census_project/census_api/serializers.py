from rest_framework import serializers
from .models import (ActivityAbroadCodes, BathingFacilities, CookingFuel, CookingSpace,
        CropType, DistrictTypes, Districts, DwellingType, EmploymentSector, EmploymentStatus,
        Enumerator, Ethnicity, FarmMeasurementUnit, Floor, HouseholdRosterAbsent,
        HouseholdRosterEmigrated, HouseholdRosterPresent, LanguageLiteracy, Lighting,
        LiquidWasteDisposal, LivestockOrFish, Localities, MaritalStatus, Mortality, Nationality,
        OuterWall, OwnershipType, Questionnaire, RegionAndCountryCodes, RelationshipCodes,
        Religion, ResidenceType, Roof, SchoolingLevel, SolidWasteDisposal, Subdistricts, Supervisor,
        Tenure, ToiletFacilities, ToiletFacilitiesShared, WaterSupplyDomestic, WaterSupplyDrinking)

class ActivityAbroadCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityAbroadCodes
        fields = '__all__'

class BathingFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BathingFacilities
        fields = ['id', 'description', 'code']

class CookingFuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingFuel
        fields = ['id', 'description', 'code']

class CookingSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookingSpace
        fields = ['id', 'description', 'code']

class CropTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CropType
        fields = ['id', 'description', 'code']

class DistrictTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistrictTypes
        fields = ['id', 'type']

class DistrictsSerializer(serializers.ModelSerializer):
    district_type = DistrictTypesSerializer()

    class Meta:
        model = Districts
        fields = ['id', 'district_type', 'name']

class DwellingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DwellingType
        fields = ['id', 'description', 'code']

class EmploymentSectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentSector
        fields = ['id', 'description', 'code']

class EmploymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentStatus
        fields = ['id', 'description', 'code']

class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = ['id', 'name', 'phone']

class EnumeratorSerializer(serializers.ModelSerializer):
    supervisor = SupervisorSerializer()

    class Meta:
        model = Enumerator
        fields = ['id', 'supervisor', 'name', 'phone']

class EthnicitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ethnicity
        fields = ['id', 'description', 'code']

class FarmMeasurementUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmMeasurementUnit
        fields = ['id', 'description', 'code']

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ['id', 'description', 'code']

class HouseholdRosterAbsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdRosterAbsent
        fields = '__all__'

class HouseholdRosterEmigratedSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdRosterEmigrated
        fields = '__all__'

class HouseholdRosterPresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseholdRosterPresent
        fields = '__all__'

class LanguageLiteracySerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageLiteracy
        fields = ['id', 'description', 'code']

class LightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lighting
        fields = ['id', 'description', 'code']

class LiquidWasteDisposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiquidWasteDisposal
        fields = ['id', 'description', 'code']

class LivestockOrFishSerializer(serializers.ModelSerializer):
    class Meta:
        model = LivestockOrFish
        fields = ['id', 'description', 'code']

class SubdistrictsSerializer(serializers.ModelSerializer):
    districtid = DistrictsSerializer()

    class Meta:
        model = Subdistricts
        fields = ['id', 'districtid', 'name']

class LocalitiesSerializer(serializers.ModelSerializer):
    subdistrictid = SubdistrictsSerializer()

    class Meta:
        model = Localities
        fields = ['id', 'subdistrictid', 'name']

class MaritalStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ['id', 'description', 'code']

class MortalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortality
        fields = '__all__'

class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = ['id', 'description', 'code']

class OuterWallSerializer(serializers.ModelSerializer):
    class Meta:
        model = OuterWall
        fields = ['id', 'description', 'code']

class OwnershipTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnershipType
        fields = ['id', 'description', 'code']

class RegionAndCountryCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionAndCountryCodes
        fields = ['id', 'name', 'code']

class RelationshipCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelationshipCodes
        fields = ['id', 'description', 'code']

class ReligionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religion
        fields = ['id', 'description', 'code']

class ResidenceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResidenceType
        fields = ['id', 'description', 'code']

class RoofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roof
        fields = ['id', 'description', 'code']

class SchoolingLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolingLevel
        fields = ['id', 'description', 'code']

class SolidWasteDisposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolidWasteDisposal
        fields = ['id', 'description', 'code']

class TenureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenure
        fields = ['id', 'description', 'code']

class ToiletFacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToiletFacilities
        fields = ['id', 'description', 'code']

class ToiletFacilitiesSharedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToiletFacilitiesShared
        fields = ['id', 'description', 'code']

class WaterSupplyDomesticSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterSupplyDomestic
        fields = ['id', 'description', 'code']

class WaterSupplyDrinkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterSupplyDrinking
        fields = ['id', 'description', 'code']

class QuestionnaireSerializer(serializers.ModelSerializer):
    region = RegionAndCountryCodesSerializer()
    district_type = DistrictTypesSerializer()
    district = DistrictsSerializer()
    dwelling_type = DwellingTypeSerializer()
    roof_type = RoofSerializer()
    outer_wall_type = OuterWallSerializer()
    floor_type = FloorSerializer()
    tenure_type = TenureSerializer()
    ownership_type = OwnershipTypeSerializer()
    lighting_type = LightingSerializer()
    drinking_water = WaterSupplyDrinkingSerializer()
    domestic_water = WaterSupplyDomesticSerializer()
    cooking_fuel = CookingFuelSerializer()
    cooking_space = CookingSpaceSerializer()
    bathing_facilities = BathingFacilitiesSerializer()
    toilet_facilities = ToiletFacilitiesSerializer()
    toilet_facilities_shared = ToiletFacilitiesSharedSerializer()
    solid_waste_disposal = SolidWasteDisposalSerializer()
    liquid_waste_disposal = LiquidWasteDisposalSerializer()
    residence_type = ResidenceTypeSerializer()
    crop_type = CropTypeSerializer()
    farm_measurement_unit = FarmMeasurementUnitSerializer()
    livestock_or_fish = LivestockOrFishSerializer()

    class Meta:
        model = Questionnaire
        fields = '__all__'
