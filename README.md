# Downloader

## 使用方法

```sh
python main.py --data-type [list|dict] --input-type [simple|standard] --output-type [video|image]
```

## 設定方法

### --data-type = list

#### --input-type = simple

```py
DATA_LIST = [
    "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
]
```

#### --input-type = standard

```py
DATA_LIST = [
    (
        "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
        "2023-01-01.mp4",
    ),
]
```

### --data-type = dict

#### --input-type = simple

```py
DATA_DICT = {
    "0001": [
        "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
    ],
}
```

#### --input-type = standard

```py
DATA_DICT = {
    "0001": [
        (
            "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
            "2023-01-01.mp4",
        ),
    ],
}
```
