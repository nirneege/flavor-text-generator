from google import genai
from google.genai import types

from flavor_text_generator.config.envitoments import GEMINI_API_KEY


def generate_flavor_text_from_llm(
    target_type: str,
    name: str,
    description: str,
    rarity: str | None = None,
    style_hint: str | None = None,
) -> str:
    """外部LLM APIを呼び出してフレーバーテキストを生成する関数"""
    # --- プロンプトの作成 ---
    prompt = "あなたは経験豊富なRPGのシナリオライターです。\n"
    prompt += (
        "以下の情報に基づいて、魅力的で簡潔なフレーバーテキストを生成してください。\n"
        "フレーバーテキストは、ゲーム内のアイテムやキャラクターの説明文として使用されます。\n"
        "プレイヤーが興味を持ち、ゲームの世界観に没入できるような内容にしてください。\n"
        "呼び出し元でレスポンステキストをそのまま利用できるように、装飾や改行は必要ありません。\n\n"
    )
    prompt += f"対象種別: {target_type}\n"
    prompt += f"名前: {name}\n"
    prompt += f"説明: {description}\n"
    if rarity:
        prompt += f"レアリティ: {rarity}\n"
    if style_hint:
        prompt += f"文体のヒント: {style_hint}\n"
    prompt += "\n生成するフレーバーテキスト:\n"

    # --- LLM API へのリクエスト ---
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=prompt,
            config=types.GenerateContentConfig(
                max_output_tokens=100,
                temperature=0.6,
                stop_sequences=["\n"],
            ),
        )

    except (KeyError, IndexError, ValueError) as e:
        # ここでログ記録などを行う
        raise ValueError from e

    # --- レスポンスの処理 ---
    if response.text is None:
        return ""
    return response.text


# 使用例 (テスト用)
# if __name__ == "__main__":
#     try:
#         text = generate_flavor_text_from_llm(
#             target_type="item",
#             name="癒やしのポーション",
#             description="飲むと傷が少し回復する液体。",
#             rarity="common",
#         )
#         print(text)
#     except Exception as e:
#         print(f"Error: {e}")
