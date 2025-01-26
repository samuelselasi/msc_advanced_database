# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActivityAbroadCodes(models.Model):
    description = models.CharField(unique=True)
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'activity_abroad_codes'
        unique_together = (('id', 'code'),)


class BathingFacilities(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'bathing_facilities'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class CookingFuel(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'cooking_fuel'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class CookingSpace(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'cooking_space'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class CropType(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'crop_type'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class DistrictTypes(models.Model):
    type = models.CharField()

    class Meta:
        managed = False
        db_table = 'district_types'
        unique_together = (('id', 'type'),)


class Districts(models.Model):
    district_type = models.ForeignKey(DistrictTypes, models.DO_NOTHING)
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'districts'
        unique_together = (('id', 'name'),)


class DwellingType(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'dwelling_type'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class EmploymentSector(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'employment_sector'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class EmploymentStatus(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'employment_status'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class Enumerator(models.Model):
    supervisor = models.ForeignKey('Supervisor', models.DO_NOTHING)
    name = models.CharField()
    phone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'enumerator'
        unique_together = (('id', 'name', 'phone'),)


class Ethnicity(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(unique=True)
    code = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'ethnicity'


class FarmMeasurementUnit(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'farm_measurement_unit'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class Floor(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'floor'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class HouseholdRosterAbsent(models.Model):
    fname = models.CharField()
    relationship_type = models.ForeignKey('RelationshipCodes', models.DO_NOTHING, db_column='relationship_type')
    sex = models.CharField()
    status = models.BooleanField()
    months_absent = models.IntegerField()
    destination = models.ForeignKey('RegionAndCountryCodes', models.DO_NOTHING, db_column='destination')
    questionaire = models.ForeignKey('Questionnaire', models.DO_NOTHING)
    nationality = models.ForeignKey('Nationality', models.DO_NOTHING)
    dob = models.DateField()
    ethnicity = models.ForeignKey(Ethnicity, models.DO_NOTHING)
    birth_place = models.ForeignKey('RegionAndCountryCodes', models.DO_NOTHING, related_name='householdrosterabsent_birth_place_set')
    religion = models.ForeignKey('Religion', models.DO_NOTHING)
    marital_status = models.ForeignKey('MaritalStatus', models.DO_NOTHING)
    language_literacy = models.ForeignKey('LanguageLiteracy', models.DO_NOTHING)
    schooling_level = models.ForeignKey('SchoolingLevel', models.DO_NOTHING)
    employment_sector = models.ForeignKey(EmploymentSector, models.DO_NOTHING)
    employment_status = models.ForeignKey(EmploymentStatus, models.DO_NOTHING)
    sight_diasability = models.BooleanField()
    hearing_disability = models.BooleanField()
    speech_disability = models.BooleanField()
    physical_disability = models.BooleanField()
    intellect_disabiity = models.BooleanField()
    emotional_disability = models.BooleanField()
    other_disabilities = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_roster_absent'


class HouseholdRosterEmigrated(models.Model):
    fname = models.CharField()
    relationship_type = models.ForeignKey('RelationshipCodes', models.DO_NOTHING, db_column='relationship_type')
    destination = models.ForeignKey('RegionAndCountryCodes', models.DO_NOTHING, db_column='destination')
    sex = models.CharField()
    age = models.IntegerField()
    status = models.BooleanField()
    year_of_departure = models.IntegerField()
    activity_abroad = models.ForeignKey(ActivityAbroadCodes, models.DO_NOTHING, db_column='activity_abroad')
    quesstionaire = models.ForeignKey('Questionnaire', models.DO_NOTHING)
    nationality = models.ForeignKey('Nationality', models.DO_NOTHING)
    dob = models.DateField()
    ethnicity = models.ForeignKey(Ethnicity, models.DO_NOTHING)
    birth_place = models.ForeignKey('RegionAndCountryCodes', models.DO_NOTHING, related_name='householdrosteremigrated_birth_place_set')
    religion = models.ForeignKey('Religion', models.DO_NOTHING)
    marital_status = models.ForeignKey('MaritalStatus', models.DO_NOTHING)
    language_literacy = models.ForeignKey('LanguageLiteracy', models.DO_NOTHING)
    schooling_level = models.ForeignKey('SchoolingLevel', models.DO_NOTHING)
    employment_sector = models.ForeignKey(EmploymentSector, models.DO_NOTHING)
    employment_status = models.ForeignKey(EmploymentStatus, models.DO_NOTHING)
    sight_diasability = models.BooleanField()
    hearing_disability = models.BooleanField()
    speech_disability = models.BooleanField()
    physical_disability = models.BooleanField()
    intellect_disabiity = models.BooleanField()
    emotional_disability = models.BooleanField()
    other_disabilities = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_roster_emigrated'


class HouseholdRosterPresent(models.Model):
    fname = models.CharField()
    relationship_type = models.ForeignKey('RelationshipCodes', models.DO_NOTHING, db_column='relationship_type')
    sex = models.CharField()
    status = models.BooleanField()
    questionnaire = models.ForeignKey('Questionnaire', models.DO_NOTHING)
    nationality = models.ForeignKey('Nationality', models.DO_NOTHING)
    dob = models.DateField()
    ethnicity = models.ForeignKey(Ethnicity, models.DO_NOTHING)
    birth_place = models.ForeignKey('RegionAndCountryCodes', models.DO_NOTHING)
    religion = models.ForeignKey('Religion', models.DO_NOTHING)
    marital_status = models.ForeignKey('MaritalStatus', models.DO_NOTHING)
    language_literacy = models.ForeignKey('LanguageLiteracy', models.DO_NOTHING)
    schooling_level = models.ForeignKey('SchoolingLevel', models.DO_NOTHING)
    employment_sector = models.ForeignKey(EmploymentSector, models.DO_NOTHING)
    employment_status = models.ForeignKey(EmploymentStatus, models.DO_NOTHING)
    sight_diasability = models.BooleanField()
    hearing_disability = models.BooleanField()
    speech_disability = models.BooleanField()
    physical_disability = models.BooleanField()
    intellect_disabiity = models.BooleanField()
    emotional_disability = models.BooleanField()
    other_disabilities = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'household_roster_present'


class LanguageLiteracy(models.Model):
    description = models.CharField()
    code = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'language_literacy'
        unique_together = (('id', 'description'),)


class Lighting(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'lighting'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class LiquidWasteDisposal(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'liquid_waste_disposal'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class LivestockOrFish(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'livestock_or_fish'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class Localities(models.Model):
    subdistrictid = models.ForeignKey('Subdistricts', models.DO_NOTHING, db_column='subdistrictID')  # Field name made lowercase.
    name = models.CharField()

    class Meta:
        managed = False
        db_table = 'localities'
        unique_together = (('id', 'subdistrictid'),)


class MaritalStatus(models.Model):
    description = models.CharField()
    code = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'marital_status'
        unique_together = (('id', 'description'),)


class Mortality(models.Model):
    name = models.CharField()
    sex = models.CharField()
    age_at_death = models.IntegerField()
    accident = models.BooleanField()
    pregnancy = models.BooleanField(blank=True, null=True)
    questionaire = models.ForeignKey('Questionnaire', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mortality'


class Nationality(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(unique=True)
    code = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'nationality'


class OuterWall(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'outer_wall'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class OwnershipType(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'ownership_type'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class Questionnaire(models.Model):
    code = models.CharField()
    region = models.ForeignKey('RegionAndCountryCodes', models.DO_NOTHING)
    district_type = models.ForeignKey(DistrictTypes, models.DO_NOTHING)
    district = models.ForeignKey(Districts, models.DO_NOTHING)
    sub_district = models.ForeignKey('Subdistricts', models.DO_NOTHING)
    locality = models.ForeignKey(Localities, models.DO_NOTHING)
    household_members_male = models.IntegerField()
    household_members_female = models.IntegerField()
    enumerator = models.ForeignKey(Enumerator, models.DO_NOTHING)
    household_visitors_male = models.IntegerField()
    household_visitors_female = models.IntegerField()
    date_started = models.DateField()
    household_address = models.CharField()
    ecg_or_vra_number = models.CharField()
    date_completed = models.DateField()
    household_number = models.CharField()
    dwelling_type = models.ForeignKey(DwellingType, models.DO_NOTHING)
    roof_type = models.ForeignKey('Roof', models.DO_NOTHING)
    outer_wall_type = models.ForeignKey(OuterWall, models.DO_NOTHING)
    floor_type = models.ForeignKey(Floor, models.DO_NOTHING)
    tenure_type = models.ForeignKey('Tenure', models.DO_NOTHING)
    ownership_type = models.ForeignKey(OwnershipType, models.DO_NOTHING)
    household_rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    shared_rooms = models.BooleanField()
    lighting_type = models.ForeignKey(Lighting, models.DO_NOTHING)
    drinking_water = models.ForeignKey('WaterSupplyDrinking', models.DO_NOTHING)
    domestic_water = models.ForeignKey('WaterSupplyDomestic', models.DO_NOTHING)
    cooking_fuel = models.ForeignKey(CookingFuel, models.DO_NOTHING)
    cooking_space = models.ForeignKey(CookingSpace, models.DO_NOTHING)
    bathing_facilities = models.ForeignKey(BathingFacilities, models.DO_NOTHING)
    toilet_facilities = models.ForeignKey('ToiletFacilities', models.DO_NOTHING)
    toilet_facilities_shared = models.ForeignKey('ToiletFacilitiesShared', models.DO_NOTHING)
    households_per_toilet_facility = models.IntegerField()
    solid_waste_disposal = models.ForeignKey('SolidWasteDisposal', models.DO_NOTHING)
    liquid_waste_disposal = models.ForeignKey(LiquidWasteDisposal, models.DO_NOTHING)
    deceased = models.BooleanField()
    fixed_tel_line = models.BooleanField()
    desktop_or_laptop = models.BooleanField()
    total_visits = models.IntegerField()
    residence_type = models.ForeignKey('ResidenceType', models.DO_NOTHING)
    crop_farming = models.BooleanField()
    tree_growing = models.BooleanField()
    livestock_rearing = models.BooleanField()
    fish_farming = models.BooleanField()
    males_in_agric = models.IntegerField()
    females_in_agric = models.IntegerField()
    crop_type = models.ForeignKey(CropType, models.DO_NOTHING)
    farm_measurement_unit = models.ForeignKey(FarmMeasurementUnit, models.DO_NOTHING, blank=True, null=True)
    livestock_or_fish = models.ForeignKey(LivestockOrFish, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'questionnaire'
        unique_together = (('id', 'code', 'household_number'),)


class RegionAndCountryCodes(models.Model):
    name = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'region_and_country_codes'
        unique_together = (('id', 'name'), ('name', 'code'),)


class RelationshipCodes(models.Model):
    description = models.CharField(unique=True)
    code = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'relationship_codes'
        unique_together = (('id', 'description'),)


class Religion(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(unique=True)
    code = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = 'religion'


class ResidenceType(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'residence_type'
        unique_together = (('id', 'description', 'code'),)


class Roof(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'roof'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class SchoolingLevel(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'schooling_level'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class SolidWasteDisposal(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'solid_waste_disposal'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class Subdistricts(models.Model):
    districtid = models.ForeignKey(Districts, models.DO_NOTHING, db_column='districtid')
    name = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subdistricts'
        unique_together = (('id', 'districtid'),)


class Supervisor(models.Model):
    name = models.CharField()
    phone = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supervisor'
        unique_together = (('id', 'name', 'phone'),)


class Tenure(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'tenure'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class ToiletFacilities(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'toilet_facilities'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class ToiletFacilitiesShared(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'toilet_facilities_shared'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class WaterSupplyDomestic(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'water_supply_domestic'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)


class WaterSupplyDrinking(models.Model):
    description = models.CharField()
    code = models.CharField()

    class Meta:
        managed = False
        db_table = 'water_supply_drinking'
        unique_together = (('id', 'description'), ('id', 'description', 'code'),)
