# Generated by Django 5.1.4 on 2025-01-13 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityAbroadCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(unique=True)),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'activity_abroad_codes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BathingFacilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'bathing_facilities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CookingFuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'cooking_fuel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CookingSpace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'cooking_space',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CropType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'crop_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
            options={
                'db_table': 'districts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DistrictTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField()),
            ],
            options={
                'db_table': 'district_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DwellingType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'dwelling_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentSector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'employment_sector',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EmploymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'employment_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Enumerator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('phone', models.IntegerField()),
            ],
            options={
                'db_table': 'enumerator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ethnicity',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(unique=True)),
                ('code', models.CharField(unique=True)),
            ],
            options={
                'db_table': 'ethnicity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FarmMeasurementUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'farm_measurement_unit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'floor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HouseholdRosterAbsent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField()),
                ('sex', models.CharField()),
                ('status', models.BooleanField()),
                ('months_absent', models.IntegerField()),
                ('dob', models.DateField()),
                ('sight_diasability', models.BooleanField()),
                ('hearing_disability', models.BooleanField()),
                ('speech_disability', models.BooleanField()),
                ('physical_disability', models.BooleanField()),
                ('intellect_disabiity', models.BooleanField()),
                ('emotional_disability', models.BooleanField()),
                ('other_disabilities', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'household_roster_absent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HouseholdRosterEmigrated',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField()),
                ('sex', models.CharField()),
                ('age', models.IntegerField()),
                ('status', models.BooleanField()),
                ('year_of_departure', models.IntegerField()),
                ('dob', models.DateField()),
                ('sight_diasability', models.BooleanField()),
                ('hearing_disability', models.BooleanField()),
                ('speech_disability', models.BooleanField()),
                ('physical_disability', models.BooleanField()),
                ('intellect_disabiity', models.BooleanField()),
                ('emotional_disability', models.BooleanField()),
                ('other_disabilities', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'household_roster_emigrated',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HouseholdRosterPresent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField()),
                ('sex', models.CharField()),
                ('status', models.BooleanField()),
                ('dob', models.DateField()),
                ('sight_diasability', models.BooleanField()),
                ('hearing_disability', models.BooleanField()),
                ('speech_disability', models.BooleanField()),
                ('physical_disability', models.BooleanField()),
                ('intellect_disabiity', models.BooleanField()),
                ('emotional_disability', models.BooleanField()),
                ('other_disabilities', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'household_roster_present',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LanguageLiteracy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField(unique=True)),
            ],
            options={
                'db_table': 'language_literacy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'lighting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LiquidWasteDisposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'liquid_waste_disposal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LivestockOrFish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'livestock_or_fish',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
            options={
                'db_table': 'localities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField(unique=True)),
            ],
            options={
                'db_table': 'marital_status',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mortality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('sex', models.CharField()),
                ('age_at_death', models.IntegerField()),
                ('accident', models.BooleanField()),
                ('pregnancy', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'mortality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(unique=True)),
                ('code', models.CharField(unique=True)),
            ],
            options={
                'db_table': 'nationality',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OuterWall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'outer_wall',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OwnershipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'ownership_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField()),
                ('household_members_male', models.IntegerField()),
                ('household_members_female', models.IntegerField()),
                ('household_visitors_male', models.IntegerField()),
                ('household_visitors_female', models.IntegerField()),
                ('date_started', models.DateField()),
                ('husehold_address', models.CharField()),
                ('ecg_or_vra_number', models.CharField()),
                ('date_completed', models.DateField()),
                ('household_number', models.CharField()),
                ('household_rooms', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('shared_rooms', models.BooleanField()),
                ('households_per_toilet_facility', models.IntegerField()),
                ('diceased', models.BooleanField()),
                ('fixed_tel_line', models.BooleanField()),
                ('desktop_or_laptop', models.BooleanField()),
                ('total_visits', models.IntegerField()),
                ('crop_farming', models.BooleanField()),
                ('tree_growing', models.BooleanField()),
                ('livestock_rearing', models.BooleanField()),
                ('fish_farming', models.BooleanField()),
                ('males_in_agric', models.IntegerField()),
                ('females_in_agric', models.IntegerField()),
            ],
            options={
                'db_table': 'questionnaire',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RegionAndCountryCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'region_and_country_codes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RelationshipCodes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(unique=True)),
                ('code', models.CharField(unique=True)),
            ],
            options={
                'db_table': 'relationship_codes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(unique=True)),
                ('code', models.CharField(unique=True)),
            ],
            options={
                'db_table': 'religion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ResidenceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'residence_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'roof',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SchoolingLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'schooling_level',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolidWasteDisposal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'solid_waste_disposal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Subdistricts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'subdistricts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('phone', models.IntegerField()),
            ],
            options={
                'db_table': 'supervisor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tenure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'tenure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ToiletFacilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'toilet_facilities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ToiletFacilitiesShared',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'toilet_facilities_shared',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WaterSupplyDomestic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'water_supply_domestic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WaterSupplyDrinking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField()),
                ('code', models.CharField()),
            ],
            options={
                'db_table': 'water_supply_drinking',
                'managed': False,
            },
        ),
    ]
