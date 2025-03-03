{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qL5apVlTntxI",
        "outputId": "8187fdb9-a723-417a-b074-0d2b29d6d9e5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "('月曜日は晴れです', '火曜日は雨です', '水曜日は晴れです', '木曜日は晴れです', '金曜日は曇りです', '土曜日は曇りのち雨です', '日曜日は雷雨です')\n",
            "{'mon': '晴れ', 'tue': '雨', 'wed': '晴れ', 'thu': '晴れ', 'fri': '曇り', 'sat': '曇りのち雨', 'sun': '雷雨'}\n"
          ]
        }
      ],
      "source": [
        "# リスト（配列）を作成\n",
        "array = (\"月曜日は晴れです\", \"火曜日は雨です\", \"水曜日は晴れです\", \"木曜日は晴れです\", \"金曜日は曇りです\", \"土曜日は曇りのち雨です\", \"日曜日は雷雨です\",)\n",
        "\n",
        "# リストを出力\n",
        "print(array)\n",
        "\n",
        "# ディクショナリ（連想配列）を作成\n",
        "dictionary = {\"mon\": \"晴れ\", \"tue\": \"雨\",\"wed\": \"晴れ\", \"thu\": \"晴れ\", \"fri\": \"曇り\", \"sat\": \"曇りのち雨\", \"sun\": \"雷雨\"}\n",
        "\n",
        "# 連想配列を出力\n",
        "print(dictionary)"
      ]
    }
  ]
}