from rest_framework import serializers
from rest_typed.serializers import TSerializer


class FlavorTextRequestSerializer(TSerializer):
    """フレーバーテキスト生成リクエストのシリアライザ"""

    target_type = serializers.ChoiceField(
        choices=["item", "character", "location", "skill"]
    )
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    rarity = serializers.CharField(max_length=50, required=False)
    style_hint = serializers.CharField(required=False)


class FlavorTextResponseSerializer(TSerializer):
    """フレーバーテキスト生成レスポンスのシリアライザ"""

    flavor_text = serializers.CharField()
