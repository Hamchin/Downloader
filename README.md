# Downloader

## 使用方法

```
python main.py --mode [video|image] --data-type [simple|standard]
```

## 補足

### --data-type = simple

```py
DATA_LIST = [
    "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
]
```

### --data-type = standard

```py
DATA_LIST = [
    (
        "https://XXXXXXXX/videos/XXXXXXXX.m3u8",
        "2023-01-01.mp4",
    ),
]
```
