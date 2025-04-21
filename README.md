# flavor-text-generator

RPG ゲームに利用するフレーバーテキストの生成を行う API アプリケーションです。

## 概要

このアプリケーションは、RPG ゲームにおけるフレーバーテキストを生成するための API を提供します。  
ユーザーは、特定のテーマやキーワードに基づいて、キャラクターやアイテム、場所などの説明文を生成することができます。  
このアプリケーションは、Python と FastAPI を使用して構築されており、Google の Gemini API を利用してテキスト生成を行います。

## 利用例

アプリケーションを起動し、以下のようなコマンドを実行します。

```bash
curl -X POST http://127.0.0.1:8000/api/v1/flavor-text/generate/ -H "Content-Type: application/json" -d '{
    "target_type": "item",
    "name": "きずぐすり",
    "description": "飲むと傷が少し回復する液体。市販されている",
    "rarity": 1,
    "style_hint": "old styled, traditional, like dungeon and dragons, hard"
}'
```

以下のレスポンスが返されます。

```json
{"flavor_text":"浅き創を癒す、ありふれたる薬。街の薬屋にて容易に入手可能なり。"}
```
