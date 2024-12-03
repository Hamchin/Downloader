# Downloader

## 使用方法

```sh
python main.py --input-format [simple|standard]
```

## データ形式

### List

#### Simple

```json
[
    "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
]
```

#### Standard

```json
[
    [
        "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
        "2024-01-01.mp4"
    ],
]
```

### Dict

#### Simple

```json
{
    "0001": [
        "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
    ],
}
```

#### Standard

```json
{
    "0001": [
        [
            "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
            "2024-01-01.mp4"
        ],
    ],
}
```
