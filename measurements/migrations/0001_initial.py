# Generated by Django 5.0.6 on 2024-06-29 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BiochemicalMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('glucose', models.FloatField(blank=True, null=True)),
                ('cholesterol', models.FloatField(blank=True, null=True)),
                ('triglycerides', models.FloatField(blank=True, null=True)),
                ('hdl', models.FloatField(blank=True, null=True)),
                ('ldl', models.FloatField(blank=True, null=True)),
                ('creatinine', models.FloatField(blank=True, null=True)),
                ('urea', models.FloatField(blank=True, null=True)),
                ('uric_acid', models.FloatField(blank=True, null=True)),
                ('hemoglobin', models.FloatField(blank=True, null=True)),
                ('hematocrit', models.FloatField(blank=True, null=True)),
                ('white_blood_cell_count', models.FloatField(blank=True, null=True)),
                ('red_blood_cell_count', models.FloatField(blank=True, null=True)),
                ('platelet_count', models.FloatField(blank=True, null=True)),
                ('calcium', models.FloatField(blank=True, null=True)),
                ('sodium', models.FloatField(blank=True, null=True)),
                ('potassium', models.FloatField(blank=True, null=True)),
                ('chloride', models.FloatField(blank=True, null=True)),
                ('iron', models.FloatField(blank=True, null=True)),
                ('ferritin', models.FloatField(blank=True, null=True)),
                ('alanine_aminotransferase', models.FloatField(blank=True, null=True)),
                ('aspratate_aminotransferase', models.FloatField(blank=True, null=True)),
                ('alkaline_phosphatase', models.FloatField(blank=True, null=True)),
                ('bilirubin', models.FloatField(blank=True, null=True)),
                ('albumin', models.FloatField(blank=True, null=True)),
                ('total_protein', models.FloatField(blank=True, null=True)),
                ('thyroid_stimulating_hormone', models.FloatField(blank=True, null=True)),
                ('thyroxine', models.FloatField(blank=True, null=True)),
                ('triiodothyronine', models.FloatField(blank=True, null=True)),
                ('c_reactive_protein', models.FloatField(blank=True, null=True)),
                ('lactate_dehydrogenase', models.FloatField(blank=True, null=True)),
                ('vitamin_a', models.FloatField(blank=True, null=True)),
                ('vitamin_b12', models.FloatField(blank=True, null=True)),
                ('vitamin_c', models.FloatField(blank=True, null=True)),
                ('vitamin_d', models.FloatField(blank=True, null=True)),
                ('vitamin_e', models.FloatField(blank=True, null=True)),
                ('vitamin_k', models.FloatField(blank=True, null=True)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='BodyMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(blank=True, null=True)),
                ('height', models.FloatField(blank=True, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('bmr', models.FloatField(blank=True, null=True)),
                ('bmi', models.FloatField(blank=True, null=True)),
                ('body_fat_percentage', models.FloatField(blank=True, null=True)),
                ('body_fat_mass', models.FloatField(blank=True, null=True)),
                ('fat_free_mass', models.FloatField(blank=True, null=True)),
                ('muscle_mass', models.FloatField(blank=True, null=True)),
                ('bone_mass', models.FloatField(blank=True, null=True)),
                ('body_water_percentage', models.FloatField(blank=True, null=True)),
                ('body_water_weight', models.FloatField(blank=True, null=True)),
                ('visceral_fat_level', models.IntegerField(blank=True, null=True)),
                ('metabolic_age', models.IntegerField(blank=True, null=True)),
                ('physical_activity_level', models.FloatField(blank=True, null=True)),
                ('physique_rating', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_foods', models.TextField(blank=True, null=True)),
                ('disliked_foods', models.TextField(blank=True, null=True)),
                ('activity_level', models.FloatField(blank=True, null=True)),
                ('weight_goal', models.FloatField(blank=True, null=True)),
                ('fat', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
                ('carbohydrates', models.FloatField(blank=True, null=True)),
                ('diet', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('past_diseases', models.TextField(blank=True, null=True)),
                ('past_medications', models.TextField(blank=True, null=True)),
                ('current_diseases', models.TextField(blank=True, null=True)),
                ('current_medications', models.TextField(blank=True, null=True)),
                ('family_history', models.TextField(blank=True, null=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('dysanexias', models.TextField(blank=True, null=True)),
                ('food_restrictions', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Diseases',
            },
        ),
        migrations.CreateModel(
            name='SegmentalBodyMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trunk_muscle', models.FloatField(blank=True, null=True)),
                ('left_arm_muscle', models.FloatField(blank=True, null=True)),
                ('right_arm_muscle', models.FloatField(blank=True, null=True)),
                ('left_leg_muscle', models.FloatField(blank=True, null=True)),
                ('right_leg_muscle', models.FloatField(blank=True, null=True)),
                ('trunk_fat', models.FloatField(blank=True, null=True)),
                ('left_arm_fat', models.FloatField(blank=True, null=True)),
                ('right_arm_fat', models.FloatField(blank=True, null=True)),
                ('left_leg_fat', models.FloatField(blank=True, null=True)),
                ('right_leg_fat', models.FloatField(blank=True, null=True)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
