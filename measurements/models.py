from django.db import models
from users.models import CustomUser, NormalUser
from nutritionists.models import Nutritionist

class BodyMeasurement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(NormalUser, on_delete=models.CASCADE, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    bmr = models.FloatField(null=True, blank=True)
    bmi = models.FloatField(null=True, blank=True)
    body_fat_percentage = models.FloatField(null=True, blank=True)
    body_fat_mass = models.FloatField(null=True, blank=True)
    fat_free_mass = models.FloatField(null=True, blank=True)
    muscle_mass = models.FloatField(null=True, blank=True)
    bone_mass = models.FloatField(null=True, blank=True)
    body_water_percentage = models.FloatField(null=True, blank=True)
    body_water_weight = models.FloatField(null=True, blank=True)
    visceral_fat_level = models.IntegerField(null=True, blank=True)
    metabolic_age = models.IntegerField(null=True, blank=True)
    physical_activity_level = models.FloatField(null=True, blank=True)
    physique_rating = models.IntegerField(null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        if self.user:
            return f"Body measurement: {self.user.username} - {self.date}"
        else:
            return f"Body measurement: {self.client.first_name}, {self.client.last_name} - {self.date}"

class SegmentalBodyMeasurement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(NormalUser, on_delete=models.CASCADE, null=True, blank=True)
    trunk_muscle = models.FloatField(null=True, blank=True)
    left_arm_muscle = models.FloatField(null=True, blank=True)
    right_arm_muscle = models.FloatField(null=True, blank=True)
    left_leg_muscle = models.FloatField(null=True, blank=True)
    right_leg_muscle = models.FloatField(null=True, blank=True)
    trunk_fat = models.FloatField(null=True, blank=True)
    left_arm_fat = models.FloatField(null=True, blank=True)
    right_arm_fat = models.FloatField(null=True, blank=True)
    left_leg_fat = models.FloatField(null=True, blank=True)
    right_leg_fat = models.FloatField(null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            return f"Segmental body measurement: {self.user.username} - {self.date}"
        else:
            return f"Segmental body measurement: {self.client.first_name}, {self.client.last_name} - {self.date}"
    

class BiochemicalMeasurement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(NormalUser, on_delete=models.CASCADE, null=True, blank=True)
    glucose = models.FloatField(null=True, blank=True)
    cholesterol = models.FloatField(null=True, blank=True)
    triglycerides = models.FloatField(null=True, blank=True)
    hdl = models.FloatField(null=True, blank=True)
    ldl = models.FloatField(null=True, blank=True)
    creatinine = models.FloatField(null=True, blank=True)
    urea = models.FloatField(null=True, blank=True)
    uric_acid = models.FloatField(null=True, blank=True)
    hemoglobin = models.FloatField(null=True, blank=True)
    hematocrit = models.FloatField(null=True, blank=True)
    white_blood_cell_count = models.FloatField(null=True, blank=True)
    red_blood_cell_count = models.FloatField(null=True, blank=True)
    platelet_count = models.FloatField(null=True, blank=True)
    calcium = models.FloatField(null=True, blank=True)
    sodium = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    chloride = models.FloatField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    ferritin = models.FloatField(null=True, blank=True)
    alanine_aminotransferase = models.FloatField(null=True, blank=True)
    aspratate_aminotransferase = models.FloatField(null=True, blank=True)
    alkaline_phosphatase = models.FloatField(null=True, blank=True)
    bilirubin = models.FloatField(null=True, blank=True)
    albumin = models.FloatField(null=True, blank=True)
    total_protein = models.FloatField(null=True, blank=True)
    thyroid_stimulating_hormone = models.FloatField(null=True, blank=True)
    thyroxine = models.FloatField(null=True, blank=True)
    triiodothyronine = models.FloatField(null=True, blank=True)
    c_reactive_protein = models.FloatField(null=True, blank=True)
    lactate_dehydrogenase = models.FloatField(null=True, blank=True)
    vitamin_a = models.FloatField(null=True, blank=True)
    vitamin_b12 = models.FloatField(null=True, blank=True)
    vitamin_c = models.FloatField(null=True, blank=True)
    vitamin_d = models.FloatField(null=True, blank=True)
    vitamin_e = models.FloatField(null=True, blank=True)
    vitamin_k = models.FloatField(null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            return f"Biochemical measurement: {self.user.username} - {self.date}"
        else:
            return f"Biochemical measurement: {self.client.first_name}, {self.client.last_name} - {self.date}"
    

class Diseases(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(NormalUser, on_delete=models.CASCADE, null=True, blank=True)
    past_diseases = models.TextField(null=True, blank=True)
    past_medications = models.TextField(null=True, blank=True)
    current_diseases = models.TextField(null=True, blank=True)
    current_medications = models.TextField(null=True, blank=True)
    family_history = models.TextField(null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    dysanexias = models.TextField(null=True, blank=True)
    food_restrictions = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Diseases"

    def __str__(self):
        if self.user:
            return f"Diseases: {self.user.username} - {self.date}"
        else:
            return f"Diseases: {self.client.first_name}, {self.client.last_name} - {self.date}"


class Diet(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(NormalUser, on_delete=models.CASCADE, null=True, blank=True)
    nutritionist = models.ForeignKey(Nutritionist, on_delete=models.CASCADE, null=True, blank=True)
    preferred_foods = models.TextField(null=True, blank=True)
    disliked_foods = models.TextField(null=True, blank=True)
    activity_level = models.FloatField(null=True, blank=True)
    weight_goal = models.FloatField(null=True, blank=True)
    fat = models.FloatField(null=True, blank=True)
    protein = models.FloatField(null=True, blank=True)
    carbohydrates = models.FloatField(null=True, blank=True)
    diet = models.TextField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user:
            return f"Diet: {self.user.username} - {self.date}"
        else:
            return f"Diet: {self.client.first_name}, {self.client.last_name} - {self.date}"