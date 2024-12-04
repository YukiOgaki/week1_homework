def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
    weather_information = [
        {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
        {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
        {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
        {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
        {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
        {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
        {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
        {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
    ]

    # Q1. 全国の平均気温を計算してください(9.5となればOK)
    temperature_total = 0

    for prefecture_citys in weather_information:
        temperature_total += prefecture_citys["temperature"]

    print(temperature_total / len(weather_information))

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
    osaka_stations = []

    for prefecture_citys in weather_information:
        if prefecture_citys["prefecture"] == "大阪府":
            osaka_stations.append(prefecture_citys["station"])
    str_osaka_stations = ",".join(osaka_stations)
    print(str_osaka_stations)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)
    fukuoka_temperatures = 0
    count = []

    for prefecture_city in weather_information:
        if prefecture_city["prefecture"] == "福岡県":
            fukuoka_temperatures += prefecture_city["temperature"]
            count.append(prefecture_city["temperature"])
    print(fukuoka_temperatures / len(count))


if __name__ == "__main__":
    main()
