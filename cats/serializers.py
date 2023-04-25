from rest_framework import serializers
from .models import Cat, Owner, Achievement, AchievementCat, Toy, FavouriteToyCat
from django.utils import timezone

class AchievementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Achievement
        fields = ('id', 'name')

class ToySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Toy
        fields = ('id', 'name')

class CatSerializer(serializers.ModelSerializer):
    achievements = AchievementSerializer(many=True, required=False)
    toys = ToySerializer(many=True, required=False)

    class Meta:
        model = Cat
        # fields = '__all__'
        fields = ('id', 'name', 'color', 'birth_year', 'is_purebred', 'owner', 'toys', 'achievements', 'created', 'changed') 
    
    def soft_del(self):
        self.deleted = True
        self.save()


    def create(self, validated_data):
        # extra = {achievements, toys}
        # Если в исходном запросе не было поля achievements
        if 'achievements' not in self.initial_data:
            # То создаём запись о котике без его достижений
            cat = Cat.objects.create(**validated_data)
        if 'toys' not in self.initial_data:
            # То создаём запись о котике без его достижений
            cat = Cat.objects.create(**validated_data)
            return cat
        
        # Уберем список достижений из словаря validated_data и сохраним его
        achievements = validated_data.pop('achievements')
        toys = validated_data.pop('toys')

        # Создадим нового котика пока без достижений, данных нам достаточно
        cat = Cat.objects.create(**validated_data)

        # Для каждого достижения из списка достижений
        for achievement in achievements:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_achievement, status = Achievement.objects.get_or_create(
                **achievement)
            # Поместим ссылку на каждое достижение во вспомогательную таблицу
            # Не забыв указать к какому котику оно относится
            AchievementCat.objects.create(
                achievement=current_achievement, cat=cat)
        for toy in toys:
            # Создадим новую запись или получим существующий экземпляр из БД
            current_toy, status = Toy.objects.get_or_create(**toy)
            # Поместим ссылку на каждую игрушку во вспомогательную таблицу
            # Не забыв указать к какому котику оно относится
            FavouriteToyCat.objects.create(
                toy=current_toy, cat=cat)
        Toy.objects.create(cat=cat, **toys)
        return cat
    

class OwnerSerializer(serializers.ModelSerializer):
    # cats = serializers.StringRelatedField(many=True)
    class Meta:
        model = Owner
        fields = ('first_name', 'last_name', 'cats')