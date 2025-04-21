from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .llm_service import generate_flavor_text_from_llm
from .serializers import FlavorTextRequestSerializer, FlavorTextResponseSerializer


class GenerateFlavorTextView(APIView):
    """フレーバーテキストの生成を行うAPIエンドポイント"""

    def post(
        self,
        request: Request,
    ) -> Response:
        """POSTリクエストを受け取り、フレーバーテキストを生成する"""
        serializer = FlavorTextRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated_data = serializer.validated_data
        try:
            flavor_text = generate_flavor_text_from_llm(**validated_data)
            print(flavor_text)  # デバッグ用

            # 生成されたフレーバーテキストをレスポンスとして返す
            response_serializer = FlavorTextResponseSerializer(
                data={"flavor_text": flavor_text}
            )
            response_serializer.is_valid()
            return Response(response_serializer.data, status=status.HTTP_200_OK)

        except (ConnectionError, ValueError, RuntimeError):
            # LLMサービス接続エラー or 応答解析エラー
            # ここでエラーログを記録することが望ましい
            return Response(
                {"error": "フレーバーテキスト生成サービスへの接続に失敗しました。"},
                status=status.HTTP_503_SERVICE_UNAVAILABLE,  # Service Unavailable
            )
